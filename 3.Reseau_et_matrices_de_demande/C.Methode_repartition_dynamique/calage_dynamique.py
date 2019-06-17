# -*- coding: utf-8 -*-
from toolbox import *

## Folder names ##
Docs=  "C:\\Users\\AlexandreNicolas\\Documents\\C0709 DIRMED\\"
DossierReseau= Docs + "5_TRAVAIL\\CreationReseau_MATLAB\\"
DossierSIREDO= Docs + "2_DONNEES\\SIREDO\\A50_6MIN\\"
DossierBretelles= Docs + "2_DONNEES\\Comptages_bretelle\\"
DossierFCD= Docs + "2_DONNEES\\FCD\\"
##

## Period under consideration ##
heure_min= datetime.strptime("06:00","%H:%M").time()
heure_max= datetime.strptime("10:00","%H:%M").time()

O_set= list([34,37,19,20,42,43]) # possible origin nodes
D_set= list([4,46,30,45,36,]) # possible destination nodes

noms_des_noeuds= { } # labels associated with foregoing node IDs

##

## Congestion detection parameters ##
congestion_threshold= 1.25 # if travel times exceed congestion_threshold * free travel time, then congestion is assumed
coef_passage_2016_2019_bretelles= { 56: 1.29, 57: 1.01, 60: 0.86, 61: 0.86, 62: 0.85, 53: 0.99, 166: 0.99}
#!! ratio between flows at entrances exits deduced for 2019 (from main road) over those measured in 2016
## ##

## Initialisation of dataframes ##
DEBITS= pd.DataFrame()
FCDS= pd.DataFrame()
DEPRATES= pd.DataFrame()
CONGESTED= pd.DataFrame()
first_congestion_time= heure_max
##


###
def findPath(node_destination, explored_nodes, current_node, current_path):
	path_set= set([])

	if len(current_path)>50: # do not allow paths longer than 50 links
		return path_set

	for try_link in NOEUDS["links_from_node"][current_node]:

		if try_link[1]== node_destination:
			path_set.add( tuple(current_path+[try_link[0]]) )

		elif try_link[1] not in explored_nodes:
			path_set_d= findPath(node_destination, explored_nodes.union([try_link[1]]), try_link[1], current_path+[try_link[0]])
			if len(path_set_d)>0:
				path_set= path_set.union(path_set_d)

	return path_set

###

def get_flow_SIREDO(postes_SIREDO, link):
	global DEBITS
	nb_SIREDOS= len(postes_SIREDO)

	SIREDO= list( [] )

	for cpt in range(nb_SIREDOS):
		monSIREDO= postes_SIREDO[cpt]
		if os.path.isfile("%s%s_JOB.csv"%(DossierSIREDO,monSIREDO)):
			SIREDO.append( pd.read_csv("%s%s_JOB.csv"%(DossierSIREDO,monSIREDO), encoding='utf-8', header=0, converters={"heure": format_time, "debit": float, "vitesse": float}, delimiter=';', index_col= 0) )

	DEBITS[link]= -1.0 # new column to receive flow on this link

	if len(SIREDO)==0:
		return -1 # no SIREDO measurements on this link


	if DEBITS.shape[0]==0:
		cols= DEBITS.columns.copy().tolist()
		DEBITS= pd.DataFrame(index=SIREDO[0].index.copy())
		for mycol in cols:
			DEBITS[mycol]= -1.0

	for heure in DEBITS.index.tolist():
		debits= list( [] )
		for cpt in range(nb_SIREDOS):
			try:
				debits.append( (SIREDO[cpt]).at[heure,"debit"] )
			except:
				pass
		DEBITS.at[heure,link]= 10.0 * np.mean(debits) # convert to flows per hour

	DEBITS_loc= DEBITS.loc[ (DEBITS.index >= heure_min) & (DEBITS.index < first_congestion_time)]

	mondebit= get_mean(DEBITS_loc[link])
	#print(" Debit moyen sur la periode consideree sur l'arc %s: %.2f"%(link,mondebit))

	return mondebit


def get_flow_comptages(numposte, link):
	global DEBITS

	if not os.path.isfile("%sposte%i_JOB.csv"%(DossierBretelles,numposte)):
		print(" $ python write_SIREDO3.py %i"%(numposte))
		os.system("python write_SIREDO3.py %i"%(numposte))

	Comptages= pd.read_csv("%sposte%i_JOB.csv"%(DossierBretelles,numposte), encoding='utf-8', header=0, converters={"heure": format_time, "debit": float, "vitesse": float}, delimiter=';', index_col=0 )

	Comptages["debit"]= 10.0 * Comptages["debit"] # convert to flows per hour

	##!! Adjust measurements to situation as of 2019
	if numposte in coef_passage_2016_2019_bretelles.keys():
		Comptages["debit"]= coef_passage_2016_2019_bretelles[numposte] * Comptages["debit"]
	##

	if DEBITS.shape[0]==0:
		cols= DEBITS.columns.copy().tolist()
		DEBITS= pd.DataFrame(index= Comptages.index.copy())
		for mycol in cols:
			DEBITS[mycol]= -1.0

	DEBITS[link]= 0.0 # new column to receive flow on this link

	for heure in DEBITS.index.tolist():
		try:
			DEBITS[link][heure]= Comptages.at[heure,"debit"]
		except:
			pass

	DEBITS_loc= DEBITS.loc[ (DEBITS.index >= heure_min) & (DEBITS.index < first_congestion_time)]
	mondebit= get_mean(DEBITS_loc[link])
	#print(" Debit moyen sur la periode consideree sur l'arc %s: %.2f"%(link,mondebit))

	return mondebit




def get_FCD_time(link):
	global FCDS

	if not os.path.isfile("%s%s_JOB.csv"%(DossierFCD, link)): # No FCD time available
		if FCDS.shape[0]==0:
			get_FCD_time("A50db") # to create hour indices

		FCDS[link]= float(LINKS.at[link, "FFT"]) # new column to receive flow on this link; fill FCDS with free travel time if no data are avaiable
		return FCDS[link][0]

	FCD= pd.read_csv("%s%s_JOB.csv"%(DossierFCD, link), encoding='utf-8', header=0, converters={"heure": format_time, "vitesse": float, "temps_de_parcours": float, "std_vitesse": float, "std_temps_de_parcours": float, "nombre_vehicules_flottants": int}, delimiter=';', index_col= 0)


	if FCDS.shape[0]==0:
		FCDS= pd.DataFrame(index= FCD.index.copy())

	FCD= FCD.loc[ (FCD["nombre_vehicules_flottants"] >=1)   ]

	FCDS[link]= float(LINKS.at[link, "FFT"]) # new column to receive flow on this link; fill FCDS with free travel time if no data are avaiable

	for heure in FCDS.index.tolist():
		try:
			FCDS[link][heure]= FCD.at[heure,"temps_de_parcours"]
		except:
			print(" Je n'ai pas trouve l'heure %s cherchee"%heure)
			pass

	FCDS_loc= FCDS.loc[ (FCDS.index >= heure_min) & (FCDS.index < heure_max)]
	montpsdeparcours= get_mean(FCDS_loc[link])
	print(" Temps de parcours moyen sur la periode consideree sur l'arc %s: %.2fs"%(link,montpsdeparcours))

	return montpsdeparcours


def get_total_path_flow(paths):
	PATHS_loc= PATHS.loc[ paths ]
	somme= 0.0
	for elt in PATHS_loc["flow"].tolist(): # discard unavailable flow data (-1). In any event, "get_min_flow" will only keep min element, so let's put as many reasonable constraints as possible
		somme+= (elt if elt!=-1 else 0.0)

	return (somme if somme>0 else -1)

def get_min_flow(links, mypath):
	LINKS_loc= LINKS.loc[ links ]
	LINKS_loc= LINKS_loc.loc[ LINKS_loc["flow"]>= 0 ].copy()

	if LINKS_loc.shape[0]==0:
		print("Je n'ai trouve aucun flux sur le chemin %i"%mypath)
		return 0.0

	LINKS_loc["total_path_flow"]= LINKS_loc["paths"].apply( get_total_path_flow )
	LINKS_loc["partial_path_flow"]= LINKS_loc.apply(lambda row: row.flow if row.total_path_flow<0 else (
														    PATHS["flow"][mypath] / row.total_path_flow * row.flow), axis=1)
	return get_min(LINKS_loc["partial_path_flow"])

def to_seconds(heure):
	return 3600*heure.hour + 60*heure.minute

def get_closest_time(heure):
	heures= FCDS.index.tolist()
	cpt_min= np.argmin( list ( map(lambda h: abs((to_seconds(h)-heure+43200) % 86400 - 43200), heures) ) ) # tested
	return heures[cpt_min]


def get_total_dyn_path_flow(paths, mylink, heure_seconds, MayILeavePathsBehind):

	mayI= bool(MayILeavePathsBehind[0])
	MayILeavePathsBehind[0]= True # encapsulated boolean that is true if the contributions from all incoming paths were reckoned for this link

	sum_deprates= 0.0

	for mypath in paths:
		links_loc= PATHS.at[mypath,"links"].copy() # travel back in time to the beginning of this path
		links_loc.reverse()

		GameIsOn= False # the Game starts when the link of interest is encountered, while travelling backwards along the path
		FreelyFlowing= True # has jamming been encountered after the game has started
		DeltaT= 0.0 # travel time to present link

		for link in links_loc:
			if GameIsOn:
				heure_loc= get_closest_time(heure_seconds-DeltaT)
				DeltaT+= FCDS.at[ heure_loc, link ]

				if CONGESTED.at[ heure_loc, link]:
					MayILeavePathsBehind[0]= False # At least one path contribution cannot be properly reckoned
					if mayI: # Paths that have already encountered a congested section count for nothing towards the flow share on the link under study, because their departure rate is higher than the flow rate at this link
						FreelyFlowing= False
						break

			if link==mylink:
				GameIsOn= True # start counting up travel time (remember that links are in reverse order)

		deprate= DEPRATES.at[ get_closest_time(heure_seconds-DeltaT), mypath]
		if FreelyFlowing: # only sum departure rates on paths that are freely flowing up to link under study
			sum_deprates+= (deprate if deprate>0.0 else 0.0)
		#else:
		#	print("J'ai connu un embouteillage autour de %s sur la route %s"%(heure_loc,link))

	return sum_deprates


def get_dynamical_min_flow(links, mypath, heure):

	heure_seconds= to_seconds(heure)
	DeltaT= 0.0

	heure_loc= get_closest_time( to_seconds(heure) + DeltaT) # closest to heure_loc

	debit_mypath= DEPRATES.at[heure_loc,mypath]
	flow_max= -1

	LINKS_dyn= LINKS.loc[ links ].copy()

	LINKS_dyn["total_path_flow"]= -1.0
	LINKS_dyn["partial_path_flow"]= -1.0
	# These links are travelled through at different times

	MayILeavePathsBehind= list([False])

	for link in links:
		# perform this process until congestion is found #
		if CONGESTED.at[heure_loc, link] and flow_max>0.0: # do not break before at least one link with measured flow has been handled
			break
		# #

		LINKS_dyn.at[link,"total_path_flow"]= get_total_dyn_path_flow(LINKS_dyn.at[link,"paths"], link, heure_seconds + DeltaT, MayILeavePathsBehind)
		LINKS_dyn.at[link,"partial_path_flow"]= DEBITS.at[heure_loc,link] if LINKS_dyn.at[link,"total_path_flow"]<=0 else (
												debit_mypath / LINKS_dyn.at[link,"total_path_flow"] * DEBITS.at[heure_loc,link])

		flow_max= max(flow_max,LINKS_dyn.at[link,"partial_path_flow"])

		# Update times
		DeltaT+= FCDS.at[heure_loc,link]
		heure_loc= get_closest_time( heure_seconds + DeltaT  )

	return get_min(LINKS_dyn["partial_path_flow"])

def detect_congestion():
	global CONGESTED, first_congestion_time

	CONGESTED= pd.DataFrame(index= FCDS.index.copy())
	for link in FCDS.columns.tolist():
		tps_min= np.percentile(FCDS[link], 30.)
		CONGESTED[link]= FCDS[link].apply(lambda t: t > congestion_threshold * tps_min)

	# Get rid of spurious fluctuations: congestion exists only if it existed just before or persists afterwards
	for link in FCDS.columns.tolist():
		myCol= CONGESTED[link]
		for cpt in range(myCol.shape[0]):
				CONGESTED[link].iat[cpt]= myCol.iat[cpt] and (myCol.iat[max(0,cpt-2)] or myCol.iat[max(0,cpt-1)] or myCol.iat[min(myCol.shape[0]-1,cpt+1)] or myCol.iat[min(myCol.shape[0]-1,cpt+2)])

		CONGESTED_LINK=  CONGESTED.loc[ CONGESTED[link] ]
		if CONGESTED_LINK.shape[0]>0:
			first_cong_loc= CONGESTED_LINK.index.min()
			if first_cong_loc<first_congestion_time:
				first_congestion_time= first_cong_loc


	print(" * La premiere congestion s'est produite a %s"%first_congestion_time)
	first_congestion_time= get_closest_time( to_seconds(first_congestion_time) - 600 ) # departure time to avoid any congestion

###


## LOADING nodes from Excel file ##
NOEUDS= pd.read_excel(DossierReseau+"reseau_FCD.xlsx", sheet_name="noeuds",  usecols= [0,1,2,3], header= 0, dtype={"X": float, "Y": float, "ID": int,  "NUMROUTE": str})
NOEUDS["links_from_node"]= NOEUDS.apply(lambda row: list([]), axis=1)
NOEUDS["links_to_node"]= NOEUDS.apply(lambda row: list([]), axis=1)
NOEUDS.set_index('ID', inplace= True)
## ##

## LOADING links from Excel file ##
LINKS= pd.read_excel(DossierReseau+"reseau_FCD.xlsx", sheet_name="arcs", usecols= range(0,31), header= 0, index_col= None,
					converters={
					"Nom_court": str,
					"Lien_no": int,
					"NUM_ROUTE": str,
					"VOIES": int,
					"Capacity": float,
					"longueur": float,
					"FFT": float,
					"SENS": str,
					"Nstart": int,
					"Nend": int,
					"Postes_comptage": get_int,
					"SIREDO": format_list_strings })

# Filter links
LINKS= LINKS.loc[ LINKS["SENS"]=='O' ] # only include direction East to West for the time being

LINKS["xstart"]= LINKS["Nstart"].apply(lambda n: NOEUDS["X"][n])
LINKS["ystart"]= LINKS["Nstart"].apply(lambda n: NOEUDS["Y"][n])
LINKS["xend"]= LINKS["Nend"].apply(lambda n: NOEUDS["X"][n])
LINKS["yend"]= LINKS["Nend"].apply(lambda n: NOEUDS["Y"][n])

LINKS.sort_values(by=['NUM_ROUTE','xstart'], inplace= True)
LINKS["paths"]= LINKS.apply(lambda row: list([]), axis=1)  # paths going through this link
LINKS["flow"]= -1.0 # empirical flow on this link
LINKS["temps_de_parcours"]= -1.0 # empirical flow on this link

LINKS.set_index(["Nom_court"],inplace=True, drop= True)
## ##

PATHS= pd.DataFrame(columns=["O","D","OD","links"])

def load_network():
	global NOEUDS, LINKS, PATHS, DEBITS, DEPRATES

	# Write links

	#!! link_index= 1 # MATLAB indices start from 1
	noeud_index= 1 # MATLAB indices start from 1

	# Get measured travel time on the link (data since beginning of 2018)
	for row in LINKS.itertuples():
		LINKS.at[row.Index,"temps_de_parcours"]= get_FCD_time(row.Index)

	# Detect congestion_threshold
	print(" * I am checking for congestion")
	detect_congestion()

	for row in LINKS.itertuples():
		print(" * Traitement du lien %s"%row.Index)

		NOEUDS["links_from_node"][row.Nstart].append( (row.Index,row.Nend) )
		NOEUDS["links_to_node"][row.Nend].append( (row.Index,row.Nstart) )



		# Get measured flow on the link
		if len(row.SIREDO) > 0: # comptage en section courante
			LINKS.at[row.Index,"flow"]= get_flow_SIREDO(row.SIREDO, row.Index)
		elif row.Postes_comptage >=0: # comptage aux bretelles
			LINKS.at[row.Index,"flow"]= get_flow_comptages(row.Postes_comptage, row.Index)
		else:
			DEBITS[row.Index]= -1.0



	## SELECT possible OD paths ##
	ODS= pd.DataFrame(columns=["O","D","paths"])

	for O in O_set:
		for D in D_set:
			ODS= ODS.append({"O": O, "D": D, "paths": list([])}, ignore_index= True)

	for row_OD in ODS.itertuples():
		PathSubSet= findPath(row_OD.D, set([]), row_OD.O, [])

		for mypath in PathSubSet:
			PATHS= PATHS.append({"O": row_OD.O,
						  "D": row_OD.D,
						  "OD": row_OD.Index,
						  "links": list(mypath)}, ignore_index=True)
			for link in mypath:
				LINKS["paths"][link].append( PATHS.shape[0]-1 ) # index of last row


	PATHS["length"]= PATHS["links"].apply(lambda x: len(x))
	PATHS["flow"]= -1
	## ##

	# Flux moyens par chemin sur la periode consideree
	print(" *  I am computing the average flow rates")
	for cpt in range(5):
		PATHS["flow"]= PATHS.apply(lambda row: get_min_flow(row.links,row.name), axis=1)


	DEPRATES= pd.DataFrame(index= DEBITS.index.copy())

	for row_PATH in PATHS.itertuples():
		DEPRATES[row_PATH.Index]= float(row_PATH.flow) # series initialised with constant flow value

	#!! return PATHS#!!

	# Flux dynamiques par chemin
	print(" * I am computing the series of depature rates")
	heures_avant_congestion= DEPRATES.loc[ (DEPRATES.index >= heure_min) & (DEPRATES.index < first_congestion_time) ].index.tolist()
	for cpt in range(3):
		for heure in heures_avant_congestion:
			print("Il est %s"%heure)
			for row_PATH in PATHS.itertuples():
				DEPRATES.at[heure,row_PATH.Index]= get_dynamical_min_flow(row_PATH.links, row_PATH.Index, heure)

	print(" * Now, I am considering the network after congestion, i.e., after %s"%first_congestion_time)
	# No iteration for congested network
	heures_apres_congestion= DEPRATES.loc[ (DEPRATES.index >= first_congestion_time) & (DEPRATES.index < heure_max) ].index.tolist()
	for heure in heures_apres_congestion:
		print("Il est %s"%heure)
		for row_PATH in PATHS.itertuples():
			DEPRATES.at[heure,row_PATH.Index]= get_dynamical_min_flow(row_PATH.links, row_PATH.Index, heure)

	print(DEPRATES.head())

	return PATHS

load_network()


DEPRATES_loc= DEPRATES.loc[  (DEPRATES.index >= heure_min) & (DEPRATES.index < heure_max) ]
print(" * Volume sur la periode consideree par OD  ",(DEPRATES_loc.sum() / 10.))
print(" * Volume global sur la periode consideree : %i "%(DEPRATES_loc.sum().sum() / 10.))


print("* I am dumping the data in a Pickle file")


pickle.dump(DEPRATES, open(DossierReseau+"deprates.p",'wb'))
pickle.dump(PATHS, open(DossierReseau+"paths.p",'wb'))

## FILTER & SORT dataframes ##
noeuds_loc= list(set(LINKS["Nstart"]).union(set(LINKS["Nend"])))
NOEUDS= NOEUDS.loc[ noeuds_loc  ]
indices_NOEUDS= NOEUDS["X"].reset_index(drop= True, inplace= False)
NOEUDS["indices"]= indices_NOEUDS.index.copy() + 1
NOEUDS.sort_values(by=["indices"], inplace= True) # a priori, this is useless

indices_LINKS= LINKS["VOIES"].reset_index(drop= True, inplace= False)
LINKS["indices"]= indices_LINKS.index.copy() + 1
LINKS.sort_values(by=["indices"], inplace= True)

indices_PATHS= PATHS["O"].reset_index(drop= True, inplace= False)
PATHS["indices"]= indices_PATHS.index.copy() + 1
PATHS.sort_values(by=["indices"], inplace= True)


## ##

# Write data
print("* I am now writing the data in a file")

with open(DossierReseau+"vue_d_ensemble_FCD.txt",'w') as monfichier:
	monfichier.write("O;D;flux")
	for row in PATHS.itertuples():
		monfichier.write("\n%s;%s;%.3f"%(row.O,row.D,row.flow))


with open(DossierReseau+"codage_MATLAB_FCD.txt",'w') as monfichier:

	## WRITE links ##
	monfichier.write("linkData= [\n")

	for row in LINKS.itertuples():

		monfichier.write("%i %i %.2f %.4f %.1f  1; %% %i-th link (%s)\n"%(
										NOEUDS["indices"][row.Nstart],
										NOEUDS["indices"][row.Nend],
										row.Capacity,
										row.longueur,
										row.FFT,
										row.indices,
										row.Index
										)
										)

	monfichier.write("];\n\n")

	## WRITE nodes ##
	monfichier.write("nodeCoordinates= [ \n")

	for row in NOEUDS.itertuples():
		monfichier.write("%.2f %.2f; %% %i-th node (%i)\n"%(
										row.X,
										row.Y,
										row.indices,
										row.Index
										)
										)
	monfichier.write("];\n\n")

	## WRITE paths ##
	len_max= PATHS["length"].max()
	print("  le plus long chemin comporte %i arcs"%len_max)

	monfichier.write("pathList= [\n")

	for row in PATHS.itertuples():
		for cpt in range(len_max):
			if cpt < row.length:
				monfichier.write("%i "% LINKS.at[row.links[cpt],"indices"])
			else:
				monfichier.write("0 ")
		monfichier.write("; %% %i-th path (%i)\n"%(row.indices, row.Index))
	monfichier.write("];\n\n")


	## WRITE departure rates ##
	dt= 5.0
	nt= int( (to_seconds(heure_max) - to_seconds(heure_min)) / dt) + 1 # number of time steps

	print("  Il y aura %i pas de temps"%nt)

	monfichier.write("pathDepartures= [\n")
	for row in PATHS.itertuples():
		myDepRates= DEPRATES[row.Index] # real path label, and not MATLAB index
		for cpt2 in range(nt):
			time_loc= get_closest_time( to_seconds(heure_min) + cpt2 * dt )
			depRate= myDepRates[time_loc] / 3600.0 # Convert to departure rates per second
			aleas= 0.0 # no fluctuation for the time being #  0.1*(random.random()-0.5)#!!
			monfichier.write("%.3f "%( (1.0+aleas)*depRate ) )
		monfichier.write("; %% %i-th path (%i)\n"%(cpt+1,row.Index))
	monfichier.write("];\n\n")

	print("J'ai tout fini!")
	"""
	# Write Network planning Parameters

	monfichier.write("OD_demand= [\n")
	for rate in depRates_OD:
		monfichier.write("%.3f;"%rate)
	monfichier.write("];\n\n")

	monfichier.write("T_A= [ ")
	for rate in depRates_OD:
		monfichier.write("%.3f "%(9.00)) # preferred time of arrival
	monfichier.write("];\n\n")
	"""

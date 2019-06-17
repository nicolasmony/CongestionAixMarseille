# -*- coding: utf-8 -*-

### Imports ###
from scipy import *
from math import acos
import pandas, os.path
from datetime import datetime
from enum import Enum
import re


### File names ###
GeneralFolder= ""
SaveFolder=""

### Parameters ###


noeud_from_id= {}

def chercheSens(s):
	if s=='Double sens':
		return 2
	else:
		return 1


print("* Reading input data")


def findPath(links, node_destination, explored_nodes, current_node, current_path):

	path_set= set([])

	if len(current_path)>50:
		return path_set
		
	for try_link in links[current_node]:
			
		if try_link[0]== node_destination:
			path_set.add( tuple(current_path+[try_link[1]]) )
			
		elif try_link[0] not in explored_nodes:
			path_set_d= findPath(links, node_destination, explored_nodes.union([try_link[0]]), try_link[0], current_path+[try_link[1]])
			if len(path_set_d)>0:
				path_set= path_set.union(path_set_d)
	return path_set


reseau= pandas.read_excel(GeneralFolder+"reseau_perimetre.xlsx", sheet_name="reseau_perimetre", usecols= range(1,31), header= 0, index_col= None,
converters={"NUM_ROUTE": str, 
"xstart": float, 
"ystart": float, 
"xend": float, 
"yend": float, 
"VOIES": int, 
"Capacity": float, 
"LONGUEUR": float,
"FFT": float,
"SENS": chercheSens,
"Nstart": int,
"Nend": int })



noeuds= pandas.read_excel(GeneralFolder+"reseau_perimetre.xlsx", sheet_name="noeuds", usecols= [1,2,3], header= 0, dtype={"X": float, "Y": float, "ID": int})
noeuds.set_index('ID', inplace= True)


reseau= reseau.loc[ (reseau["NUM_ROUTE"]== 'A50') | (reseau["NUM_ROUTE"]== 'A501') | (reseau["NUM_ROUTE"]== 'D2') ]
reseau.sort_values(by=['NUM_ROUTE','xstart'], inplace= True)



with open(SaveFolder+"codage_MATLAB.txt",'w') as monfichier:

	noeuds_loc= list(set(reseau["Nstart"]).union(set(reseau["Nend"])))
	links_per_node= [ list([]) for noeud in range(len(noeuds_loc)+1) ] # each item is a pair (end node, link number)
	
	# Write links

	monfichier.write("linkData= [\n")
	link_index= 1 # MATLAB indices start from 1
	noeud_index= 1 # MATLAB indices start from 1
	
	for row in reseau.itertuples():
	
		if row.xend <= row.xstart and row.SENS==1: # only include direction West to East for the time being
			continue
			
		# Fill dictionary with node IDs
		if row.Nstart not in noeud_from_id:
			noeud_from_id[row.Nstart]= noeud_index
			noeud_index+= 1
		if row.Nend not in noeud_from_id:
			noeud_from_id[row.Nend]= noeud_index
			noeud_index+= 1
			
		noeud_start= noeud_from_id[row.Nstart]
		noeud_end= noeud_from_id[row.Nend]
		
		if row.xend > row.xstart: # first consider direction from Marseille to Aubagne
			monfichier.write("%i %i %.2f %.4f %.1f  1; %% link %i\n"%(noeud_start, noeud_end, row.Capacity, row.LONGUEUR, row.FFT, link_index))
			links_per_node[noeud_start].append( (noeud_end, link_index) )
			link_index+= 1
		else: # then it is a bidirectional road
			monfichier.write("%i %i %.2f %.4f %.1f 1; %% link %i\n"%(noeud_end,noeud_start, row.Capacity, row.LONGUEUR, row.FFT, link_index))
			links_per_node[noeud_end].append( (noeud_start, link_index) )
			link_index+= 1

	monfichier.write("];\n\n")

	# Write nodes

	monfichier.write("nodeCoordinates= [ \n")

	for noeud in sorted(noeud_from_id, key= lambda x: noeud_from_id[x]):
		monfichier.write("%.2f %.2f; %% node %i\n"%(noeuds["X"][noeud], noeuds["Y"][noeud],noeud_from_id[noeud]))

	monfichier.write("];\n\n")

	##### Write paths #####
	OD_set= list( [ 
	(noeud_from_id[253],noeud_from_id[294]), # A50 from Marseille to La Tourtelle approximately
	(noeud_from_id[253],noeud_from_id[99]), # A50-A501 from Marseille to Aubagne
	(noeud_from_id[253],noeud_from_id[195]) # A50-A501 from Marseille past Aubagne
	])
	depRates_OD= list( [
	0.89,
	0.5,
	0.04
	] )
	depRates_path= list([])
	##### #####
	
	
	PathSet= set([])
	nb_paths_per_OD= [ 0 for OD in OD_set]
	
	for cpt_OD in range(len(OD_set)):
		OD= OD_set[cpt_OD]
		PathSubSet= findPath(links_per_node, OD[1], set([]), OD[0], [])
		nb_paths_per_OD[cpt_OD]= len(PathSubSet)
		for cpt_pss in range(len(PathSubSet)):
			depRates_path.append( depRates_OD[cpt_OD] / nb_paths_per_OD[cpt_OD] ) #!!
		PathSet= PathSet.union(PathSubSet )

	len_max= max( len(path) for path in PathSet )
	nb_paths= len(PathSet)
	

	path_index= 1 # MATLAB indices start from 1
	monfichier.write("pathList= [\n")
	for path in PathSet:
		for cpt in range(len_max):
			if cpt<len(path):
				monfichier.write("%i "%path[cpt]) 
			else:
				monfichier.write("0 ")
		monfichier.write("; %% path %i\n"%(path_index))
		path_index+= 1
	monfichier.write("];\n\n")


	# Write departure rates
	nt= int(3600./10.)+1 # number of time steps
	
	monfichier.write("pathDepartures= [\n")
	for cpt in range(nb_paths):
		depRate= depRates_path[cpt]
		for cpt2 in range(nt):
			monfichier.write("%.3f "%depRate)
		monfichier.write("; %% path %i\n"%(cpt+1))
	monfichier.write("];\n\n")
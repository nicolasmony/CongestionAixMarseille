# -*- coding: UTF-8 -*-

import sys
import glob
#import matplotlib.pyplot as plt
import itertools
import operator
from math import atan,sqrt


###############  A MODIFIER PAR L'UTILISATEUR  ######################

#annees = [2015,2016]
#mois=['01','02','03','04','05','06','07','08','09','10','11','12']
annees = [2016]
mois = ['01','02','03','04','05']

#####################################################################


##############   DEFINITION DES PRINCIPALES FONCTIONS ###############

def valide(trafic):
    debit = trafic[0]
    conce = trafic[1]
    vites = trafic[2]
    if debit == 0 or conce < 1 or vites == 0:
        return False
    elif vites > 150:
        return False
    else:
        return True


def tournant(p1, p2, p3):
    indica = (p2[0]-p1[0])*(p3[1]-p1[1])-(p2[1]-p1[1])*(p3[0]-p1[0])
    if indica == 0:
        return 'aligne'
    elif indica > 0:
        return 'gauche'
    else:
        return 'droite'


###traitement du nuage de point pour calculer le diagramme fondamental###
def recherchedroites(nuage):
    # filtrage des points extremes
    nbpoints = len(nuage)
    nuage.sort(key=operator.itemgetter(0))
    nuage = nuage[:-int(0.0002 * nbpoints)]

    # calcul de l'ensemble des pentes et coordonnees a l'origine pour toutes les droites passant par deux points du nuage
    # recherche de l'ensemble de droites qui vont definir l'enveloppe convexe
    print("recherche des droites de l\'enveloppe")
    dicoDroites = {}
    dicoPoints = {}
    nbcouples = len(nuage) ** 2
    avancement = 0
    indice = 0
    for couplepoint in itertools.product(nuage, nuage):
        av = int(100 * indice / nbcouples)
        if av != avancement:
            print(str(av) + '%')
            avancement = av
        k1 = couplepoint[0][1]
        q1 = couplepoint[0][0]
        k2 = couplepoint[1][1]
        q2 = couplepoint[1][0]
        if k1 != k2:
            pentecour = int((q2 - q1) / (k2 - k1))
            coordo = q1 - pentecour * k1
            if -18 <= pentecour <= 130 and coordo >= 0:
                try:
                    coordorigin = dicoDroites[pentecour]
                    if coordo > coordorigin:
                        dicoDroites[pentecour] = coordo
                        dicoPoints[pentecour] = (
                        couplepoint[0][1], couplepoint[0][0], couplepoint[1][1], couplepoint[1][0])
                except KeyError:
                    dicoDroites[pentecour] = coordo
                    dicoPoints[pentecour] = (couplepoint[0][1], couplepoint[0][0], couplepoint[1][1], couplepoint[1][0])
        indice += 1

    del dicoDroites

    xretenus = []
    yretenus = []
    coordretenus = []
    for key, value in dicoPoints.items():
        xretenus.append(value[0])
        xretenus.append(value[2])
        yretenus.append(value[1])
        yretenus.append(value[3])
        coordretenus.append(value[:2])
        coordretenus.append(value[2:])
    return coordretenus


###algo enveloppe convexe a partir des points trouves (parcours de graham)
def calculenveloppe(coordretenus):
    # tri sur les ordonnees pour obtention du pivot
    coordretenus.sort(key=operator.itemgetter(1, 0))
    pivot = coordretenus[0]
    coordretenus = coordretenus[1:]
    # creation de la base avec angle puis tri
    baseAngles = []
    for point in coordretenus:
        xNvRepere = point[0] - pivot[0]
        yNvRepere = point[1] - pivot[1]
        thetaPoplaire = 2 * atan(yNvRepere / (xNvRepere + sqrt(xNvRepere ** 2 + yNvRepere ** 2)))
        baseAngles.append((point[0], point[1], thetaPoplaire))

    baseAngles.sort(key=operator.itemgetter(2))
    print([coord[0] for coord in baseAngles])
    print([coord[1] for coord in baseAngles])
    print([coord[2] for coord in baseAngles])
    enveloppeConvexe = [pivot, baseAngles[0][:2]]
    for point in baseAngles[1:]:
        vitesse = (point[1] - enveloppeConvexe[-1][1]) / (point[0] - enveloppeConvexe[-1][0])
        if tournant(enveloppeConvexe[-2], enveloppeConvexe[-1], point) == 'gauche':
            if -30 <= vitesse <= 130:
                enveloppeConvexe.append(point[:2])
        else:
            while tournant(enveloppeConvexe[-2], enveloppeConvexe[-1], point) == 'droite':
                vitesse = (point[1] - enveloppeConvexe[-2][1]) / (point[0] - enveloppeConvexe[-2][0])
                if -30 <= vitesse <= 130:
                    del enveloppeConvexe[-1]
                else:
                    break
            if -30 <= vitesse <= 130:
                enveloppeConvexe.append(point[:2])

    enveloppeConvexe.sort(key=operator.itemgetter(0))
    return enveloppeConvexe

###############################################################################################

#################################  CORPS DU SCRIPT ############################################

chemin = sys.path[0]
baseDeDonnees = {}

with open('diagrammesfondamentaux.csv','w') as sortie1:
    sortie1.write('code;concentration;debit\n')
with open('caractersitiques.csv','w') as sortie2:
    sortie2.write('code;capacite;vitesseAvide;concentrationCritique\n')


print('recuperation des donnees')
for an in annees:
    print('recuperation annee '+str(an))
    for mm in mois:
        print('mois ', mm)
        recherche = chemin + '\\D6MN\\'+str(an)+'\\'+mm+"//*.dat"
        liste_archive = glob.glob(recherche)

        for archive in liste_archive:
            try:
                with open(archive) as siredo:
                    data=siredo.readlines()
                    for pointBrut in data:
                        pointDonnees = pointBrut.split(';')
                        rgs = pointDonnees[0]
                        debit = []
                        vitesse = []
                        concentration = []
                        try:
                            for i in range(6):
                                debit.append(int(pointDonnees[i+6]))
                                vitesse.append(int(pointDonnees[i+13]))
                                if int(pointDonnees[i+6]) > 0 and int(pointDonnees[i+13]) > 0:
                                    concentration.append(int(pointDonnees[i+6])/int(pointDonnees[i+13]))
                                else:
                                    concentration.append(0)
                            accident = int(pointDonnees[20])
                            indic = pointDonnees[22].strip().replace(' ', '')
                        except (ValueError, IndexError):
                            #print(pointBrut)
                            continue

                        if len(indic) == 0 and accident == 0:
                            debitTot = sum(debit)
                            concentrationTot = sum(concentration)
                            if debitTot > 0 and concentrationTot > 0:
                                vitesseTot = debitTot/concentrationTot
                            else:
                                vitesseTot = 0
                            pointTraite = (debitTot, concentrationTot, vitesseTot)
                            if valide(pointTraite):
                                try:
                                    baseDeDonnees[rgs].append(pointTraite)
                                except KeyError:
                                    baseDeDonnees[rgs] = [pointTraite]

            except FileNotFoundError:
                print("mois "+mm+" inexistant")
                continue

print('traitement des donnes')
for key, values in baseDeDonnees.items():
    print('recherche du diagramme pour le point '+key)
    print('nombre de points pour le point '+key+' : '+str(len(values))+' exemple : ', values[0])
    # obtention de points uniques sevant de base a l'enveloppe
    coordretenus = list(set(recherchedroites(values)))
    enveloppeConvexe=calculenveloppe(coordretenus)

    debits=[point[1] for point in enveloppeConvexe]
    concentrations=[point[0] for point in enveloppeConvexe]
    #plt.plot([point[1] for point in values], [point[0] for point in values], 'bo', concentrations, debits, 'r-')
    #plt.show()
    #print([point[0] for point in enveloppeConvexe])
    #print([point[1] for point in enveloppeConvexe])

    capacite=max(debits)
    concentrationCrit=concentrations[debits.index(capacite)]
    listeVitesse=[(debits[i]-debits[i-1])/(concentrations[i]-concentrations[i-1]) for i in range(1,len(enveloppeConvexe)) if concentrations[i]-concentrations[i-1]>2]
    vitesseVide=max(listeVitesse)
    #print("vitesse a vide : ", vitesseVide, " km/h")
    #print("capacite : ", capacite, " veh/h")
    #print("concentration critique : ", concentrationCrit, " veh/km")
    print('ecriture des resultats')
    with open('diagrammesfondamentaux.csv','a') as sortie1:
        for point in enveloppeConvexe:
            sortie1.write(key+';'+str(point[0])+';'+str(point[1])+'\n')
    with open('caractersitiques.csv','a') as sortie2:
            sortie2.write(key+';'+str(capacite)+';'+str(vitesseVide)+';'+str(concentrationCrit)+'\n')

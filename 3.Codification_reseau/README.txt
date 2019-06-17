LISEZ-MOI
------------------------------------
Ce dossier contient d'une part :
- un tableau Excel "reseau_FCD.xlsx" avec la description du réseau autoroutier et routier structurant du périmètre d'étude
- les scripts Python permettant de convertir les données sur le réseau en des variables (matrices) lues par les différents programmes/logiciels, notamment MATLAB
- le fichier texte résultant de l'exécution de ces scripts.

D'autre part, il inclut aussi les algorithmes permettant la reconstitution d'une matrice dynamique de demande à partir du réseau codifié et des mesures empiriques de débit et de temps de parcours FCD :
- un fichier Excel "CalculMatriceDynamique_Fratar_petit.xlsx" mettant en œuvre une méthode de Fratar à partir des débits mesurés ou déduits (par une analyse simple, indépendante) aux différents points d'injection/sortie du réseau. Les onglets du fichier Excel concernent le recensement des différents trajets OD, les tronçons FCD empruntés par chacun de ces trajets, les temps de parcourus associés aux tronçons (données FCD) et l'implémentation de la méthode de Fratar.
- un script Python "calage_dynamique.py" qui met en œuvre une méthode de suivi des chemins et de répartition des débits. Les noms de fichiers et valeurs de paramètres (y compris l'ensemble des nœuds d'entrée/sortie du réseau) à modifier pour l'exécution du script figurent en tête de script, dans les espaces annotés. Le script lit le réseau codifié (tableur Excel), calcule l'ensemble des itinéraires possibles, évalue au fil du temps le flux minimal le long de chaque itinéraire (en répartissant le débit mesuré entre les différents itinéraires si l'arc où a lieu la mesure est partagé entre plusieurs itinéraires) et produit un fichier texte avec des matrices directement importables dans MATLAB (par copier-coller).

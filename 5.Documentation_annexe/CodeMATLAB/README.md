Documentation pour le code MATLAB 
-----------------------------------------------------------
Ce dossier documente l'algorithme MATLAB implémenté par Ke HAN et al., tel qu'Explain l'a exploité et adapté dans le cadre de son étude.

EN PRATIQUE
--------------
Les étapes qui suivent présupposent qu'une version d'essai gratuite (30 jours) de MATLAB 
https://fr.mathworks.com/campaigns/products/trials.html
ou bien du logiciel libre Octave 
https://www.gnu.org/software/octave/
a été téléchargée au préalable.

1. Codification du réseau : 
Le script Python "writeNetwork.py" prend en entrée le fichier Excel répertoriant les caractéristiques du réseau (par exemple, "reseau_FCD.xlsx") et génère en sortie un fichier texte (par exemple, "codage_MATLAB.txt") avec les matrices des arcs et nœuds du réseau aux formats demandés par MATLAB. 
Après avoir modifié, au besoin, les paramètres de ce script  et l'avoir exécuté
$ python writeNetwork.py
il suffit de copier-coller les matrices du fichier texte de sortie vers le fichier MATLAB "save_Marseille_net.m"

2. Création de la matrice dynamique de demande :
Selon la méthode retenue (voir la note dédiée à l'obtention d'une matrice dynamique), adapter la feuille de calcul Excel "CalculMatriceDynamique_Fratar.xlsx" (pour la méthode implémentant une matrice Fratar) ou bien exécuter le script Python "calage_dynamique.py" (pour la méthode de suivi des chemins). Ce dernier script produit un fichier texte (par exemple, "codage_MATLAB.txt") avec la liste des chemins et les matrices de taux de départ associés, au format demandé par MATLAB.
Il suffit alors de copier-coller les matrices du fichier texte de sortie vers les fichiers MATLAB "save_Marseille_paths.m" (pour les chemins) et "save_Marseille_dep.m" (pour les taux de départ).

2. Ouvrir le dossier dans lequel ont sont enregistrés les fichiers *.m et *.mat de l'algorithme MATLAB.

3. Exécuter, dans l'ordre,
save_Marseille_net.m
save_Marseille_paths.m
save_Marseille_dep.m
CREATE_NETWORK_PROPERTIES.m
DYNAMIC_NETWORK_LOADING.m

4. Visualiser les résultants en exécutant
OPEN_NETWORK_GUI.m
(Ne fonctionne que sous MATLAB pour l'instant.)

ETUDE DU CODE MATLAB
---------------------------------------
Pour une compréhension approfondie de l'algorithme de Ke HAN et al., le tableur Excel "liste_des_variables.xlsx" détaille les variables et paramètres utilisés dans l'algorithme. 

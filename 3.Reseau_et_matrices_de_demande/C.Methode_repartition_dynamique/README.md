Méthode de répartition dynamique des débits
---------------------------------------------

Cette méthode suit les débits rencontrés par les véhicules partis d'une certaine origine à une certaine heure le long des arcs de l'itinéraire, relève les débits rencontrés et les répartit entre itinéraires empruntant des arcs communs.

Le script Python "calage_dynamique.py" contient à la fois le module de création des itinéraires et le module de création des matrices dynamiques. Pour l’utiliser, il faut l’ouvrir dans un éditeur de texte et
-	modifier les noms des dossiers/fichiers : DossierReseau est le dossier contenant le fichier Excel avec description du réseau, DossierSIREDO est le dossier contenant les fichiers CSV des comptages SIREDO de pleine voie, DossierBretelles est le dossier contenant les fichiers CSV des comptages aux bretelles et DossierFCD est le dossier contenant le fichier CSV avec les temps de parcours FCD (exemple en figure 1)
-	modifier les identifiants des nœuds-origines et nœuds-destination du réseau (lignes 16 et 17)
-	de manière facultative, étiqueter les identifiants de nœuds avec des noms
-	si les données de comptages ne sont pas homogènes dans le temps, introduire les coefficients de redressement appropriés à la ligne 25
-	exécuter le code en tapant dans un terminal la commande $ python calage_dynamique.py

L'exécution du script génère un fichier texte, comme "codage_MATLAB.txt"), dont les éléments peuvent être copiés-collés dans le code MATLAB
du répertoire 4.Code_MATLAB, de la manière suivante :
-	la liste des arcs linkData, à copier-coller dans le fichier MATLAB "save_Marseille_net.m"
-	la liste des nœuds nodeCoordinates, à copier-coller dans le fichier MATLAB "save_Marseille_net.m"
-	la liste des chemins pathList, à copier-coller dans le fichier MATLAB "save_Marseille_paths.m" 
-	les matrices de taux de départ associés pathDepartures, à copier-coller dans "save_Marseille_dep.m" (pour les taux de départ). 

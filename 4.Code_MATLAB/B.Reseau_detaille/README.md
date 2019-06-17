Le réseau modélisé dans ce répertoire est un peu plus fin que le "réseau simplifié" du répertoire A. De plus, à la différence du répertoire A, la matrice de demande dynamique est ici reconstituée à l'aide de la méthode de répartition dynamique des débits, plutôt que la méthode de Fratar. 

UTILISATION
-----------------------------------------
1. Télécharger une version d'essai gratuite (30 jours) de MATLAB sur
https://fr.mathworks.com/campaigns/products/trials.html
ou bien télécharger le logiciel libre Octave 
https://www.gnu.org/software/octave/

2. Ouvrir un des sous-dossiers du présent répertoire (il contient les programmes sous la forme de fichiers *.m et *.mat), selon la situation à simuler.

3. Lancer MATLAB et exécuter, *dans cet ordre*,
- save_Marseille_net.m
- save_Marseille_paths.m
- save_Marseille_dep.m
- CREATE_NETWORK_PROPERTIES.m
- DYNAMIC_NETWORK_LOADING_standalone.m

Ce faisant, des fichiers de données *.mat (réseau, taux de départ, ...) sont automatiquement générés.

4. Visualiser les résultants en exécutant
OPEN_NETWORK_GUI.m
(Ne fonctionne que sous MATLAB pour l'instant.)

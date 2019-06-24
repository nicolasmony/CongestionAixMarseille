LISEZ-MOI
----------------------------
Ce répertoire contient le programme proposé par Ke Han et al. (2019), tel qu'il a été adapté par Explain pour modéliser l'axe A50/A501 du réseau géré par la DIRMed, à titre d'illustration. 

Ainsi, à l'heure actuelle, seuls le tronçon de l'A50 de Marseille vers Aubagne, la bifurcation vers l'A501 et la portion de la RD2 qui longe le premier ont été codifiés. Cette modélisation a été effectuée à deux degrés de finesse :
- un réseau détaillé
- un réseau simplifié, comportant une dizaine de nœuds en moins. (La plupart des tests ont été réalisés sur cette seconde version).

Chaque sous-dossier du présent répertoire contient une situation testée (situation actuelle, demande accrue, etc.), déjà implémentée dans les fichiers "save_***.m" -- les matrices de demande ont déjà été reconstituées dans chaque cas et intégrées au code, pour faciliter la tâche de l'utilisateur.

Le tableur Excel "liste_des_variables.xlsx" répertorie les principaux paramètres et variables utilisés dans le code MATLAB, afin de faciliter sa compréhension.

De plus, des commentaires abondants du code sont disponibles sous forme d'annotations dans les fichiers "*.m" du sous-dossier "A.Reseau_simplifie/Situation_actuelle". (Par souci de compacité, ces annotations ne figurent pas dans les programmes similaires des autres sous-dossiers.)

NB: L'outil de visulation des simulations n'est opérationnel que sous MATLAB (version d'essai gratuite).


UTILISATION
-----------------------------------------
1. Télécharger une version d'essai gratuite (30 jours) de MATLAB sur
https://fr.mathworks.com/campaigns/products/trials.html
ou bien télécharger le logiciel libre Octave 
https://www.gnu.org/software/octave/

2. Ouvrir un des sous-dossiers du présent répertoire (il contient les programmes sous la forme de fichiers *.m et *.mat), selon la situation à simuler.

3. Lancer MATLAB et exécuter, *dans cet ordre*,
save_Marseille_net.m (ou save_Marseille_net2.m selon les cas)
save_Marseille_paths.m
save_Marseille_dep.m
CREATE_NETWORK_PROPERTIES.m
DYNAMIC_NETWORK_LOADING_standalone.m

Ce faisant, des fichiers de données *.mat (réseau, taux de départ, ...) sont automatiquement générés.

4. Visualiser les résultants en exécutant
OPEN_NETWORK_GUI.m
(Ne fonctionne que sous MATLAB pour l'instant.)


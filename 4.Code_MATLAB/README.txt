LISEZ-MOI
----------------------------
Ce dossier contient l'adaptation du programme proposé par Ke Han et al. (2019) au cas du réseau de Marseille.

A terme, le programme contiendra le réseau structurant sur l'ensemble du périmètre d'étude et pourra être exécuté sous Octave
(logiciel sous licence GNU). 
A l'heure actuelle, seul le tronçon de l'A50 de Marseille vers Aubagne, la bifurcation vers l'A501 et la portion de la RD2 qui longe
le premier ont été codifiés. L'outil de visulation n'est opérationnel que sous MATLAB (version d'essai gratuite).


UTILISATION
-----------------------------------------
1. Télécharger une version d'essai gratuite (30 jours) de MATLAB sur
https://fr.mathworks.com/campaigns/products/trials.html
ou bien télécharger le logiciel libre Octave 
https://www.gnu.org/software/octave/

2. Ouvrir le dossier dans lequel ont été téléchargés les fichiers *.m et *.mat

3. Exécuter, dans l'ordre,
save_Marseille_net.m
save_Marseille_paths.m
save_Marseille_dep.m
CREATE_NETWORK_PROPERTIES.m
DYNAMIC_NETWORK_LOADING.m

4. Visualiser les résultants en exécutant
OPEN_NETWORK_GUI.m
(Ne fonctionne que sous MATLAB pour l'instant.)


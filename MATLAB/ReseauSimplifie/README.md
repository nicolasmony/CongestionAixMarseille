 *** Chargement de l'axe A50-A501 dans le sens Aubagne vers Marseille en JOB entre 06h00 et 10h00 ***

UTILISATION
------------
Pour cet exemple, le réseau et les taux de départ ont été pré-chargés dans des fichiers de données MATLAB (¤) (les xxx.mat de ce dossier). L'exécution du code en est donc facilitée :

1. Télécharger l'ensemble des fichiers dans un même dossier

2. Ouvrir *DYNAMIC_NETWORK_LOADING_standalone.m* dans MATLAB (¤¤)

3. Remplacer la ligne 30 du fichier avec le chemin vers le dossier de téléchargement.

4. Exécuter *DYNAMIC_NETWORK_LOADING_standalone.m*

5. Exécuter *OPEN_NETWORK_GUI.m*

Une illustration du chargement de l'axe A50-A501 entre 06h00 et 10h00 en jour ouvrable (lundi, mardi, jeudi) s'affiche alors à l'écran. 

(¤) Une version d'essai gratuite de MATLAB peut être obtenue en suivant le lien https://fr.mathworks.com/campaigns/products/trials.html
(¤¤) Le code original a été modifié par Explain (23/04/2019) pour rectifier ce que nous supposons être une erreur dans le modèle de transfert aux jonctions entre arcs, qui générait une congestion artificiellement élevée dans la version initiale.

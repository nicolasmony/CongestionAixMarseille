LISEZ-MOI
------------------------------------
Ce répertoire contient les données qui nourriront directement le programme de simulation dynamique MATLAB, à savoir :

A) Le réseau modélisé

Les caractéristiques du réseau sont répertoriées dans le tableau Excel "reseau_FCD.xlsx" (longueur des arcs, temps de parcours à vide, capacité, ...), décrivant le réseau autoroutier et le routier structurant du périmètre d'étude (A50/A501). La méthode de constitution de ce réseau modèle est exposée dans la section 4 de la note NT02 (dans le répertoire CongestionAixMarseille/2.Donnees_de_trafic)

Est également présent le script Python "writeNetwork.py" qui permet la transformation de ce tableur Excel en listes d'arcs et de nœuds lisibles par MATLAB.


B) La méthode de Fratar dynamique pour reconstituer une matrice dynamique

Cette méthode part des débits injectés dans le réseau aux différentes entrées et extraites du réseau aux différentes sorties; elle optimise ensuite les flux associés à un ensemble de chemins prédéfinis.


C) La méthode de répartition dynamique des débits

Cette méthode suit les débits rencontrés par les véhicules partis d'une certaine origine à une certaine heure le long des arcs de l'itinéraire, relève les débits rencontrés et les répartit entre itinéraires empruntant des arcs communs.


Les deux méthodes précédentes, B) et C), permettant la reconstitution d'une matrice dynamique de demande (taux de départ) par itinéraire, sont détaillées dans la note NT08_Reconstitution_des_matrices_de_demande.pdf 

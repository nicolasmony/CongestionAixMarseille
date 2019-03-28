## Traitement des SIREDO : obtention du diagramme fondamental

# Principe méthodologique

L'objet de la section est de présenter une manière d'exploiter directement les relevés 6 min des boucles SOL2 installés dans la chaussée pour obtenir les caractéristiques principales ainsi que l'enveloppe concave du nuage de points du diagramme fondamental.
La méthodologie s'inspire du rapport Théorie du trafic et régulation dynamique du CEREMA qui recommande d'obtenir une caractérisation du diagramme fondamental par l'obtention de l'enveloppe des données plutôt que par une régression linéaire.
L'algorithme de recherche d'enveloppe convexe utilisé est celui du parcours de Graham.
La capacité est déterminé comme le débit maximum obtenu avec l'enveloppe. La vitesse à vide est la vitesse la pente maximale de l'enveloppe (obtenue sur une portion significative).

# Utilisation du script

- Placer le script Python et le répertoire contenant les données SIREDO 6min (fichiers .dat par jour dans un répertoire par mois dans un répertoire par année) dans le même répertoire
- Editer les premières lignes du script pour indiquer la liste des années et mois à prendre en compte.
- Exécuter le script avec Python (version utilisée : 3.7)

# Résultats obtenus

Le script produit deux fichiers :
- un fchiers contenants les différents points du diagrammes fondemental (interpolation linéaire entre les points) de chaque point de comptage : diagrammesfondamentaux.csv
- un fichier contenants les principales caractéristiques de la section routière par point de comptage : caracteristiques.csv



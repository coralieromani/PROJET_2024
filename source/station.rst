Recupération coordonnées des stations(bike/Base_des_donnees/station)
====================================================================

Ce module contient deux fonctions principales permettant de récupérer les coordonnées géographiques des stations de vélo à partir de leurs noms et villes, et de traiter un ensemble de données des stations de vélo.

Description des fonctions
-------------------------
**obtenir_coordonnees**

Cette fonction utilise le service de géocodage de l'API Nominatim de **geopy** pour obtenir les coordonnées géographiques (latitude et longitude) d'un lieu donné dans une ville spécifiée en France.

- **Paramètres** 

    - **nom_lieu** (str) : Le nom du lieu dont on souhaite obtenir les coordonnées (par exemple, le nom d'une station).  

    - **ville** (str) : La ville dans laquelle se trouve le lieu.

- **Retour**

    - **(latitude, longitude)** (tuple) : Un tuple contenant la latitude et la longitude du lieu, ou **(None, None)** si l'adresse n'a pas pu être géocodée.

- **Exceptions**

    - Si une erreur se produit lors de l'appel à l'API de géocodage (par exemple, un problème de connexion), un message d'erreur est affiché et la fonction renvoie **(None, None)**.

**traiter_stations**

Cette fonction traite un **DataFrame** contenant des informations sur des stations de vélo, cherche les coordonnées géographiques pour chaque station, puis renvoie une liste de dictionnaires avec ces informations.

- **Paramètres**

    - **dataframe** (**pandas.DataFrame**) : Le **DataFrame** contenant les données des stations. 
    
    Il est supposé que les colonnes **'nom'** et **'commune'** contiennent respectivement le nom de la station et la ville.

- **Retour**

    - **stations_avec_coordonnees** (list) : Une liste de dictionnaires contenant pour chaque station :  

        - **nom** (str) : Le nom de la station.  

        - **latitude** (float) : La latitude de la station.  

        - **longitude** (float) : La longitude de la station.

- **Comportement**

    - Pour chaque ligne du **DataFrame**, la fonction extrait le nom de la station et la ville associée, puis utilise la fonction **obtenir_coordonnees** pour récupérer les coordonnées géographiques.  

    - Si des informations sont manquantes pour une station (nom ou ville), la ligne est ignorée et un message est affiché.  

    - La fonction respecte la limite de fréquence de l'API en introduisant une pause de 1 seconde entre chaque requête.

- **Exemple d'utilisation**

.. code-block:: python

    # Charger les données des stations
    MMM_MMM_Velomagg = pd.read_csv("https://data.montpellier3m.fr/sites/default/files/ressources/MMM_MMM_Velomagg.csv", encoding="utf-8")
    
    # Traiter les stations pour obtenir leurs coordonnées
    stations_coordonnees = traiter_stations(MMM_MMM_Velomagg)

- **Notes supplémentaires**

    - La fonction **obtenir_coordonnees** utilise l'API Nominatim, qui impose une limite de fréquence des requêtes. Un délai de 1 seconde est respecté entre chaque appel pour éviter d'être bloqué.

    - Les stations pour lesquelles le nom ou la ville est manquant sont ignorées, et un message est affiché pour chaque ligne incomplète.

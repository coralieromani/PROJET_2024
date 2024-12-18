import pandas as pd
import plotly.graph_objects as go

# Charger les données
url_fichier = "https://drive.google.com/uc?id=1yJUkkGiobznF50tQaKwbM4a2bfiEVmRy"
Donnees_montpellier = pd.read_csv(url_fichier, sep=';')  # Ajouter le séparateur correct si nécessaire

# Convertir la colonne 'date' en format datetime
Donnees_montpellier['date'] = pd.to_datetime(Donnees_montpellier['date'])

# Regrouper par date et calculer la somme des intensités
flux_global = Donnees_montpellier.groupby('date')['intensity'].sum()


# Ajouter une colonne pour les jour de la semaine
Donnees_montpellier['weekday'] = Donnees_montpellier['date'].dt.dayofweek

# Calculer la moyenne des flux par jour de la semaine
moyenne_par_jour = Donnees_montpellier.groupby('weekday')['intensity'].mean()
jours_semaine = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']

fig = go.Figure()

fig.add_trace(go.Bar(
    x=jours_semaine,
    y=moyenne_par_jour,
    name='Moyenne des flux',
    marker_color='green'
))

# Ajouter des détails au graphique
fig.update_layout(
    title='Flux moyen des vélos par jour de la semaine',
    xaxis_title='Jour de la semaine',
    yaxis_title='Nombre moyen de vélos',
    template='plotly_white',
    height=500
)

# Sauvegarder le graphique
fig.write_html("docs/Diagramme/Diagramme_Semaine_2023.html")

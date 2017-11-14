import folium

# Creates an instance of the Map class
map = folium.Map(location=[38.58,-99.09], zoom_start=6, tiles="Mapbox Bright")

# Add elements or objects to the map - referred to as child
fg = folium.FeatureGroup(name="My Map")

for coordinates in [[38.2, -99.1],[39.2, -97.1]]:
    fg.add_child(folium.Marker(location=coordinates, popup="Hi I am a Marker", icon=folium.Icon(color='green')))


map.add_child(fg)

map.save("map.html")
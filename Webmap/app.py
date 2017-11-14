"""
Webmap 

Author: William
Date: 06/11/2017

https://github.com/williamsoftwarecode/python-projects

This application is a webmap made with Python and Folium, which is a third party library for visualising maps. 
Features include: 
    1. Open Street Map (OSM) basemap
    2. Point markers on top of the basemap
    
Additional Notes:
    1. FeatureGroup can be used to consolidate different attributes together
"""



import folium

# Creates an instance of the Map class
map = folium.Map(location=[38.58,-99.09], zoom_start=6, tiles="Mapbox Bright")

# Add elements or objects to the map - referred to as child
fg = folium.FeatureGroup(name="My Map")

# Add multiple markers based on coordinates from a list
for coordinates in [[38.2, -99.1],[39.2, -97.1]]:
    fg.add_child(folium.Marker(location=coordinates, popup="Hi I am a Marker", icon=folium.Icon(color='green')))


map.add_child(fg)

# Create HTML map
map.save("map.html")
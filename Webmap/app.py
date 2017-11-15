"""
Webmap 

Author: William
Date: 12/11/2017

https://github.com/williamsoftwarecode/python-projects

This application is a webmap made with Python and Folium, which is a third party library for visualising maps. 
Features include: 
    1. Open Street Map (OSM) basemap
    2. Point markers on top of the basemap
    
Additional Notes:
    1. FeatureGroup can be used to consolidate different attributes together
"""



import folium
import pandas

# Read coordinates of volcanoes in Volcanoes_USA.txt
data = pandas.read_csv("Volcanoes_USA.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
name = list(data["NAME"])
elev = list(data["ELEV"])
coordinates = zip(lat, lon, name, elev)

# Function for 
def color_producer(elevation): 
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else: 
        return 'red'

# Creates an instance of the Map class
map = folium.Map(location=[38.58,-99.09], zoom_start=6, tiles="Mapbox Bright")

# Add elements or objects to the map - referred to as child
fgv = folium.FeatureGroup(name="Volcanoes")
fgp = folium.FeatureGroup(name="Population")

# Add multiple markers based on coordinates from a list - plots the locations of volcanoes in the USA
# Different elevations are given a different color 
# Green: 0 - 1000 m 
# Yellow: 1000 - 3000 m
# Red: >= 3000 m
for lt, ln, nm, el in coordinates:
    pp = str(nm)+", "+str(el)+" m"
    fgv.add_child(folium.CircleMarker(location=[lt,ln], popup=folium.Popup(pp, parse_html=True), 
    radius=6, fill='true', color='grey', fill_color=color_producer(el), fill_opacity=0.7))

# Adding a polygon using GeoJson in Folium
# fg.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read()))
fgp.add_child(folium.GeoJson('world.json', style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 
    else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000
    else 'red'
}))


# Adding feature groups to the map with layer control
map.add_child(fgp)
map.add_child(fgv)
map.add_child(folium.LayerControl())

# Create HTML map
map.save("map.html")
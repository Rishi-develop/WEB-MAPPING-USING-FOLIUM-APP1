from turtle import color, fillcolor
import folium
from matplotlib.pyplot import fill
import pandas

file = pandas.read_csv("Volcanoes.txt")
lat=list(file["LAT"])
lon= list(file["LON"])
elev = list(file["ELEV"])
Name = list(file["NAME"])

def color_Producer(Elevat):
    if Elevat < 1000:
        return 'green'
    elif 1000 <= Elevat < 3000:
        return 'blue' 
    else:
        return 'red'

html = """<h4> Valcano Name:
</h4>
<a href = "https://www.google.com/search?q=%%22%s%%22" target="_blank"> %s</a><br>
Height: %s m"""

map = folium.Map(location = [38.58, -99.01],zoom_start = 6, tiles='Stamen Terrain')

fgv = folium.FeatureGroup(name="My Valcanoes")

for i,j,el,name in zip(lat,lon,elev,Name):
    iframe = folium.IFrame(html=html % (name,name,el), width = 200,height =100)
    fgv.add_child(folium.CircleMarker(location=[i,j],radius =6,popup=folium.Popup(iframe),color = "grey", fill_color= color_Producer(el),fill = True ,fill_opacity =0.7))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open('D:\RISHI\project\web mapping app 1\world','r', encoding='utf-8-sig').read(), style_function= lambda a : {'fillColor':'Yellow' if a['properties']['POP2005']< 10000000 
else 'blue' if 10000000 <= a['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map1_html_popup_adavnced.html")
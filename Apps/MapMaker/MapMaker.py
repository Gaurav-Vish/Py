import folium
from geopy.geocoders import Nominatim

nom  = Nominatim(user_agent="G")
n = nom.geocode("3995 23rd St,CA 94114")
#print(n.address)
#print(n.point)
print(n.latitude)
print(n.longitude)

map = folium.Map(location=[n.latitude,n.longitude], zoom_start=10, tiles="OpenStreetMap")
map.save("MapMaker1.html")

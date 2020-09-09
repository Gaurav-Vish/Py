import folium

map = folium.Map(location=[19,73], zoom_start=10)
###zoom_start=1->16 == zoomed out->zoomed in
map.save("Map1.html")

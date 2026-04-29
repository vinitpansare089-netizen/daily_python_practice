import folium

m = folium.Map(location=[28.61,77.23], zoom_start=12)
folium.Marker([28.61,77.23], popup="Location").add_to(m)

m 

import openrouteservice
client = openrouteservice.Client(key="5b3ce3597851110001cf6248729ae0da3c6342289d21452129e44d18")
coordinates = ((77.2090, 28.6139), (75.7873, 26.9124))
route = client.directions(coordinates=coordinates, profile='driving-car')
distance_km = route['features'][0]['properties']['segments'][0]['distance'] / 1000
print(f"Distance from Delhi to Jaipur: {distance_km:.2f} km")

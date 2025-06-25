import openrouteservice

# 🔑 Replace "your-api-key-here" with your real key from openrouteservice.org
client = openrouteservice.Client(key="5b3ce3597851110001cf6248729ae0da3c6342289d21452129e44d18")

# 📍 Coordinates: (longitude, latitude)
# From Delhi to Jaipur
coordinates = ((77.2090, 28.6139), (75.7873, 26.9124))

# 🚗 Get route data
route = client.directions(coordinates=coordinates, profile='driving-car')

# 📏 Extract distance in kilometers
distance_km = route['routes'][0]['summary']['distance'] / 1000

print(f"Distance from Delhi to Jaipur: {distance_km:.2f} km")

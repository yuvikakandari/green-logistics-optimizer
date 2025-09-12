import openrouteservice
import itertools

#function to get coordinates (address or lat,long)
def get_coords(loc):
    # if input form is "lat,long"
    if "," in loc and all(part.strip().replace('.', '', 1).replace('-', '', 1).isdigit() 
                               for part in loc.split(',')):
        lat, lon = map(float, loc.split(','))
        return [lon, lat] 
     #ors takes [long, lat]
    else:
        # Or geocode given location
        result = client.pelias_search(text=loc)
        return result['features'][0]['geometry']['coordinates']

#my api key for ORS
api_key = "5b3ce3597851110001cf6248729ae0da3c6342289d21452129e44d18"
client = openrouteservice.Client(key=api_key)

#taking location inputs from user
start_location = input("Enter your start location (address or latitude,longitude): ")
destination = input("Enter destinations (comma separated): ").split(',')

#convert the string of cities into a list
cleaned_destination = []
for location in destination:
    cleaned_destination.append(location.strip())

#destination(s)
destination = cleaned_destination

# Mapping coordinates of all locations
l_coords = {}
l_coords[start_location] = get_coords(start_location)
for location in destination:
    l_coords[location] = get_coords(location)

#using itertools to create pairs of locations and storing distances
distances = {}
locations = [start_location] + destination

for dest_1, dest_2 in itertools.combinations(locations, 2):
    route = client.directions(
        coordinates=[l_coords[dest_1], l_coords[dest_2]],
        profile='driving-car',
        format='geojson'
    )
    distance_km = route['features'][0]['properties']['segments'][0]['distance'] / 1000
    distances[(dest_1, dest_2)] = distance_km
    distances[(dest_2, dest_1)] = distance_km

#print pairwise distances
print("\nPairwise Distances:")
for pair, dist in distances.items():
    print(f"{pair[0]} -> {pair[1]}: {dist:.2f} km")

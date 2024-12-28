from geopy.geocoders import Nominatim
import webbrowser

def get_coordinates(city_name, area_name):
    geolocator = Nominatim(user_agent="geoapiExercises")
    location_name = f"{area_name}, {city_name}"
    location = geolocator.geocode(location_name)
    
    if location:
        return location.latitude, location.longitude
    else:
        return None, None

def open_google_maps(lat, lng):
    google_maps_url = f"https://www.google.com/maps?q={lat},{lng}"
    webbrowser.open(google_maps_url)

if __name__ == "__main__":
    city_name = input("Enter the city name: ")
    area_name = input(f"Enter a specific area in {city_name}: ")
    
    latitude, longitude = get_coordinates(city_name, area_name)
    
    if latitude and longitude:
        print(f"Coordinates of {area_name}, {city_name}:")
        print(f"Latitude: {latitude}, Longitude: {longitude}")
        open_google_maps(latitude, longitude)
    else:
        print(f"Could not find coordinates for {area_name}, {city_name}.")

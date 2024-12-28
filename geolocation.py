import requests
from geopy.geocoders import Nominatim
import webbrowser

def get_coordinates(place_name):
    # Initialize Nominatim API
    geolocator = Nominatim(user_agent="geoapiExercises")
    
    # Get location
    location = geolocator.geocode(place_name)
    
    # Return latitude and longitude
    if location:
        return location.latitude, location.longitude
    else:
        return None, None

def get_current_location():
    # Fetch the current location based on the user's IP address
    response = requests.get('https://ipinfo.io/json')
    
    if response.status_code == 200:
        data = response.json()
        loc = data['loc'].split(',')
        latitude = float(loc[0])
        longitude = float(loc[1])
        return latitude, longitude
    else:
        return None, None

def open_google_maps(lat, lng):
    google_maps_url = f"https://www.google.com/maps?q={lat},{lng}"
    webbrowser.open(google_maps_url)

if __name__ == "__main__":
    option = input("Enter '1' to enter a place name or '2' to use your current location: ")
    
    if option == '1':
        place_name = input("Enter the place name: ")
        lat, lng = get_coordinates(place_name)
    elif option == '2':
        lat, lng = get_current_location()
    else:
        print("Invalid option.")
        lat, lng = None, None
    
    if lat and lng:
        print(f"Coordinates: Latitude={lat}, Longitude={lng}")
        open_google_maps(lat, lng)
    else:
        print("Could not retrieve the location.")

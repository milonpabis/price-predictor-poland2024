import googlemaps
import os

class GeocodingAPI:
    """
    A class that provides geocoding functionality using the Google Maps Geocoding API.
    
    Attributes:
        gmaps (googlemaps.Client): The Google Maps client object.
    
    Methods:
        get_location(address: str) -> tuple: Retrieves the latitude and longitude coordinates for a given address.
    """


    def __init__(self):
        self.gmaps = googlemaps.Client(key=os.environ["GOOGLE_MAPS_GEOCODING"])


    def get_location(self, address: str) -> tuple:
        """
        Retrieves the latitude and longitude coordinates for a given address.
        
        Params:
            address (str): The address to geocode.
        
        Returns:
            tuple: A tuple containing the latitude and longitude coordinates.
            None: If the address could not be geocoded.
        """

        geocode_result = self.gmaps.geocode(address)
        try:
            location = geocode_result[0]["geometry"]["location"]
            return location["lat"], location["lng"]
        except Exception as e:
            print(e)
            return None
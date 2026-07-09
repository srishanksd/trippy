import requests

class MapsAgent:
    def __init__(self):
        pass
    
    def search(self, place):
        url = f"https://nominatim.openstreetmap.org/search?q={place}&format=json&limit=1"
        headers = {
            "User-Agent": "TripPlanner/1.0"
        }
        response = requests.get(url, headers=headers).json()
        return response
    
    def extract_data(self,data):
        latitude = data[0]['lat']
        longitude = data[0]['lon']
        name = data[0]['name']
        address = data[0]['display_name']
        return {
            "latitude" : latitude,
            "longitude" : longitude,
            "name" : name,
            "address": address,   
        }

# x = MapsAgent()
# data = x.search("jog falls")
# ans = x.extract_data(data)
# print(ans)
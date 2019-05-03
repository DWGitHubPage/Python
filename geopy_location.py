# Python3.7.3

from geopy.geocoders import Nominatim
import pprint as pp

geolocator = Nominatim(user_agent="specify_your_app_name_here")
location = geolocator.geocode("117 Sandusky St, Pittsburgh, PA 15212")

print(location.address)
print((location.latitude, location.longitude))
print("\n")
pp.pprint(location.raw)


# Finding address based on coordinates.
print("\n")

location = geolocator.reverse("40.4481053008913, -80.0022214634394")
print(location.address)
print((location.latitude, location.longitude))
print("\n")
pp.pprint(location.raw)

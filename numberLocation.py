
import phonenumbers
import folium

from PhNumber import number

from phonenumbers import geocoder


Key = "c0040f3a465b4574933c42c731eeefec"
snumber = phonenumbers.parse(number)

YourLocation = geocoder.description_for_number(snumber,"en")
print(YourLocation)

from phonenumbers import carrier

service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider,"en"))

#from opencage.geocoder import OpenCageGeocode

#geocoder = OpenCageGeocode(Key)
#query = str(YourLocation)

#results = geocoder.geocode(query)
#print(results)


#lat = results[0]["geometry"]["lat"]
#lng = results[0]["geometry"]["lng"]

#print(lat,lng)

#myMap = folium,Map(location=[lat,lng],zoom_start = 9)

#folium.Marker([lat,lng],popup = YourLocation(myMap))

#myMap.save("myLocation.html")
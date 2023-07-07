import phonenumbers
from test import number
from phonenumbers import geocoder

ch_nmber = phonenumbers.parse(number, "CH")
print(geocoder.description_for_number(ch_nmber, "en"))

from phonenumbers import carrier
service_number= phonenumbers.parse(number,"RO")
print(carrier.name_for_number(service_number, "en"))



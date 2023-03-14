import phonenumbers
from phonenumbers import geocoder , carrier ,timezone

mobile = input(" Enter Mobile Number with Country Code  :   ")
mobile =phonenumbers.parse(mobile)

print(timezone.time_zones_for_number(mobile))

print(carrier.name_for_number(mobile, "en"))

print(geocoder.description_for_number(mobile,"en"))

print(" Validate Mobile Number : ",phonenumbers.is_valid_number(mobile))

print(" Checking Possiblity of Number : ",phonenumbers.is_possible_number(mobile))
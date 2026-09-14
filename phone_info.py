import phonenumbers
from phonenumbers import geocoder, carrier , timezone

phone_no = input("Enter phone number with country code: ")
phone_number = phonenumbers.parse(phone_no)

time_zones = timezone.time_zones_for_number(phone_number)
carrier_name = carrier.name_for_number(phone_number, "en")
region = geocoder.description_for_number(phone_number, "en")

print("Time Zone: ", time_zones)
print("Carrier: ", carrier_name)
print("Region: ", region)
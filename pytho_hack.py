import phonenumbers
from phonenumbers import geocoder, carrier, timezone

number = "+8801568450889"

# Get the country description
numbers_country = phonenumbers.parse(number, "CH")
country_description = geocoder.description_for_number(numbers_country, "en")
print(f"Country: {country_description}")

# Get the carrier name
numbers_operator = phonenumbers.parse(number, "RO")
operator_name = carrier.name_for_number(numbers_operator, "en")
print(f"Carrier: {operator_name}")

# Get the timezone
numbers_timezone = phonenumbers.parse(number, "GB")
time_zones = timezone.time_zones_for_number(numbers_timezone)
print(f"Time zones: {time_zones}")
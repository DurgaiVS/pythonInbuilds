import phonenumbers
from phonenumbers import geocoder

phn = phonenumbers.parse("+919994536996")
print(geocoder.description_for_valid_number(phn, 'en'))
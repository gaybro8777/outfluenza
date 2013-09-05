from messages.models import Message
from zipcodes.models import Zipcode

def handleZipcode(message):
	print(message)
	if message.prescriberZipcode:
		print("exists 1")
		zipcodes = Zipcode.objects.filter(zipcode__exact = message.prescriberZipcode)
		if len(zipcodes) > 0:
			print("modify 1")
			zipcodes[0].prescriberCases += 1
			zipcodes[0].save()
		else:
			new_zipcode = Zipcode().defaultFields(message.prescriberZipcode)			
			print(new_zipcode)
			new_zipcode.prescriberCases += 1
			new_zipcode.save()

	if message.patientZipcode:
		print("exists 2")
		zipcodes = Zipcode.objects.filter(zipcode__exact = message.patientZipcode)
		if len(zipcodes) > 0:
			print("modify 2")
			zipcodes[0].patientCases += 1
			zipcodes[0].save()
		else:
			print("HERE 2")
			new_zipcode = Zipcode().defaultFields(message.patientZipcode)
			new_zipcode.patientCases += 1
			new_zipcode.save()

	if message.pharmacyZipcode:
		print("exists 3")
		zipcodes = Zipcode.objects.filter(zipcode__exact = message.pharmacyZipcode)
		if len(zipcodes) > 0:
			print("modify 3")
			zipcodes[0].pharmacyCases += 1
			zipcodes[0].save()
		else:
			print("HERE 3")
			new_zipcode = Zipcode().defaultFields(message.pharmacyZipcode)
			new_zipcode.pharmacyCases += 1
			new_zipcode.save()
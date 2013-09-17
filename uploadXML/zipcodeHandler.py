from messages.models import Message
from zipcodes.models import Zipcode
import zipcodes_to_state

def handleZipcode(message):
	if message.prescriberZipcode:
		zipcode = getZipcode(message.prescriberZipcode)	
		zipcode.prescriberCases += 1
		zipcode.save()

	if message.patientZipcode:
		zipcode = getZipcode(message.patientZipcode)	
		zipcode.patientCases += 1
		zipcode.save()

	if message.pharmacyZipcode:
		zipcode = getZipcode(message.pharmacyZipcode)	
		zipcode.pharmacyCases += 1
		zipcode.save()

def getZipcode(zipcode):
	zipcodes = Zipcode.objects.filter(zipcode__exact = zipcode)
	if len(zipcodes) > 0:
		return zipcodes[0]
	else:
		return Zipcode().defaultFields(zipcode, getStateForZipcode(zipcode))

def getStateForZipcode(zipcode):
	temp = zipcode
	while zipcode - temp < 30:
		try:
			state = zipcodes_to_state.zipcodes_to_state[temp]
			return state
		except KeyError:
			temp -= 1
	return 'AA'
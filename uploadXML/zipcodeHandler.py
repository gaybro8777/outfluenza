from message.models import Message
from zipcodes.models import Zipcode
import zipcodes_to_state
import zipcode_to_county

def handleZipcode(message):
	if message.patientZipcode:
		zipcode = getZipcode(message.patientZipcode)	
		if message.patientGender == 'M':
			zipcode.malePatientCases += 1
		else:
			zipcode.femalePatientCases += 1
		zipcode.save()
		return zipcode
	return None

def getZipcode(zipcode):
	zipcodes = Zipcode.objects.filter(zipcode__exact = zipcode)
	if len(zipcodes) > 0:
		return zipcodes[0]
	else:
		return Zipcode().defaultFields(zipcode, getStateForZipcode(zipcode), getCountyForZipcode(zipcode))

def getStateForZipcode(zipcode):
	temp = zipcode
	while zipcode - temp < 30:
		try:
			state = zipcodes_to_state.zipcodes_to_state[temp]
			return state
		except KeyError:
			temp -= 1
	return 'AA'

def getCountyForZipcode(zipcode):
	temp = zipcode
	while zipcode - temp < 30:
		try:
			state = zipcode_to_county.zipcode_to_county[temp]
			return state
		except KeyError:
			temp -= 1
	return 'NA'
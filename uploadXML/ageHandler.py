from age.models import Age
from message.models import Message, DEFAULT_TIME
from zipcodes.models import Zipcode
import datetime

def handleAge(message, zipcode):
	if zipcode and message.patientDob != DEFAULT_TIME:
		patientAge = datetime.datetime.now().year - message.patientDob.year
		ageObjs = Age.objects.filter(age__exact = patientAge, zipcode__exact = zipcode.zipcode)
		ageObj = None
		if len(ageObjs) > 0:
			ageObj = ageObjs[0]
		else:
			ageObj = Age().defaultFields(patientAge)
			ageObj.zipcode = zipcode.zipcode
			ageObj.state = zipcode.state
		ageObj.num_cases += 1
		ageObj.save()
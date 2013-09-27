from age.models import Age
from message.models import Message, DEFAULT_TIME
from zipcodes.models import Zipcode
import datetime

def handleAge(message, zipcode):
	if zipcode and message.patientDob != DEFAULT_TIME:
		patientAge = datetime.datetime.now().year() - message.patientDob.year()
		ageObjs = Age.objects.filter(age__exact = patientAge)
		ageObj = None
		if len(ageObj) > 0:
			ageObj = ageObjs[0]
		else:
			ageObj = Age().defaultFields()
			ageObj.zipcode = zipcode.zipcode
			ageObj.state = zipcode.state
		ageObj.num_cases += 1
		ageObj.save()
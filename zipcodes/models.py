from django.db import models
import zipcodes_to_state

class Zipcode(models.Model):
	zipcode = models.IntegerField(primary_key = True)
	prescriberCases = models.IntegerField()
	patientCases = models.IntegerField()
	pharmacyCases = models.IntegerField()
	state = models.CharField(max_length=2)

	def __str__(self):
		output = 'Zipcode: ' + str(self.zipcode)
		output += ', State: ' + self.state
		output += ', Prescriber Cases: ' + str(self.prescriberCases)
		output += ', Patient Zipcode: ' + str(self.patientCases)
		output += ', Pharmacy Zipcode: ' + str(self.pharmacyCases)
		return output

	def defaultFields(self, zipcode):
		self.zipcode = zipcode
		self.prescriberCases = 0
		self.patientCases = 0
		self.pharmacyCases = 0
		try:
			self.state = zipcodes_to_state.zipcodes_to_state[zipcode]
		except KeyError:
			self.state = 'AK' #TODO: do something smart here.
		return self

class State(models.Model):
	name = models.CharField(max_length = 2, primary_key = True)
	num_cases = models.IntegerField()
	bucket = models.IntegerField()

	def __str__(self):
		return 'State: ' + self.name + ', num_cases: ' + str(self.num_cases)

	def populate(self, name, num_cases, bucket):
		self.name = name
		self.num_cases = num_cases
		self.bucket = bucket
		return self
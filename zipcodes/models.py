from django.db import models

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

	def defaultFields(self, zipcode, state):
		self.zipcode = zipcode
		self.prescriberCases = 0
		self.patientCases = 0
		self.pharmacyCases = 0
		self.state = state
		return self

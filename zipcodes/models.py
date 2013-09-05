from django.db import models

class Zipcode(models.Model):
	zipcode = models.IntegerField(primary_key = True)
	prescriberCases = models.IntegerField()
	patientCases = models.IntegerField()
	pharmacyCases = models.IntegerField()

	def __str__(self):
		output = 'Zipcode: ' + str(self.zipcode)
		output += ', Prescriber Cases: ' + str(self.prescriberCases)
		output += ', Patient Zipcode: ' + str(self.patientCases)
		output += ', Pharmacy Zipcode: ' + str(self.pharmacyCases)
		return output

	def defaultFields(self, zipcode):
		self.zipcode = zipcode
		self.prescriberCases = 0
		self.patientCases = 0
		self.pharmacyCases = 0
		return self
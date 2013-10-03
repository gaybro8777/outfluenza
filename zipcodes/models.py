from django.db import models

class Zipcode(models.Model):
	zipcode = models.IntegerField(primary_key = True)
	county = models.CharField(max_length=100)
	malePatientCases = models.IntegerField()
	femalePatientCases = models.IntegerField()
	state = models.CharField(max_length=2)

	def __str__(self):
		output = 'Zipcode: ' + str(self.zipcode)
		output += ', State: ' + self.state
		output += ', County: ' + str(self.county)
		output += ', Male Patient Cases: ' + str(self.malePatientCases)
		output += ', Female Patient Cases: ' + str(self.femalePatientCases)
		return output

	def defaultFields(self, zipcode, state, county):
		self.zipcode = zipcode
		self.county = county
		self.malePatientCases = 0
		self.femalePatientCases = 0
		self.state = state
		return self

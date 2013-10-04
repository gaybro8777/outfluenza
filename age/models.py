from django.db import models

class Age(models.Model):
	age = models.IntegerField()
	num_cases = models.IntegerField()
	zipcode = models.IntegerField()
	state = models.CharField(max_length = 2)

	def defaultFields(self, age):
		self.age = age
		self.num_cases = 0
		self.zipcode = 0
		self.state = 'AA'
		return self
from django.db import models

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

class StateStatistic(models.Model):
	name = models.CharField(max_length = 2, primary_key = True)

	def populate(self, name):
		self.name = name
		return self

class USTimeGraphJson(models.Model):
	date = models.DateField()
	num = models.IntegerField()

	def __str__(self):
		return 'data: ' + str(self.name) + ', num: ' + str(self.num)

	def populate(self, date, num):
		self.date = date
		self.num = num
		return self



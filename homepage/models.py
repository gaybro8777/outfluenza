from django.db import models

class State(models.Model):
	name = models.CharField(max_length = 2, primary_key = True)
	num_male_cases = models.IntegerField()
	num_female_cases = models.IntegerField()
	bucket = models.IntegerField()

	def __str__(self):
		return 'State: ' + self.name + ', num_cases: ' + str(self.num_male_cases + self.num_female_cases)

	def populate(self, name, num_male_cases, num_female_cases, bucket):
		self.name = name
		self.num_male_cases = num_male_cases
		self.num_female_cases = num_female_cases
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
		return 'data: ' + str(self.date) + ', num: ' + str(self.num)

	def populate(self, date, num):
		self.date = date
		self.num = num
		return self

class County(models.Model):
	name = models.CharField(max_length = 100, primary_key = True)
	num_male_cases = models.IntegerField()
	num_female_cases = models.IntegerField()
	bucket = models.IntegerField()

	def __str__(self):
		return 'County: ' + self.name + ', num_cases: ' + str(self.num_male_cases + self.num_female_cases)

	def populate(self, name, num_male_cases, num_female_cases, bucket):
		self.name = name
		self.num_male_cases = num_male_cases
		self.num_female_cases = num_female_cases
		self.bucket = bucket
		return self


class Gender(models.Model):
	state = models.CharField(max_length=2, primary_key=True)
	male = models.IntegerField()
	female = models.IntegerField()

	def __str__(self):
		return 'male: ' + str(self.male) + ', female: ' + str(self.female)

	def populate(self, state):
		self.state = state
		self.male = 0
		self.female = 0
		return self

class DisplayAge(models.Model):
	age = models.IntegerField(primary_key=True)
	num_cases = models.IntegerField()

	def __str__(self):
		return 'age: ' + str(self.age) + ', num: ' + str(self.num_cases)

	def populate(self, age, num_cases):
		self.age = age
		self.num_cases = num_cases
		return self
		
class TopMetrics(models.Model):
	worstZipcode = models.IntegerField()
	numRecentCases = models.IntegerField()
	percentIncrease = models.IntegerField()

	def populate(self, worstZipcode, numRecentCases, percentIncrease):
		self.worstZipcode = worstZipcode
		self.numRecentCases = numRecentCases
		self.percentIncrease = percentIncrease

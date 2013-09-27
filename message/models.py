from django.db import models
import datetime

DEFAULT_TIME = datetime.date(1000, 1, 1)

class Message(models.Model):
	# message ID
	messageID = models.CharField(max_length = 200, primary_key = True)
	
	# medication fields
	writtenDate = models.DateField()
	productCode = models.CharField(max_length = 200)
		
	# patient fields
	patientGender = models.CharField(max_length = 1)
	patientDob = models.DateField()

	#Geographic Information
	zipcode = models.IntegerField()
	state = models.CharField(max_length = 2)

	def __str__(self):
		output = 'messageID: ' + self.messageID + '\n'
		output += 'writtenDate: ' + str(self.writtenDate) + '\n'
		output += 'productCode: ' + self.productCode + '\n'
		output += 'patientGender: ' + self.patientGender + '\n'
		output += 'patientDob: ' + str(self.patientDob) + '\n'
		output += 'zipcode: ' + str(self.zipcode) + '\n'
		output += 'state: ' + self.state + '\n'
		return output

	def defaultFields(self):
		self.messageID = ""
		self.writtenDate = DEFAULT_TIME
		self.productCode = ""
		self.patientGender = "M"
		self.patientDob = DEFAULT_TIME
		self.zipcode = 0
		self.state = 'AA'
		return self
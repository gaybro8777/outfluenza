from django.db import models
import datetime

class Message(models.Model):
	# message ID
	messageID = models.CharField(max_length = 200, primary_key = True)
	
	# medication fields
	writtenDate = models.DateField()
	productCode = models.CharField(max_length = 200)
	refillsQuantity = models.IntegerField()
		
	# patient fields
	patientZipcode = models.IntegerField()
	patientGender = models.CharField(max_length = 1)
	patientDob = models.DateField()

	# prescriber fields
	prescriberLastName = models.CharField(max_length = 75)
	prescriberZipcode = models.IntegerField()

	# pharmacy fields
	pharmacyZipcode = models.IntegerField()

	def __str__(self):
		output = 'messageID: ' + self.messageID + '\n'
		output += 'writtenDate: ' + str(self.writtenDate) + '\n'
		output += 'productCode: ' + self.productCode + '\n'
		output += 'refillsQuantity: ' + str(self.refillsQuantity) + '\n'
		output += 'patientZipcode: ' + str(self.patientZipcode) + '\n'
		output += 'patientGender: ' + self.patientGender + '\n'
		output += 'patientDob: ' + str(self.patientDob) + '\n'
		output += 'prescriberLastName: ' + str(self.prescriberLastName) + '\n'
		output += 'prescriberZipcode: ' + str(self.prescriberZipcode) + '\n'
		output += 'pharmacyZipcode: ' + str(self.pharmacyZipcode) + '\n'
		return output

	def defaultFields(self):
		self.messageID = ""
		self.writtenDate = datetime.datetime.now()
		self.productCode = ""
		self.refillsQuantity = 0
		self.patientZipcode = 0
		self.patientGender = "M"
		self.patientDob = datetime.datetime.now()
		self.prescriberLastName = ""
		self.prescriberZipcode = 0
		self.pharmacyZipcode = 0
		return self
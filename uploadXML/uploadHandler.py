from messages.models import Message
from zipcodeHandler import handleZipcode, getStateForZipcode
import xml.etree.cElementTree as etree
from xml.etree.cElementTree import ParseError as ParseError
import datetime
import time

TAG_PREFIX = '{http://www.surescripts.com/messaging}'

def handleUpload(file):
	i = 0
	for line in file:
		try:
			xmlObj = etree.fromstring(line)
			message = createMessage(xmlObj)
			message.save()
			handleZipcode(message)
		except ParseError as inst:
			print(i)
			pass
		i += 1

def createMessage(root):
	message = Message().defaultFields()
	# Handle messageID here
	for messageID in root.iter(TAG_PREFIX + 'MessageID'):
		message.messageID = messageID.text
	# Handle Prescriber here
	for prescriber in root.iter(TAG_PREFIX + 'Prescriber'):
		handlePrescriber(message, prescriber)
	# Handle Patient here
	for patient in root.iter(TAG_PREFIX + 'Patient'):
		handlePatient(message, patient)
	# Handle Medication here
	for medication in root.iter(TAG_PREFIX + 'MedicationPrescribed'):
		handleMedication(message, medication)
	# Handle Pharmacy here
	for pharmacy in root.iter(TAG_PREFIX + 'Pharmacy'):
		handlePharmacy(message, pharmacy)
	handleGeographicData(message)
	return message

def handleGeographicData(message):
	if message.patientZipcode:
		message.zipcode = message.patientZipcode
	elif message.prescriberZipcode:
		message.zipcode = message.prescriberZipcode
	else:
		message.zipcode = message.pharmacyZipcode
	message.state = getStateForZipcode(message.zipcode)

def stringToDatetime(timeString, timeFormat):
	return datetime.datetime.fromtimestamp(time.mktime(time.strptime(timeString, timeFormat)))

def handlePrescriber(message, prescriber):
	for lastName in prescriber.iter(TAG_PREFIX + 'LastName'):
		message.prescriberLastName = lastName.text
	for zipcode in prescriber.iter(TAG_PREFIX + 'ZipCode'):
		message.prescriberZipcode = int(zipcode.text)

def handlePatient(message, patient):
	for dateOfBirth in patient.iter(TAG_PREFIX + 'DateOfBirth'):
		message.patientDob = stringToDatetime(dateOfBirth.text, "%Y%m%d")
	for gender in patient.iter(TAG_PREFIX + 'Gender'):
		message.patientGender = gender.text
	for zipcode in patient.iter(TAG_PREFIX + 'ZipCode'):
		message.patientZipcode = int(zipcode.text)

def handleMedication(message, medication):
	for productCode in medication.iter(TAG_PREFIX + 'ProductCode'):
		message.productCode = productCode.text
	for date in medication.iter(TAG_PREFIX + 'WrittenDate'):
		message.writtenDate = stringToDatetime(date.text, "%Y%m%d")
		#message.writtenDate = message.writtenDate.replace(day = 1)
	for refills in medication.iter(TAG_PREFIX + 'Refills'):
		for quantity in refills.iter(TAG_PREFIX + 'Quantity'):
			message.refillsQuantity = int(quantity.text)

def handlePharmacy(message, pharmacy):
	for zipcode in pharmacy.iter(TAG_PREFIX + 'ZipCode'):
		message.pharmacyZipcode = int(zipcode.text)
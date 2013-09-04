from messages.models import Message
import xml.etree.cElementTree as etree
import datetime
import time

TAG_PREFIX = '{http://www.surescripts.com/messaging}'

def handleUpload(file):
	for line in file:
		try:
			xmlObj = etree.fromstring(line)
			message = createMessage(xmlObj)
			message.save()
		except:
			pass

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
	return message

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
	for refills in medication.iter(TAG_PREFIX + 'Refills'):
		for quantity in refills.iter(TAG_PREFIX + 'Quantity'):
			message.refillsQuantity = int(quantity.text)

def handlePharmacy(message, pharmacy):
	for zipcode in pharmacy.iter(TAG_PREFIX + 'ZipCode'):
		message.pharmacyZipcode = int(zipcode.text)
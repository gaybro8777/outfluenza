from message.models import Message
from django.db.models import Sum, Count

def createTrainingData():
	messages = Message.objects.values('zipcode', 'writtenDate').annotate(num_zip=Count('zipcode'),num_date=Count('writtenDate'))
	f = open('test.csv', 'w')
	for message in messages:
		output = createRow(message)
		f.write(output+'\n')


def createRow(message):
	output = str(message['num_zip'] + message['num_date']) + ','
	output += str(message['zipcode']) + ','
	output += str(message['writtenDate'].year) + ','
	output += str(message['writtenDate'].month) + ','
	output += str(message['writtenDate'].day)
	return output

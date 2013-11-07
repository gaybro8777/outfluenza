from message.models import Message
from django.db.models import Sum, Count
import datetime


from numpy import *#arange,array,ones#,random,linalg
from pylab import plot,show
from scipy import stats

from numpy import *
import pylab

import random


BASE_DATE = datetime.datetime(2013, 1, 1)

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


def test():
	xi = arange(0,9)
	A = array([ xi, ones(9)])
	# linearly generated sequence
	y = [19, 20, 20.5, 21.5, 22, 23, 23, 25.5, 24]

	slope, intercept, r_value, p_value, std_err = stats.linregress(xi,y)

	print 'r value', r_value
	print 'p_value', p_value
	print 'standard deviation', std_err

	line = slope*xi+intercept
	plot(xi,line,'r-',xi,y,'o')
	show()

def polyTest():
	state = 'NY'
	messages = Message.objects.filter( writtenDate__gt=BASE_DATE).values('writtenDate').annotate(num = Count('writtenDate')).order_by('writtenDate')
	x = [convertToInt(m['writtenDate']) for m in messages]
	y = [m['num'] for m in messages]

	z5 = polyfit(x, y, 4)
	p5 = poly1d(z5)

	xx = linspace(0, 1000, 100)
	pylab.plot(x, y, 'o', x, getY(z5, x),'-g', x, p5(x),'-b')
	#pylab.legend(['data to fit', '4th degree poly', '5th degree poly'])
	#pylab.axis([18,30,7,30])
	pylab.show()

def convertToInt(date):
	return (date-datetime.date(2013, 1, 1)).total_seconds() / (60*60*24)

def getY(theta, x_list):
	return [theta[0] * x * x * x * x + 
		theta[1] * x * x * x + 
		theta[2] * x * x + 
		theta[3] * x + 
		theta[4] for x in x_list]

def getPredictions(state):
	if state == 'US':
		messages = Message.objects.filter(writtenDate__gt=BASE_DATE).values('writtenDate').annotate(num = Count('writtenDate')).order_by('writtenDate')
	else:
		messages = Message.objects.filter(state__exact=state, writtenDate__gt=BASE_DATE).values('writtenDate').annotate(num = Count('writtenDate')).order_by('writtenDate')
	x = [convertToInt(m['writtenDate']) for m in messages]
	y = [m['num'] for m in messages]
	z5 = polyfit(x, y, 4);
	return z5

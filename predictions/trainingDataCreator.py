from message.models import Message
from django.db.models import Sum, Count


from numpy import *#arange,array,ones#,random,linalg
from pylab import plot,show
from scipy import stats

from numpy import *
import pylab

import random

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
	print  'p_value', p_value
	print 'standard deviation', std_err

	line = slope*xi+intercept
	plot(xi,line,'r-',xi,y,'o')
	show()

def polyTest():
	x = [19, 20, 20.5, 21.5, 22, 23, 23.8, 25.5, 29]
	y = [20, 20.5, 21.5, 22, 23, 23, 25.5, 24, 8]

	# fit the data with a 4th degree polynomial
	z4 = polyfit(x, y, 4) 
	p4 = poly1d(z4) # construct the polynomial 

	z5 = polyfit(x, y, 5)
	p5 = poly1d(z5)

	xx = linspace(0, 30, 100)
	pylab.plot(x, y, 'o', xx, p4(xx),'-g', xx, p5(xx),'-b')
	pylab.legend(['data to fit', '4th degree poly', '5th degree poly'])
	pylab.axis([18,30,7,30])
	pylab.show()


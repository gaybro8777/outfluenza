from django.db import models

class Prediction(models.Model):
	state = models.CharField(max_length = 2, primary_key = True)
	theta0 = models.IntegerField()
	theta1 = models.IntegerField()
	theta2 = models.IntegerField()
	theta3 = models.IntegerField()
	theta4 = models.IntegerField()

	def populate(self, state, theta):
		self.state = state
		self.theta0 = theta[0]
		self.theta1 = theta[1]
		self.theta2 = theta[2]
		self.theta3 = theta[3]
		self.theta4 = theta[4]
		return self
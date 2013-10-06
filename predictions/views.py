from django.http import HttpResponse
from predictions.trainingDataCreator import createTrainingData

def CreatePredictions(request):
	createTrainingData()
	return HttpResponse('training data created')
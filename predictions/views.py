from django.http import HttpResponse
from predictions.trainingDataCreator import createTrainingData, getPredictions
from predictions.models import Prediction
from django.core import serializers

def CreatePredictions(request):
	createTrainingData()
	return HttpResponse('training data created')

def GetPredictions(request, state):
	p = getPredictions(state)
	predictions = [Prediction().populate(state, p)]
	return HttpResponse(serializers.serialize("json", predictions, ensure_ascii=False))
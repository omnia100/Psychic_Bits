from django.shortcuts import render
from .models import prediction
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . serializers import predictionSerializer

# Create your views here.




@api_view(['GET'])
def showPrediction(request,pk):
	try:
		predict = prediction.objects.get(pk=pk)
	except predict.DoesNotExist:
		return HttpResponseNotFound('<h1>no such ID</h1>')

	if request.method == 'GET':
		serializer = predictionSerializer(predict)
		return Response(serializer.data)





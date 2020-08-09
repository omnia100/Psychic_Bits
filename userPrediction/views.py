from django.shortcuts import render
from .models import prediction
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . serializers import predictionSerializer
from . models import prediction
from PsychicBits.models import Match
from users.models import Profile
from django.contrib.auth.decorators import login_required

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









@login_required(login_url='psychicbits/mainhome.html')
def vote(request,userID,matchID,voting):
	
	match=Match.objects.get(pk=matchID)
	newVote=prediction.objects.create(matchID=match ,vote=voting)
	
	#get messag vot is done 
	#you have to log in

	return HttpResponse('')


def calculateScore(request, matchID, result):
	match=Match.objects.get(pk=matchID)

	truePredictions=prediction.objects.filter(matchID__id=matchID).filter(vote=result)#return queryset of matchID res filtered prediction 

	#print(truePredictions)
	

	print(truePredictions)
	if not truePredictions:
		return HttpResponse('<h1>No true prediction</h1>')

	
	for predictionObj in truePredictions: 
		predictor=Profile.objects.get(pk=predictionObj.userID)
		predictor.score+=1
		predictor.save()
	return HttpResponse('score increased')
	
	


		
"""
		

"""
	

	













from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from . models import matchData
from . serializers import matchDataSerializer
from rest_framework.views import exception_handler
import json
import joblib
import pandas as pd




"""
@api_view(['GET'])
def matchList(request, pk):
    try:
        match = matchData.objects.get(pk=pk)
    except match.DoesNotExist:
        return HttpResponseNotFound('<h1>no such ID</h1>')

    if request.method == 'GET':
        serializer = matchDataSerializer(match)
        return Response(serializer.data)
"""

def appendFeatures(jsonObj):
	arr=[]
	arr.append(jsonObj[0]['AttackRateH'])
	arr.append(jsonObj[0]['AttackRateA'])

	arr.append(jsonObj[0]['DefenceRateH'])
	arr.append(jsonObj[0]['DefenceRateA'])

	arr.append(jsonObj[0]['DGH'])
	arr.append(jsonObj[0]['DGA'])

	arr.append(jsonObj[0]['HomeRank'])
	arr.append(jsonObj[0]['AwayRank'])

	arr.append(jsonObj[0]['AvgHST'])
	arr.append(jsonObj[0]['AvgAST'])

	arr.append(jsonObj[0]['AvgHF'])
	arr.append(jsonObj[0]['AvgAF'])

	arr.append(jsonObj[0]['AvgHC'])
	arr.append(jsonObj[0]['AvgAC'])

	arr.append(jsonObj[0]['AvgHR'])
	arr.append(jsonObj[0]['AvgAR'])

	arr.append(jsonObj[0]['AvgHY'])
	arr.append(jsonObj[0]['AvgAY'])

	return arr



@api_view(['GET'])
def predictMatch(request,HomeTeam,AwayTeam):
	match=matchData.objects.filter(HomeTeam__exact=HomeTeam).filter(AwayTeam__exact=AwayTeam)
	serializer = matchDataSerializer(match,many=True)
	jsonObj=serializer.data
	features=appendFeatures(jsonObj)

	filePath='mlModel/finalize.pkl'
	try:
		classifier=joblib.load(filePath)
		prediction = classifier.predict([features])[0]
		percentage=classifier.predict_proba([features])[0]

		if prediction == 1:
			predVal='w'

		elif prediction == 0:
			predVal='d'

		if prediction == -1:
			predVal='l'


		percentageList=[]
		for i in (percentage):
			p=str(i)
			percentageList.append(p)
			percentageList.append(',')
		del percentageList[-1]

		data_details = {'res' : predVal, 'lose' : percentageList[0], 'draw' : percentageList[2], 'win': percentageList[4]}
		return HttpResponse(json.dumps(data_details))

		#return HttpResponse(percentageList)

	except ValueError as e:
		return Response(e.args[0], status.HTTP_400_BAD_REQUEST)



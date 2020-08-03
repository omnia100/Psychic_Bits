from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . models import matchData
from . serializers import matchDataSerializer





@api_view(['GET'])
def matchList(request, pk):
    try:
        match = matchData.objects.get(pk=pk)
    except match.DoesNotExist:
        return HttpResponseNotFound('<h1>no such ID</h1>')

    if request.method == 'GET':
        serializer = matchDataSerializer(match)
        return Response(serializer.data)



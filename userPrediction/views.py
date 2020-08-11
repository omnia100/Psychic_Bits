from django.shortcuts import render, get_object_or_404, redirect
from pyexpat.errors import messages

from .models import prediction
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import predictionSerializer
from .models import prediction
from PsychicBits.models import Match
from users.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def showPrediction(prof):
    predict = prediction.objects.filter(userID=prof)
    return predict



@login_required(login_url='psychicbits/mainhome.html')
def vote(request, matchID):
    if request.method == 'POST':
        vote = request.POST['browser']

        match = Match.objects.get(pk=matchID)

        username = request.user.username
        user = get_object_or_404(User, username=username)
        profileObj = get_object_or_404(Profile, user=user)

        old = prediction.objects.filter(matchID=match, userID=profileObj)
        if old:
            old.delete()

        newVote = prediction(userID=profileObj, matchID=match, vote=vote)
        newVote.save()

    return redirect('/psychicbits/mainhome')



def calculateScore(match, result):
    truePredictions = prediction.objects.filter(matchID=match, vote=result)

    if  truePredictions:
        for predictionObj in truePredictions:
            predictor = User.objects.get(pk=predictionObj.userID)
            predictor.profile.score += 1
            predictor.save()

    return HttpResponse('score increased')




def topTen():
    scoreList = Profile.objects.all().order_by('-score')[:10]
    names = []
    scores = []
    for user in scoreList:
        names.append(user.user)
        scores.append(user.score)
    return names, scores

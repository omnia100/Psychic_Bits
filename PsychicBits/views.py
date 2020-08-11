from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from PsychicBits.models import Match
from django.shortcuts import render
from API.views import predict_Match, predictMatchPP
from userPrediction.views import topTen


def index(request):
    matches_list = Match.objects.all()
    context = {'matches_list': matches_list}
    return render(request, 'psychicbits/home.html', context)


def match(request, match_id):
    match = Match.objects.get(id=match_id)
    pred = predictMatchPP(match.HT, match.AT)
    context = {'match': match,
               'pred':pred}
    return render(request, 'psychicbits/match.html', context)


def mainhome(request):
    names,scores = topTen()
    context = {'names':names,
               'scores':scores}
    return render(request, 'psychicbits/mainhome.html',context)


def vote(request):
    m = Match.objects.filter(FTR= "").filter(pred__isnull=False)[0]
    context={'nextmatch':m}
    return render(request, 'psychicbits/vote.html',context)



def profile(request, user_id):
    # user = User.objects.get(pk=user_id)
    # context = {'user': user}
    # return render(request, 'psychicbits/userProfile.html', context)
    return None

def home(request):
    return render(request, 'psychicbits/mainhome.html')
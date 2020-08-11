from django.http import HttpResponse
from PsychicBits.models import Match
from django.shortcuts import render


def index(request):
    matches_list = Match.objects.all()
    context = {'matches_list': matches_list}
    return render(request, 'psychicbits/home.html', context)


def match(request, match_id):
    match = Match.objects.get(id=match_id)
    context = {'match': match}
    return render(request, 'psychicbits/match.html', context)


def mainhome(request):
    return render(request, 'psychicbits/mainhome.html')

def vote(request):
    return render(request, 'psychicbits/vote.html')



def profile(request, user_id):
    # user = User.objects.get(pk=user_id)
    # context = {'user': user}
    # return render(request, 'psychicbits/userProfile.html', context)
    return None
def home(request):
    
    return render(request, 'psychicbits/mainhome.html')
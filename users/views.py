from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from userPrediction.views import showPrediction
from .models import Profile
from .models import User
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


#  login() saves the user’s ID in the session, using Django’s session framework.

# POST only --> '/users/register/'
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            profile = Profile(user=user)
            profile.save()
            messages.success(request, 'Your account has been created!')
            return HttpResponseRedirect(f'/users/{user.username}/')
        else:
            print("Invalid username or password.")
            messages.error(request, "Invalid username or password.")
    else:
        raise Http404


# 'users/logout/'
def log_out(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect('/psychicbits/mainhome')


# POST only: --> /users/login/
def log_in(request):
    # if request.user.is_authenticated():  # if user is already logged in
    #    return HttpResponseRedirect('/psychicbits/mainhome')

    if request.method == 'POST':
        # form = AuthenticationForm(request,request.POST)
        # if form.is_valid():
        form = request.POST
        username = form['username']
        password = form['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.info(request, f"You are now logged in as {username}")
            return redirect('/psychicbits/mainhome')
        else:
            messages.error(request, "Invalid username or password.")
    # else:
    #     messages.error(request, "Invalid username or password.")
    else:
        raise Http404


def profile(request, user_name):
    user = get_object_or_404(User, username=user_name)
    profile = get_object_or_404(Profile, user=user)
    history = showPrediction(profile)
    context = {'profile': profile,
               'history': history}
    return render(request, 'users/profile.html', context)

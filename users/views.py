from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Profile
from .models import User
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import NewUserForm


#  login() saves the user’s ID in the session, using Django’s session framework.


def register(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = Profile(user=user)
            profile.save()
            login(request, profile.user)
            return HttpResponseRedirect('/psychicbits/')
    else:
        form = NewUserForm()

    return render(request, 'users/register.html', {'form': form})


def profile(request, user_name):
    user = get_object_or_404(User, username=user_name)
    profile = get_object_or_404(Profile, user=user)
    context = {'profile': profile}
    return render(request, 'users/profile.html', context)


def logout(request):
    logout(request)
    return redirect('/psychicbits/')


def log_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/psychicbits/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request,
                  template_name="users/login.html",
                  context={"form": form})


# @login_required
# def vote(request):
#
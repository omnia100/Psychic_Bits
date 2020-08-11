from django.urls import path
from . import views

urlpatterns = [
    path('results', views.index, name='index'),
    path('match<int:match_id>/', views.match, name='match page'),
    path('mainhome', views.mainhome, name='mainhome'),
    path('vote', views.vote, name='vote'),
    # psychicbits/vote
]

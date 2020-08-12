from django.urls import path
from . import views
#from PsychicBits.views import match

urlpatterns = [ 
 #path('match/<int:pk>', views.matchList),
 path('prediction/<int:pk>', views.showPrediction, name='prediction'),
 path('uvote/<int:matchID>', views.vote, name='vote'),
 path('score/<int:matchID>/<str:result>/', views.calculateScore, name='score'),
 path('topTen/', views.topTen, name='topTen'),

]

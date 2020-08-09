from django.urls import path
from . import views
#from PsychicBits.views import match

urlpatterns = [ 
 #path('match/<int:pk>', views.matchList),
 path('prediction/<int:pk>', views.showPrediction),
 path('vote/<int:userID>/<int:matchID>/<str:voting>/', views.vote),
 path('score/<int:matchID>/<str:result>/', views.calculateScore),

]

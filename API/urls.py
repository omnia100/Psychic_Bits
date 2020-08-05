from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [ 
 #path('match/<int:pk>', views.matchList),
 path('match/<HomeTeam>/<AwayTeam>/', views.searchMatch),
]






from django.urls import path
from . import views

urlpatterns = [ 
 #path('match/<int:pk>', views.matchList),
 path('prediction/<int:pk>', views.showPrediction),
]

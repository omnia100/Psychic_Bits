from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('match<int:match_id>/',views.match, name='match page'),
    path('user/<int:user_id>/', views.profile, name='profile'),
]
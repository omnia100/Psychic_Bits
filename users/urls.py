from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('login/', views.log_in, name='login'),
    path('<user_name>/', views.profile, name='profile'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add+anime/', views.add_anime, name='add_ame'),
    # Add more paths here
]
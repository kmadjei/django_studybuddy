from django.urls import path

# importing views.py from current directory
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # dynamic routing -> room/<str:pk> ??
    path('room/<str:pk>', views.room, name='room'),

    path('create-room/', views.createRoom, name='create-room')
]
from django.urls import path

# importing views.py from current directory
from . import views

urlpatterns = [
    path('login/', views.loginPage, name='login'),


    path('', views.home, name='home'),
    # dynamic routing -> room/<str:pk> ??
    path('room/<str:pk>', views.room, name='room'),

    path('create-room/', views.createRoom, name='create-room'),
    path('update-room/<str:pk>', views.updateRoom, name='update-room'),
    path('delete-room/<str:pk>', views.deleteRoom, name='delete-room'),
]
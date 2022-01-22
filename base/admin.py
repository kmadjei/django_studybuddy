from django.contrib import admin

# Register your models here.

# acessing the classes from manage.py in current dir
from .models import Room, Topic, Message

# To view created models in django admin panel 
admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)
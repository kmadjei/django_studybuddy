from django.forms import ModelForm
from .models import Room

class RoomForm(ModelForm):
    class Meta: # ??
        model = Room
        fields = '__all__' # creates form with the attributes of the Room model
        exclude = ['host', 'participants']
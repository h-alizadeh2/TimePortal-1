# import form class from django
from django import forms
from .models import Time_Traveler

# create a ModelForm
class Create_Time_traveler(forms.ModelForm):
    class Meta:
        model = Time_Traveler
        fields = "__all__"

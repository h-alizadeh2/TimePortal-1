# import form class from django
from django import forms
from django.shortcuts import get_object_or_404, redirect, render
from .models import Time_Traveler

# create a ModelForm
class Create_Time_traveler(forms.ModelForm):
    class Meta:
        model = Time_Traveler
        fields = "__all__"

def TravelerUpdate(request,pk):
    traveler = get_object_or_404(Time_Traveler , id=pk)

    if request.method == 'POST':

        form = Create_Time_traveler(request.POST,instance=traveler)
        if form.is_valid ():
            form.save()
            return redirect ('form')
    else:
        form = Create_Time_traveler(instance=traveler) 
    
    return render(request, 'update.html', {'form':form})       
from django.shortcuts import render
from .forms import Create_Time_traveler

# Create your views here.
def show(request):
    return render(request, 'index.html')



def home_view(request):
	context ={}

	# create object of form
	form = Create_Time_traveler(request.POST or None, request.FILES or None)
	
	# check if form data is valid
	if form.is_valid():
		# save the form data to model
		form.save()

	context['form']= form
	return render(request, "index.html", context)

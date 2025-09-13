from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Patient, ScalingProphy, Pictures
from .forms import PatientForm, PictureForm, ScalingProphyForm
from django.db import transaction

# Create your views here.
def PatientsBasicRecord(request):
    if request.method == "POST":
        patient_form = PatientForm(request.POST)
        pictures_form = PictureForm(request.POST)
        scalingprophy_form = ScalingProphyForm(request.POST)
        if patient_form.is_valid():
            patient_form.save()
        if pictures_form.is_valid():
            pictures_form.save()
        if scalingprophy_form.is_valid():
            scalingprophy_form.save()
        return redirect('success')
    else:
        patient_form = PatientForm()
        pictures_form = PictureForm()
        scalingprophy_form = ScalingProphyForm()
    context = {
        'patient_form' : patient_form, 
        'pictures_form' : pictures_form,
        'scalingprophy_form':scalingprophy_form,
    }
    
    return render(request, 'treatmentplan.html', context)

def SuccessView(request):
    return HttpResponse('success!')
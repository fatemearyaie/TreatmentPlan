from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Patient, ScalingProphy, Pictures
from .forms import PatientForm
from django.db import transaction

# Create your views here.
def PatientsBasicRecord(request):
    return render(request, 'treatmentplan.html')

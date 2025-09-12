from django import forms
from django.utils import timezone
from .models import Patient, ScalingProphy, Pictures

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient  
        fields = ['case_id','patient_FullName','visit_date','visit_date']
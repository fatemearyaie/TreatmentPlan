from django import forms
from django.utils import timezone

class PatientForm(forms.ModelForm):
    case_id = forms.CharField(max_length=255)
    patient_FullName = forms.CharField(max_length=25)
    visit_date = forms.DateField(default=timezone.now)
    disease = forms.CharField(max_length=500, null=True, blank=True)

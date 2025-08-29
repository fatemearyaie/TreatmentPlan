from django.contrib import admin
from .models import Patient
# Register your models here.
class PatientAdmin(admin.ModelAdmin):
    model = Patient
    list_display = ['case_id', 'patient_FullName', 'visit_date', 'disease']
admin.site.register(Patient, PatientAdmin)
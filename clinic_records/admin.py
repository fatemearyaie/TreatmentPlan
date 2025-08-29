from django.contrib import admin
from .models import Patient, Pictures
# Register your models here.
class PatientAdmin(admin.ModelAdmin):
    list_display = ['case_id', 'patient_FullName', 'visit_date', 'disease']

class PicturesAdmin(admin.ModelAdmin):
    list_display = ['opg', 'photo']
admin.site.register(Pictures, PicturesAdmin)
admin.site.register(Patient, PatientAdmin)
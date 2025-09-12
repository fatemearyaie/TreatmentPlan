from .views import PatientsBasicRecord
from django.urls import path

urlpatterns = [
    path('', PatientsBasicRecord, name='patient')
]

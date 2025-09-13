from .views import PatientsBasicRecord, SuccessView
from django.urls import path

urlpatterns = [
    path('', PatientsBasicRecord, name='patient'),
    path('success/', SuccessView, name='success')
]

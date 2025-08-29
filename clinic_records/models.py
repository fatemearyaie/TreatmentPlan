from django.db import models
from django.utils import timezone

# Create your models here.
class Patient(models.Model):
    case_id = models.CharField(max_length=255)
    patient_FullName = models.CharField(max_length=30)
    visit_date = models.DateField(default=timezone.now)
    disease = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.patient_FullName
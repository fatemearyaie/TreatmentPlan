from django.db import models
from django.utils import timezone

# Create your models here.
class Patient(models.Model):
    case_id = models.CharField(max_length=255, primary_key=True)
    patient_FullName = models.CharField(max_length=30)
    visit_date = models.DateField(default=timezone.now)
    disease = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.patient_FullName
    
class Pictures(models.Model):
    bite_wing1 = models.BooleanField(null=True, blank=True)
    bite_wing2 = models.BooleanField(null=True, blank=True)
    bite_wing3 = models.BooleanField(null=True, blank=True)
    bite_wing4 = models.BooleanField(null=True, blank=True)

    PA1 = models.CharField(max_length=1, null=True, blank=False)
    PA2 = models.CharField(max_length=1, null=True, blank=False)
    PA3 = models.CharField(max_length=1, null=True, blank=False)
    PA4 = models.CharField(max_length=1, null=True, blank=False)

    opg = models.BooleanField(default=True)
    photo =  models.BooleanField(default=True)
    pictures_price = models.DecimalField(max_digits=9, decimal_places=0, null=True, blank=True)
    picture_note = models.TextField(default=None)
    patient = models.ManyToManyField("patient")

    def __str__(self):
        return f"{self.pictures_price} - self.patient.patient_FullName"

class ScalingProphy(models.Model):
    count_session_choice = [
        ('one','one session'),
        ('two', 'two sessions')
    ]
    sessions_count = models.BooleanField(choices=count_session_choice)
    scalingprophy_price = models.DecimalField(max_digits=9, decimal_places=0, null=False, blank=False)
    scalingprophy_note = models.TextField(default=None)
    
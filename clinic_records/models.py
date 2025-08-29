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
    

class Pictures(models.Model):
    Bite_wings_choices = [
        ('1' , '1'),
        ('2' , '2'),
        ('3' , '3'),
        ('4' , '4'),
    ]
    bite_wings = models.CharField(max_length=1, choices=Bite_wings_choices)
    opg = models.BooleanField(default=True)
    photo =  models.BooleanField(default=True)
    PA_coices =[
        ('1','1'),
        ('2', '2'),
        ('3','3'),
        ('4','4')
    ]
    PA = models.CharField(max_length=1, choices=PA_coices)
    pictures_price = models.DecimalField(max_digits=9, decimal_places=0, null=True, blank=True)
    picture_note = models.CharField(max_length=1000, default=None)
    patient = models.ManyToManyField("patient")

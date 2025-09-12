from django.db import models

# Create your models here.
class UserControl(models.Model):
    name = models.CharField(max_length=50)
    family = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)
    created_dt = models.DateTimeField(auto_now_add=True)
    modified_df = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.family} - {self.name}'
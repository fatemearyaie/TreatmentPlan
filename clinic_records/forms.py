from django import forms
from django.utils import timezone
from .models import Patient, ScalingProphy, Pictures

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient  
        fields = ['case_id','patient_FullName','visit_date','disease']

class PictureForm(forms.ModelForm):
    class Meta:
        model = Pictures
        fields = ['bite_wing1','bite_wing2','bite_wing3','bite_wing4', 'PA1','PA2','PA3','PA4','opg','photo','pictures_price','picture_note','patient']

class ScalingProphyForm(forms.ModelForm):
    class Meta:
        model = ScalingProphy
        fields = ['sessions_count', 'scalingprophy_price', 'scalingprophy_note']
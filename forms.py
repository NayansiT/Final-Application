from django import forms
from .models import Application

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['name', 'address', 'email', 'phone_number', 'date_of_birth',
                  'tenth_marks', 'twelfth_marks', 'graduation_marks',
                  'profile_picture', 'document']

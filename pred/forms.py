from .models import Journaltable 
from django import forms

class JournlSearchForm(forms.ModelForm):
    class Meta:
        model = Journaltable
        fields = ['publisher', 'journal']


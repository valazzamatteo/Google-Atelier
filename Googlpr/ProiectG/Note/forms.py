from django import forms
from .models import Notes

class CreateNewNota(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['name', 'text']

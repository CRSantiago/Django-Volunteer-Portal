from django import forms

from .models import Log

class LogForm(forms.ModelForm):
    class Meta:
        model = Log
        fields = [
            'date',
            'hours_completed',
        ]
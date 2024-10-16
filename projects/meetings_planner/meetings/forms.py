from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm, DateInput, TimeInput, TextInput
from .models import Meeting
from datetime import date

class MeetingForm(ModelForm):
    class Meta:
        model = Meeting
        fields = '__all__'
        widgets = {
            'date': DateInput(attrs={"type": "date"}),
            'start': TimeInput(attrs={"type": "time"}),
            'duration': TextInput(attrs={"type": "number", "min": "1", "max": "4"})
        }

    def clean_date(self):
        d = self.cleaned_data.get("date")
        if d < date.today():
            raise ValidationError("Les réunions ne peuvent pas être dans le passé.")
        return d

from django import forms
from django.core.exceptions import ValidationError


class NasaForm(forms.Form):
    start = forms.DateField(
        input_formats=['%Y-%m-%d'], widget=forms.SelectDateWidget())

    end = forms.DateField(
        input_formats=['%Y-%m-%d'], widget=forms.SelectDateWidget())

    def clean(self):
        cleaned_data = super().clean()
        first = cleaned_data.get("start")
        last = cleaned_data.get("end")

        if first and last:

            if first > last:
                raise ValidationError(
                    "end date must be after start date"
                )

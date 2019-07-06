from django import forms
from .models import Configuration


class ConfigurationForm(forms.ModelForm):
    class Meta:
        model = Configuration
        exclude = ('id', )

        widgets = {
            'site_name': forms.TextInput(attrs={'class': 'form-control'}),
            'site_name_mini': forms.TextInput(attrs={'class': 'form-control'}),
            'use_site_name': forms.CheckboxInput(attrs={'class': 'form-control i-checks'}),
            'site_logo': forms.FileInput(),
            'site_logo_mini': forms.FileInput(),
            'order_code_sequence': forms.NumberInput(attrs={'class': 'form-control'}),
        }

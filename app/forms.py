from django import forms
from django.core import validators

def must_be_empty(value):
    if value:
        raise forms.ValidationError("is not empty")

class TestForm(forms.Form):
    name= forms.CharField(label="Name", help_text="Please Insert a name" , required=False, validators=[must_be_empty])
    email=forms.EmailField(required=True, label="Email",validators=[validators.EmailValidator])
    verify=forms.EmailField(required=True, label="Email",validators=[validators.EmailValidator])

    def clean(self):
        cleaned_data= super().clean()
        if cleaned_data['email'] != cleaned_data['verify']:
            raise forms.ValidationError("Not same Emails")
from django import forms
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class OrganizationSignUpForm(forms.ModelForm):
    organization_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(validators=[RegexValidator(r'^\d{10}$')], required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    confirm_password = forms.CharField(widget=forms.PasswordInput, required=True)

    class Meta:
        model = User
        fields = ['organization_name', 'email', 'phone_number', 'password', 'confirm_password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")

        return cleaned_data

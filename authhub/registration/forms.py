from django import forms
from .models import Accounts_Table

class Form(forms.ModelForm):
    class Meta:
        model = Accounts_Table
        fields = ("first_name", "last_name", "gmail", "username", "password", "security")
        widgets = {
            'password': forms.PasswordInput(),  # This hides the password input
        }


    def clean_username(self):
        username = self.cleaned_data.get('username')
        if Accounts_Table.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already taken. Please choose a different username.")
        return username
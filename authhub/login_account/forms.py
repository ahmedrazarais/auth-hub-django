from django import forms

class Login_Form(forms.Form):
    username = forms.CharField(max_length=50, required=True)
    password = forms.CharField(widget=forms.PasswordInput(), required=True)



class Forgot_password(forms.Form):
    username = forms.CharField(max_length=50, required=True)
    security = forms.CharField(max_length=50, required=True)
    new_password = forms.CharField(widget=forms.PasswordInput(), required=True)







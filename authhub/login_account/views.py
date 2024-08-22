from registration.models import Accounts_Table
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import Login_Form,Forgot_password
from django.contrib.auth.hashers import check_password,make_password

def login_home_page(request):
    return render(request, "login_account/login_home.html")


def login_form_input(request):
    if request.method == "POST":
        form = Login_Form(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username").strip()
            password = form.cleaned_data.get("password")

            # Check if the user exists in Accounts_Table
            user = Accounts_Table.objects.filter(username__iexact=username).first()

            if user is None:
                messages.error(request, 'The username you entered does not exist.')

            elif not check_password(password, user.password):
                messages.error(request, 'The password you entered is incorrect.')

            else:
            
                return redirect('login_success')

    else:
        form = Login_Form()

    return render(request, "login_account/login_form.html", {"form": form})


def login_success(request):
    return render(request, "login_account/login_success.html")



def forgot_pswd(request):
    if request.method == "POST":
        form = Forgot_password(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username").strip()
            security = form.cleaned_data.get("security").strip()
            new_password = form.cleaned_data.get("new_password")

            # Check if the user exists in Accounts_Table
            user = Accounts_Table.objects.filter(username__iexact=username).first()

            if user is None:
                messages.error(request, 'The username you entered does not exist.')
            elif user.security != security:  # Direct comparison if security answer is not hashed
                messages.error(request, 'The security answer you entered is incorrect.')
            else:
                # Update the password
                user.password = make_password(new_password)
                user.save()
                return redirect('password_update') 
    else:
        form = Forgot_password()

    return render(request, "login_account/forgot_password.html", {"form": form})


def password_update(request):
    return render(request, "login_account/update_pswd_news.html")

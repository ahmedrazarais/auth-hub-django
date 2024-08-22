from django.shortcuts import render,redirect
from .forms import Form

# Create your views here.
def register(request):
    return render(request,"registration/register_info.html")

def registration_form(request):
    if request.method == 'POST':
        accounts_form = Form(request.POST)
        if accounts_form.is_valid():
            accounts_form.save()
            return redirect("success")
    else:
        accounts_form = Form()

    return render(request, "registration/register.html", {"account_form": accounts_form})




def register_complete(request):
    return render(request,"registration/creation_message.html")

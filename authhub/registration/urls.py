
from django.urls import path
from . import views

urlpatterns = [
  
    path('' , views.register, name="register_home"),
    path('registration_process/' , views.registration_form, name="register_process"),
    path('register_complete/' , views.register_complete, name="success"),
   
    

]
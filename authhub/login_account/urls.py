
from django.urls import path
from . import views

urlpatterns = [
    
    path('' , views.login_home_page , name="login_home_page"),
    path('login_form/' , views.login_form_input , name="login_form_input"),
    path('login_success/' , views.login_success , name="login_success"),
    path('forgot_password/' , views.forgot_pswd , name="forgot_pswd"),
    path('Password_Updated/' , views.password_update , name="password_update"),

    

]
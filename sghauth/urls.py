from django.urls import path
from . import  views
app_name = 'sghauth'
urlpatterns = [
    path('login',views.sghlogin,name='login' ),
    path('register',views.register,name='register' ),
    path('captcha',views.send_email_captcha,name='email_captcha' ),
    path('logout',views.sghlogout,name='logout' ),
]

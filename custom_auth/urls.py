from django.urls import path
from custom_auth.views import UserRegisterAPIViews
"""ВРУЧНУЮ"""
from custom_auth.views import LoginView

from rest_framework.authtoken.views import obtain_auth_token #АВТОМАТИЧЕСКИ


urlpatterns = [
    path('registration/', UserRegisterAPIViews.as_view(), name='user-registration'),
    # path('logining/', obtain_auth_token, name='user-obtain_auth_token'), #АВТОМАТИЧЕСКИ
    path('login/', LoginView.as_view()), #Вручную
]

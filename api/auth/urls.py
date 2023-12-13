from django.urls import path, include
from .views import *
from rest_framework import routers 

urlpatterns = [
    #path('auth/token', ObtainTokenView.as_view()),
    # path('register/',UserView.as_view()),
    # path('update/',UserView.as_view()),
    path('token/',ObtainTokenView.as_view()),
    path('details/',VerificationView.as_view())
]
from django.urls import path, include
from .views import *
from rest_framework import routers 
from .views import *
urlpatterns = [
    #path('auth/token', ObtainTokenView.as_view()),
    path('import/',ImportView.as_view()),
]
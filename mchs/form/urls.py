from django.urls import path, include
from .views import post


urlpatterns = [
    path('', post)
]
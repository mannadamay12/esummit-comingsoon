from django.urls import path
from .views import *

urlpatterns = [
    path('',                register,			name='register'),
    path('gallery/',        gallery,			name='gallery'),
]
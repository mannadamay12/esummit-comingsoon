from django.urls import path
from .views import *

urlpatterns = [
    path('',                subscribe,			name='subscribe'),
    path('gallery/',        gallery,			name='gallery'),
]
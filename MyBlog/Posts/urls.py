from django.urls import path

from .views import base, newpost

urlpatterns = [
    path('', base, name='base'),
    path('newpost/', newpost, name='newpost'),
]
from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('try/', home_view, name='home_view')
]

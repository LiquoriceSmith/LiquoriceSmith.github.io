from django.shortcuts import render
from .models import MainPage
# Create your views here.
from django.http import HttpResponse


def index(request):
    exemplar = MainPage.objects.all()
    return render(request, 'biography/index.html', {'exemplar': exemplar})

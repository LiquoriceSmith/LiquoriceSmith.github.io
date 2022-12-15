from django.shortcuts import render
from .models import MainPage, Otzivy
from .forms import OtzivForm
# Create your views here.
from django.http import HttpResponseRedirect


def index(request):
    exemplar = MainPage.objects.all()

    otzyv = Otzivy.objects.all().order_by('-id')[:3]
    return render(request, 'biography/Главная.html', {'exemplar': exemplar, 'otzyv': otzyv})


def home_view(request):
    if request.method == 'POST':
        form = OtzivForm(request.POST, request.FILES)
        form.save()
        return HttpResponseRedirect(request.path)
    else:
        form = OtzivForm()

    return render(request, "biography/otziv.html", {"form": form})

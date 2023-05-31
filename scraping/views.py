from django.shortcuts import render
from .models import Vacancy

def home(request):
    qs = Vacancy.objects.all()
    return render(request, 'base.html', {'object_list': qs, 'name': 'ssssss'})

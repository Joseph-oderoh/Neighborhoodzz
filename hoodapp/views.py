from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import NeighbourHood
# Create your views here.

def homepage(request):
    return render(request, 'index.html')


def hoods(request):
    all_hoods = NeighbourHood.objects.all()
    all_hoods = all_hoods[::-1]
    params = {
        'all_hoods': all_hoods,
    }
    return render(request, 'hoodz.html', params)
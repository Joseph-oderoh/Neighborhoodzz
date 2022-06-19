from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from .forms import NeighbourHoodForm

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

def create_hood(request):
    if request.method == 'POST':
        form = NeighbourHoodForm(request.POST, request.FILES)
        if form.is_valid():
            hood = form.save(commit=False)
            hood.admin = request.user.profile
            hood.save()
            return redirect('hood')
    else:
        form = NeighbourHoodForm()
    return render(request, 'new_hoodz.html', {'form': form})

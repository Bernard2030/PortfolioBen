from django.shortcuts import render
from .models import Home,About,Category,Skills,Portfolio

# Create your views here.

def home(request):

# Home view

    home = Home.objects.latest('updated')

    context = {
        "home": home,
    }
    return render(request, 'home.html', context)     

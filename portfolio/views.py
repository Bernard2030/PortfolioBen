from django.shortcuts import render
from .models import Home,About,Category,Skills,Portfolio,Profile

# Create your views here.

def home(request):

# Home view

    home = Home.objects.latest('updated')

    


#About view

    about = About.objects.latest('updated')
    profiles = Profile.objects.filter(about=about)  

    context = {
        "home": home,
        "about": about,
        "profiles": profiles, 
    }
    return render(request, 'home.html', context) 


 

from django.shortcuts import render , redirect , HttpResponse
from django.contrib import messages

from .models import Team , Services , Contact

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')


def services(request):
    services = Services.objects.all()
    return render(request, 'services.html',{'services':services})


def team(request):
    team = Team.objects.all()
    return render(request, 'team.html', {'team':team})




def contact(request):
    if request.method == 'POST':
        
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        print(name,email)
        con = Contact(name=name,email=email,subject=subject, message=message)
        con.save()
        messages.info(request,  " message sent ")
        return redirect('/contact/')
    
    else:

        return render(request,'contact.html')
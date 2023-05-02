from django.shortcuts import render
from django.http import HttpResponse
from Home.models import (Contact)
# Create your views here.


def index(request):
    return render(request, 'index.html')




def contact_us(request):
    if request.method == 'POST':
        data = request.POST
        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')
        message = data.get('message')
        contact = Contact.objects.create(name= name, email = eamil, phone = phone, message = message)
        contact.save()
    return render(request, 'contacts.html')



def about_us(request):
    return render(request, 'about.html')


def computers(request):
    return render(request, 'fastercomputers.html')
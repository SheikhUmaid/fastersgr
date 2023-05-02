from django.urls import path

from .views import *



urlpatterns = [
    path('', index, name = 'index'),
    path('contact/', contact_us, name = 'Contact'),
    path('about/', about_us, name = 'about'),
    path('computers/', computers, name = 'computers')
]
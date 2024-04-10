from django.shortcuts import render
from django.http import HttpResponse

from listings.models import Brand, Listing

def hello(request):
    brands = Brand.objects.all()
    listings = Listing.objects.all()
    return render(request, 'listings/hello.html', {'brands' : brands, 'listings' : listings })

def about(request):
    return HttpResponse('<h1> Page à propos de Django </h1>')

def listings(request):
    return HttpResponse('<h1> Page Listings  </h1>')

def contact(request):
    return HttpResponse('<h1> Formulaire de contact </h1>')
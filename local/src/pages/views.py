from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Hello</h1>")
    return render(request, 'home.html', {})

def contact_view(*args, **kwargs):
    return HttpResponse("<h1>Info</h1>")
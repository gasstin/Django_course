from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Hello</h1>")
    my_context = {
        "text": "This is the home page",
        "favorite_number": 31,
        "list": [44,67,88,65,89]
    }
    return render(request, 'home.html', my_context)

def contact_view(*args, **kwargs):
    return HttpResponse("<h1>Info</h1>")
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


# This will return the literal text "Howdy!" to the browser.
def hello(request):
    # pull data from database
    # transform data
    # send emails, etc
    return HttpResponse("Howdy!")


# This will return a template
def wakeup(request):
    return render(request, 'wakeup.html')


def teapot(request):
    return render(request, 'teapot.html')


def lovelyday(request):
    return render(request, 'lovelyday.html')


def plate_of_tem(request):
    return render(request, 'plate_of_tem.html', {'name': 'Sweet Tea'})

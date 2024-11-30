from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage(request):
    text = "Mening birinchi Django saytim"
    text += '<br><br>Mening ismim Asilbek, Hello World!'
    return HttpResponse(text)



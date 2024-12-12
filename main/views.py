from django.shortcuts import render
from django.http import HttpResponse
from .models import Kitob

# Create your views here.
def homepage(request):
    kitoblar = Kitob.objects.all()
    context = {
        'books': kitoblar
    }
    return render(request, template_name='index.html', context=context)





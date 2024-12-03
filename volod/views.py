from django.shortcuts import render


from .forms import *

def index(request):
    myForm = MyFrom()
    return render(request, 'index.html', context={'form': myForm})
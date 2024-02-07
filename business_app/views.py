from django.shortcuts import render
from django.views.generic import View


# Create your views here.
def business(request, template_name='business/index.html'):
    return render(request, template_name)



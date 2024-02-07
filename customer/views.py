from django.shortcuts import render


# Create your views here.

def customer(request, template_name='customer/index.html'):
    return render(request, template_name)

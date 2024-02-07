from django.shortcuts import render


# Create your views here.


def public(request, template_name='public/index.html'):
    return render(request, template_name)

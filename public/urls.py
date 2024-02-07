from django.urls import path
from .views import public

urlpatterns = [
    path('', public, name='public')
]
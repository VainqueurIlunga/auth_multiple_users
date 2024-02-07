from django.urls import path
from .views import business
urlpatterns = [
    path('', business, name='business')
]
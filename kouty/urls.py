# urls.py
from django.urls import path
from .views import contact
app_name = 'contact'

urlpatterns = [
    path('contact/', contact, name='contact'),
]

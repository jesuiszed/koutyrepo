from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='admin_index'),
    path('login/', views.login_view, name='admin_login'),
    path('services/', views.gestion_services, name='gestion_services'),
    path('produits/', views.gestion_produits, name='gestion_produits'),
    path('partenaires/', views.gestion_partenaires, name='gestion_partenaires'),
    path('specialistes/', views.gestion_specialistes, name='gestion_specialistes'),
]

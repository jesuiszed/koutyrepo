from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.index, name='admin_index'),
    path('login/', views.login_view, name='admin_login'),
    path('deconnexion', CustomLogoutView.as_view(), name='custom_logout'),
    path('services/', views.gestion_services, name='gestion_services'),
    path('produits/', views.gestion_produits, name='gestion_produits'),
    path('partenaires/', views.gestion_partenaires, name='gestion_partenaires'),
    path('specialistes/', views.gestion_specialistes, name='gestion_specialistes'),
    path('mentions/', views.gestion_mentions, name='gestion_mentions'),
    path('temoins/', views.gestion_temoin, name='gestion_temoin'),
    path('visitor_stats/', views.visitor_stats, name='visitor_stats'),
]

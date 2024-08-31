from django.urls import path
from koutyMa import settings
from . import views
from django.conf.urls.static import static

app_name = 'koutyUsers'

urlpatterns = [
    path('', views.index, name='index'),
    path('base/', views.base, name='base'),
    path('mention/', views.mention, name='mention'),
    path('produit/', views.produit, name='produit'),
    path('specialiste/', views.specialiste, name='specialiste'),

]

from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from kouty.models import *

def index(request):
    service = Service.objects.all()
    produit = Produit.objects.all()[:3]
    partenaire = Partenaire.objects.all()
    specialiste = Specialiste.objects.all()
    temoins = Temoin.objects.all()
    mentions = Mention.objects.all().order_by('-date_publication')[:3]



    context = {
        'service': service,
        'produit': produit,
        'partenaire': partenaire,
        'specialiste': specialiste,
        'temoins': temoins,
        'mentions': mentions
    }

    return render(request, 'index.html', context)

def base(request):
    return render(request, 'base.html')
def mention(request):
    mentions_list = Mention.objects.all().order_by('-date_publication')  # Trie les mentions par date de publication, la plus récente en premier
    paginator = Paginator(mentions_list, 6)  # Nombre de mentions par page, ici 6

    page_number = request.GET.get('page')  # Récupère le numéro de la page actuelle
    mentions = paginator.get_page(page_number)  # Obtient les mentions de la page demandée

    return render(request, 'newsPage.html', {'mentions': mentions})

def produit(request):
    produit_list = Produit.objects.all()  # Trie les mentions par date de publication, la plus récente en premier
    paginator = Paginator(produit_list, 6)  # Nombre de mentions par page, ici 6

    page_number = request.GET.get('page')  # Récupère le numéro de la page actuelle
    produits = paginator.get_page(page_number)  # Obtient les mentions de la page demandée

    return render(request, 'productPage.html', {'produits': produits})

def specialiste(request):
    specialiste_list = Specialiste.objects.all()  # Récupère tous les spécialistes
    paginator = Paginator(specialiste_list, 6)  # Nombre de spécialistes par page, ici 6

    page_number = request.GET.get('page')  # Récupère le numéro de la page actuelle
    specialistes = paginator.get_page(page_number)  # Obtient les spécialistes de la page demandée

    return render(request, 'specialistsPage.html', {'specialistes': specialistes})
from django.shortcuts import render
from kouty.models import Service, Produit, Partenaire, Specialiste

def index(request):
    service = Service.objects.all()
    produit = Produit.objects.all()
    partenaire = Partenaire.objects.all()
    specialiste = Specialiste.objects.all()

    context = {
        'service': service,
        'produit': produit,
        'partenaire': partenaire,
        'specialiste': specialiste,
    }

    return render(request, 'index.html', context)

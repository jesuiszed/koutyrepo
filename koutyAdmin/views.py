from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse
from kouty.models import Service, Produit, Partenaire, Specialiste
from koutyAdmin.forms import ServiceForm, ProduitForm, PartenaireForm, SpecialisteForm

def index(request):
    return render(request, 'admin/index.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('admin_index'))
        else:
            return render(request, 'admin/login.html', {'error_message': 'Invalid credentials'})
    return render(request, 'admin/login.html')

@login_required(login_url='admin_login')
def gestion_services(request):
    services = Service.objects.all()
    form = ServiceForm()

    if request.method == 'POST':
        if 'modifier' in request.POST:
            service_id = request.POST['service_id']
            service = Service.objects.get(pk=service_id)
            form = ServiceForm(request.POST, request.FILES, instance=service)
            if form.is_valid():
                form.save()
        elif 'supprimer' in request.POST:
            service_id = request.POST['service_id']
            service = Service.objects.get(pk=service_id)
            service.delete()
        elif 'ajouter' in request.POST:
            form = ServiceForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('gestion_services')

    context = {'services': services, 'form': form}
    return render(request, 'admin/gest_services.html', context)

@login_required(login_url='admin_login')
def gestion_produits(request):
    produits = Produit.objects.all()
    form = ProduitForm()

    if request.method == 'POST':
        if 'modifier' in request.POST:
            produit_id = request.POST['produit_id']
            produit = Produit.objects.get(pk=produit_id)
            form = ProduitForm(request.POST, request.FILES, instance=produit)
            if form.is_valid():
                form.save()
        elif 'supprimer' in request.POST:
            produit_id = request.POST['produit_id']
            produit = Produit.objects.get(pk=produit_id)
            produit.delete()
        elif 'ajouter' in request.POST:
            form = ProduitForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('gestion_produits')

    context = {'produits': produits, 'form': form}
    return render(request, 'admin/gest_produits.html', context)

@login_required(login_url='admin_login')
def gestion_partenaires(request):
    partenaires = Partenaire.objects.all()
    form = PartenaireForm()

    if request.method == 'POST':
        if 'modifier' in request.POST:
            partenaire_id = request.POST['partenaire_id']
            partenaire = Partenaire.objects.get(pk=partenaire_id)
            form = PartenaireForm(request.POST, request.FILES, instance=partenaire)
            if form.is_valid():
                form.save()
        elif 'supprimer' in request.POST:
            partenaire_id = request.POST['partenaire_id']
            partenaire = Partenaire.objects.get(pk=partenaire_id)
            partenaire.delete()
        elif 'ajouter' in request.POST:
            form = PartenaireForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('gestion_partenaires')

    context = {'partenaires': partenaires, 'form': form}
    return render(request, 'admin/gest_partenaires.html', context)

@login_required(login_url='admin_login')
def gestion_specialistes(request):
    specialistes = Specialiste.objects.all()
    form = SpecialisteForm()

    if request.method == 'POST':
        if 'modifier' in request.POST:
            specialiste_id = request.POST['specialiste_id']
            specialiste = Specialiste.objects.get(pk=specialiste_id)
            form = SpecialisteForm(request.POST, request.FILES, instance=specialiste)
            if form.is_valid():
                form.save()
        elif 'supprimer' in request.POST:
            specialiste_id = request.POST['specialiste_id']
            specialiste = Specialiste.objects.get(pk=specialiste_id)
            specialiste.delete()
        elif 'ajouter' in request.POST:
            form = SpecialisteForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('gestion_specialistes')

    context = {'specialistes': specialistes, 'form': form}
    return render(request, 'admin/gest_specialistes.html', context)

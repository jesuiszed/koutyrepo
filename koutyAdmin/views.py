from pyexpat.errors import messages
from django.utils import timezone
from django.db.models import Count
from django.db.models.functions import TruncMonth, TruncYear
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from kouty.models import *
from koutyAdmin.forms import *
def index(request):
    return render(request, 'admin/visitor_stats.html')
def index1(request):
    return render(request, 'registration/password_reset_email.html')
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

@login_required(login_url='admin_login')
def gestion_mentions(request):
    mentions = Mention.objects.all()
    form = MentionForm()

    if request.method == 'POST':
        if 'modifier' in request.POST:
            mention_id = request.POST.get('mention_id')
            mention = get_object_or_404(Mention, pk=mention_id)
            form = MentionForm(request.POST, request.FILES, instance=mention)
            if form.is_valid():
                form.save()
                messages.success(request, 'Mention modifiée avec succès.')
                return redirect('gestion_mentions')
        elif 'supprimer' in request.POST:
            mention_id = request.POST.get('mention_id')
            mention = get_object_or_404(Mention, pk=mention_id)
            mention.delete()
            messages.success(request, 'Mention supprimée avec succès.')
            return redirect('gestion_mentions')
        elif 'ajouter' in request.POST:
            form = MentionForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, 'Mention ajoutée avec succès.')
                return redirect('gestion_mentions')

    context = {'mentions': mentions, 'form': form}
    return render(request, 'admin/gest_mention.html', context)

@login_required(login_url='admin_login')
def gestion_temoin(request):
    temoins = Temoin.objects.all()
    form = TemoinForm()

    if request.method == 'POST':
        if 'modifier' in request.POST:
            temoin_id = request.POST.get('temoin_id')
            temoin = get_object_or_404(Temoin, pk=temoin_id)
            form = TemoinForm(request.POST, request.FILES, instance=temoin)
            if form.is_valid():
                form.save()
                messages.success(request, 'Témoin modifié avec succès.')
                return redirect('gestion_temoin')
        elif 'supprimer' in request.POST:
            temoin_id = request.POST.get('temoin_id')
            temoin = get_object_or_404(Temoin, pk=temoin_id)
            temoin.delete()
            messages.success(request, 'Témoin supprimé avec succès.')
            return redirect('gestion_temoin')
        elif 'ajouter' in request.POST:
            form = TemoinForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, 'Témoin ajouté avec succès.')
                return redirect('gestion_temoin')

    context = {'temoins': temoins, 'form': form}
    return render(request, 'admin/gest_temoin.html', context)

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('admin_login')


def visitor_stats(request):
    today = timezone.now().date()

    # Statistiques journalières
    today_count = VisitorCount.objects.filter(date=today).first()
    total_count = sum(VisitorCount.objects.values_list('count', flat=True))

    # Statistiques par pays et ville
    country_stats = Visitor.objects.values('country').annotate(count=Count('id')).order_by('-count')
    city_stats = Visitor.objects.values('city').annotate(count=Count('id')).order_by('-count')

    # Statistiques mensuelles
    monthly_stats = Visitor.objects.annotate(month=TruncMonth('timestamp')).values('month').annotate(
        count=Count('id')).order_by('-month')

    # Statistiques annuelles
    yearly_stats = Visitor.objects.annotate(year=TruncYear('timestamp')).values('year').annotate(
        count=Count('id')).order_by('-year')

    context = {
        'today_count': today_count.count if today_count else 0,
        'total_count': total_count,
        'country_stats': country_stats[:10],  # Top 10 countries
        'city_stats': city_stats[:10],  # Top 10 cities
        'monthly_stats': monthly_stats[:12],  # Last 12 months
        'yearly_stats': yearly_stats,
    }
    return render(request, 'admin/visitor_stats.html', context)
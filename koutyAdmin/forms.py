from django import forms
from kouty.models import Service, Produit, Partenaire, Specialiste

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['titre', 'description', 'image']

class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = ['titre', 'description', 'image']

class PartenaireForm(forms.ModelForm):
    class Meta:
        model = Partenaire
        fields = ['nom', 'description', 'image']

class SpecialisteForm(forms.ModelForm):
    class Meta:
        model = Specialiste
        fields = ['nom', 'role', 'image']

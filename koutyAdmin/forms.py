from django import forms
from kouty.models import *

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
class MentionForm(forms.ModelForm):
    class Meta:
        model = Mention
        fields = ['titre', 'source', 'lien', 'extrait', 'date_publication', 'image']

class TemoinForm(forms.ModelForm):
    class Meta:
        model = Temoin
        fields = ['nom', 'role', 'temoignage', 'image']
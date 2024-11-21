from django.db import models

class Service(models.Model):

    id = models.AutoField(primary_key=True)
    titre = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='media/', blank=True, null=True)
    def __str__(self):
        return self.titre

class Produit(models.Model):

    id = models.AutoField(primary_key=True)
    titre = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='Produit/', blank=True, null=True)
    def __str__(self):
         return self.titre

class Partenaire(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='Partenaire/', blank=True, null=True)
    def __str__(self):
        return self.nom

class Specialiste(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Specialiste/', blank=True, null=True)
    def __str__(self):
        return self.nom


class Mention(models.Model):
    titre = models.CharField(max_length=200)
    source = models.CharField(max_length=200)  # Le site ou la publication d'origine
    lien = models.URLField(max_length=500, blank=True, null=True)  # Lien vers l'article
    extrait = models.TextField()  # Un extrait pertinent de l'article
    date_publication = models.DateField()
    image = models.ImageField(upload_to='actualites/', blank=True, null=True)


    def __str__(self):
        return f"{self.titre} ({self.source})"


class Role(models.TextChoices):
    CLIENT = 'Client', 'Client'
    EMPLOYE = 'Employé', 'Employé'
    PARTENAIRE = 'Partenaire', 'Partenaire'
    FOURNISSEUR = 'Fournisseur', 'Fournisseur'
    AUTRE = 'Autre', 'Autre'


class Temoin(models.Model):
    nom = models.CharField(max_length=100)
    role = models.CharField(max_length=100, choices=Role.choices, default=Role.AUTRE)
    temoignage = models.TextField()
    image = models.ImageField(upload_to='Temoignages/', blank=True, null=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.nom} - {self.role}"


class Visitor(models.Model):
    ip_address = models.GenericIPAddressField()
    country = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

class VisitorCount(models.Model):
    count = models.IntegerField(default=0)
    date = models.DateField(unique=True)
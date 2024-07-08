from django.db import models

class Service(models.Model):

    id = models.AutoField(primary_key=True)
    titre = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='Service/', blank=True, null=True)
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
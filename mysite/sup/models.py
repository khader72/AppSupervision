from django.db import models

# Create your models here.



class Host(models.Model):
    id_host = models.CharField(primary_key=True, max_length=255)
    hostname = models.CharField(max_length=255)
    adresse_ip = models.CharField(max_length=20)
    description = models.CharField(max_length=240)
    id_equipement = models.CharField(max_length=240)
    id_service = models.CharField(max_length=70)
    id_type = models.IntegerField()
    
class Equipement(models.Model):
    id_equipement = models.CharField(primary_key=True, max_length=25)
    libelle_equipement = models.CharField(max_length=40)
    

    
class GroupHost(models.Model):
    id_group_host = models.CharField(primary_key=True, max_length=40)
    libelle_group_host = models.CharField(max_length=70)
    
    
class HistoryConnect(models.Model):
    id_hist = models.CharField(primary_key=True, max_length=30)
    login = models.CharField(max_length=40)
    last_connect = models.DateTimeField()
    ip_connect = models.CharField(max_length=20)
    lib_connect = models.CharField(max_length=20)
    

    

class Privilege(models.Model):
    id_privilege = models.AutoField(primary_key=True)
    lib_privilege = models.CharField(max_length=30)
    
    
class Service(models.Model):
    id_service = models.CharField(primary_key=True, max_length=255)
    libelle_service = models.CharField(max_length=255)
    email_service = models.CharField(max_length=255)
    dept_service = models.CharField(max_length=255)
    
class Systeme(models.Model):
    id_systeme = models.CharField(primary_key=True, max_length=50)
    libelle_systeme = models.CharField(max_length=30)
    
class Type(models.Model):
    id_type = models.AutoField(primary_key=True)
    libelle_type = models.CharField(max_length=60)
    

class User(models.Model):
    id_user = models.CharField(primary_key=True, max_length=20)
    nom = models.CharField(max_length=40)
    prenom = models.CharField(max_length=60)
    user = models.CharField(max_length=20)
    password = models.CharField(max_length=255)
    last_connect = models.DateField()
    status = models.CharField(max_length=1)
    creation_date = models.DateField()
    id_privilege = models.CharField(max_length=20)

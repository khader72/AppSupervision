# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Equipement(models.Model):
    id_equipement = models.CharField(primary_key=True, max_length=25)
    libelle_equipement = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'equipement'


class GroupHost(models.Model):
    id_group_host = models.CharField(primary_key=True, max_length=40)
    libelle_group_host = models.CharField(max_length=70)

    class Meta:
        managed = False
        db_table = 'group_host'


class HistoryConnect(models.Model):
    id_hist = models.CharField(primary_key=True, max_length=30)
    login = models.CharField(max_length=40)
    last_connect = models.DateTimeField()
    ip_connect = models.CharField(max_length=20)
    lib_connect = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'history_connect'


class Host(models.Model):
    id_host = models.CharField(primary_key=True, max_length=255)
    hostname = models.CharField(max_length=255)
    adresse_ip = models.CharField(max_length=12)
    description = models.CharField(max_length=240)
    id_equipement = models.CharField(max_length=240)
    id_service = models.CharField(max_length=70)
    id_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'host'


class Privilege(models.Model):
    id_privilege = models.AutoField(primary_key=True)
    lib_privilege = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'privilege'


class Service(models.Model):
    id_service = models.CharField(primary_key=True, max_length=255)
    libelle_service = models.CharField(max_length=255)
    email_service = models.CharField(max_length=255)
    dept_service = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'service'


class Systeme(models.Model):
    id_systeme = models.CharField(primary_key=True, max_length=50)
    libelle_systeme = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'systeme'


class Type(models.Model):
    id_type = models.AutoField(primary_key=True)
    libelle_type = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'type'


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

    class Meta:
        managed = False
        db_table = 'user'

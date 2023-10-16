from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.template import loader
from random import randint
from django.views.decorators.csrf import csrf_protect
from .models import Host,Type,Equipement,Service,User,Privilege
import sweetify
from django.db import connection
import datetime


# Create your views here.


def index(request):
    template = loader.get_template("sup/home.html")
    context= {
        "latest_question_list": 'test',
    }
    return HttpResponse(template.render(context,request))


def host(request):
    match request.method:
        case 'GET':
            dataHostAll = Host.objects.all()
            dataType = Type.objects.all().values()
            dataEquip = Equipement.objects.all()
            dataService = Service.objects.all()
            
            context = {
                'dataHostAll': dataHostAll,
                'dataType' : dataType,
                'dataEquip' : dataEquip,   
                'dataService':dataService,    
            }
            template= loader.get_template("sup/host.html")
            return HttpResponse(template.render(context,request))
        case 'POST':
            id=randint(0,99999)
            hostname= request.POST['hostname']
            adresse_ip=request.POST['adresse_ip']
            description=request.POST['descriptions']
            equipement=request.POST['equipement']
            service=request.POST['service']
            type=request.POST['types']
            datahost =Host.objects.create(id_host=id,hostname=hostname,adresse_ip=adresse_ip,description=description,
                                id_equipement=equipement,id_service=service,id_type=type)
            datahost.save()
            data={
                'response': 0
            }
            return JsonResponse(data)
       
        
def hostdel(request):
    id= request.POST['id']
    delhost = Host.objects.get(id_host=id)
    delhost.delete()
    data={
        'response': 0
    }
    return JsonResponse(data)


def service(request):
    
    match request.method:
        case 'GET':
            dataService = Service.objects.all()  
            context = {
                'dataService':dataService,             
            }
            
            template = loader.get_template("sup/service.html")            
            return HttpResponse(template.render(context,request))
        
        case 'POST':
            id=randint(0,999999999999)
            nomservice= request.POST['nomservice']
            emailservice=request.POST['emailservice']
            direction=request.POST['direction']
            
            dataservice=Service.objects.create(id_service=id,libelle_service=nomservice,email_service=emailservice,dept_service=direction)
            dataservice.save()
            data={
                'response': 0
            }
            return JsonResponse(data)

def servicedel(request):
    id= request.POST['id']
    delservice = Service.objects.get(id_service=id)
    delservice.delete()
    data={
        'response': 0
    }
    return JsonResponse(data)
        
        
def equipement(request):
    
    match request.method:
        case 'GET':
            dataEquipement = Equipement.objects.all()  
            context = {
                'dataEquipement':dataEquipement,             
            }
            
            template = loader.get_template("sup/equipement.html")            
            return HttpResponse(template.render(context,request))
        
        case 'POST':
            id=randint(0,999999999999)
            nomservice= request.POST['nomservice']
            emailservice=request.POST['emailservice']
            direction=request.POST['direction']
            
            dataequipement=Service.objects.create(id_service=id,libelle_service=nomservice,email_service=emailservice,dept_service=direction)
            dataequipement.save()
            data={
                'response': 0
            }
            return JsonResponse(data)

def equipementdel(request):
    id= request.POST['id']
    delequipement = Equipement.objects.get(id_equipement=id)
    delequipement.delete()
    data={
        'response': 0
    }
    return JsonResponse(data)



#def vueHostAll():
#    with connection.cursor() as cursor:
#        cursor.execute("SELECT * FROM v_host WHERE")
#       row = cursor.fetchone()

#    return row ##



def user(request):
    match request.method:
        case 'GET':
            userAll = User.objects.all()
            privilegeAll = Privilege.objects.all()
            
            context = {
                'userAll': userAll,
                'privilegeAll':privilegeAll,  
            }
            template= loader.get_template("sup/user.html")
            return HttpResponse(template.render(context,request))
        case 'POST':
            id=randint(0,999999999999)
            status ='Y'
            nom= request.POST['nom']
            prenom=request.POST['prenom']
            user=request.POST['user']
            password = request.POST['passuser']
            privilege = request.POST['privilege']
            creation_date=datetime.date.today()
            last_connect=datetime.date.today()
            datauser =User.objects.create(id_user=id,nom=nom,prenom=prenom,user=user,password=password,last_connect=last_connect,
                                status=status,creation_date=creation_date,id_privilege=privilege)
            datauser.save()
            data={
                'response': 0
            }
            return JsonResponse(data)
        
def userdel(request):
    id= request.POST['id']
    userdel = User.objects.get(id_user=id)
    userdel.delete()
    data={
        'response': 0
    }
    return JsonResponse(data)

from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.template import loader
from random import randint
from django.views.decorators.csrf import csrf_protect
from .models import Host,Type,Equipement,Service
import sweetify

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
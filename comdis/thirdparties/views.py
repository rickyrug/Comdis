from django.shortcuts import render, HttpResponse, HttpResponseRedirect,redirect
from django.core.serializers import serialize
from django.utils.timezone import now
from .models import Client, Supplier

# Create your views here.

def index(request):
    clientList = Client.objects.all()
    suppliersList = Supplier.objects.all()

    dataClients = serialize("json",clientList)
    dataSupplier = serialize("json",suppliersList)


    context = {
        "clientList"    :dataClients
        ,"supplierList" :dataSupplier
    }
    return render(request,"thirdparties/index.html",context)

def upsertClients(request,id_client= None):
    context = {}
    return render(request,'thirdparties/upsertClient.html',context)

def upsertSupplier(request,id_supplier= None):
    context = {}
    return render(request,'thirdparties/upsertSupplier.html',context)

def deleteclient(request,id_client=None):
    return redirect("indexthirdparties")

def deletesupplier(request,id_supplier=None):
    return redirect("indexthirdparties")
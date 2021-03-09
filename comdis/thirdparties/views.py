from django.shortcuts           import render, HttpResponse, HttpResponseRedirect,redirect
from django.core.serializers    import serialize
from django.utils.timezone      import now
from .models                    import Client, Supplier
from .forms                     import CustomerForm

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
    initdata = {}

    if request.method == 'POST':
        form = CustomerForm(request.POST)

        if form.is_valid():
            var_Name    =  form.cleaned_data['Name']
            var_City    = form.cleaned_data['City']
            var_Country = form.cleaned_data['Country']
            var_RFC     = form.cleaned_data['RFC']
            var_ZipCode = form.cleaned_data['ZipCode']
            var_Address = form.cleaned_data['Address']
            var_Phone1  = form.cleaned_data['Phone1']
            var_Phone2  = form.cleaned_data['Phone2']
            var_idCustomer = form.cleaned_data['idCustomer']

            if not var_idCustomer:
                Client.objects.create(
                    Address= var_Address
                    ,Name= var_Name
                    ,Country= var_Country
                    ,City=  var_City
                    , ZipCode=var_ZipCode
                    ,RFC = var_RFC
                    ,Phone1= var_Phone1
                    ,Phone2 = var_Phone2
                )
            else:
                updateCustomer = Client.objects.get(pk = var_idCustomer)
                updateCustomer.Address = var_Address
                updateCustomer.Name    = var_Name
                updateCustomer.Country = var_Country
                updateCustomer.City    = var_City
                updateCustomer.ZipCode = var_ZipCode
                updateCustomer.RFC     = var_RFC
                updateCustomer.Phone1  = var_Phone1
                updateCustomer.Phone2   = var_Phone2
                #missing auditory fields update updateby
                updateCustomer.save()
            return redirect("indexthirdparties") 

    else:

        if id_client:
            customer = Client.objects.get(pk = id_client)
            initdata = {
                 "Name": customer.Name
                ,"City":customer.City
                ,"Country":customer.Country
                ,"RFC":customer.RFC
                ,"ZipCode":customer.ZipCode
                ,"Address":customer.Address
                ,"Phone1":customer.Phone1
                ,"Phone2":customer.Phone2
                ,"idCustomer":customer.pk

            }
            form = CustomerForm(initdata)
        else:
            form = CustomerForm()

    context = {
        "form":form
    }
    return render(request,'thirdparties/upsertClient.html',context)

def upsertSupplier(request,id_supplier= None):
    initdata = {}

   

    context = {}
    return render(request,'thirdparties/upsertSupplier.html',context)

def deleteclient(request,id_client=None):
    if id_client:
        deletedClient = Client.objects.get(pk=id_client)
        deletedClient.delete()
    return redirect("indexthirdparties")

def deletesupplier(request,id_supplier=None):
    return redirect("indexthirdparties")
from django.shortcuts           import render, HttpResponse, HttpResponseRedirect,redirect
from django.core.serializers    import serialize
from django.utils.timezone      import now
from .models                    import Client, Supplier
from .forms                     import CustomerForm, SupplierForm
from main.models                import Country,City

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

            countryObj      =  Country.objects.get(pk=var_Country)
            cityObj         =  City.objects.get(pk=var_City)

            if not var_idCustomer:
                Client.objects.create(
                    Address= var_Address
                    ,Name= var_Name
                    ,Country= countryObj
                    ,City=  cityObj
                    , ZipCode=var_ZipCode
                    ,RFC = var_RFC
                    ,Phone1= var_Phone1
                    ,Phone2 = var_Phone2
                )
            else:
                updateCustomer = Client.objects.get(pk = var_idCustomer)
                updateCustomer.Address = var_Address
                updateCustomer.Name    = var_Name
                updateCustomer.Country = countryObj
                updateCustomer.City    = cityObj
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
                ,"City":customer.City.pk
                ,"Country":customer.Country.pk
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

    if request.method == 'POST':
        form = SupplierForm(request.POST)

        if form.is_valid():
            var_Name        =  form.cleaned_data['Name']
            var_City        = form.cleaned_data['City']
            var_Country     = form.cleaned_data['Country']
            var_RFC         = form.cleaned_data['RFC']
            var_ZipCode     = form.cleaned_data['ZipCode']
            var_Address     = form.cleaned_data['Address']
            var_Phone1      = form.cleaned_data['Phone1']
            var_Phone2      = form.cleaned_data['Phone2']
            var_idSupplier  = form.cleaned_data['idSupplier']

            countryObj      =  Country.objects.get(pk=var_Country)
            cityObj         =  City.objects.get(pk=var_City)

            if not var_idSupplier:
                Supplier.objects.create(
                    Address = var_Address
                    ,Name   = var_Name
                    ,Country= countryObj
                    ,City   =  cityObj
                    ,ZipCode=var_ZipCode
                    ,RFC    = var_RFC
                    ,Phone1 = var_Phone1
                    ,Phone2 = var_Phone2
                )
            else:
                updateSupplier = Supplier.objects.get(pk = var_idSupplier)
                updateSupplier.Address = var_Address
                updateSupplier.Name    = var_Name
                updateSupplier.Country = countryObj
                updateSupplier.City    = cityObj
                updateSupplier.ZipCode = var_ZipCode
                updateSupplier.RFC     = var_RFC
                updateSupplier.Phone1  = var_Phone1
                updateSupplier.Phone2   = var_Phone2
                #missing auditory fields update updateby
                updateSupplier.save()
            return redirect("indexthirdparties") 

    else:

        if id_supplier:
            supplier = Supplier.objects.get(pk = id_supplier)
            initdata = {
                 "Name": supplier.Name
                ,"City":supplier.City.pk
                ,"Country":supplier.Country.pk
                ,"RFC":supplier.RFC
                ,"ZipCode":supplier.ZipCode
                ,"Address":supplier.Address
                ,"Phone1":supplier.Phone1
                ,"Phone2":supplier.Phone2
                ,"idSupplier":supplier.pk

            }
            form = SupplierForm(initdata)
        else:
            form = SupplierForm()

    context = {
        "form":form
    }
    return render(request,'thirdparties/upsertSupplier.html',context)

def deleteclient(request,id_client=None):
    if id_client:
        deletedClient = Client.objects.get(pk=id_client)
        deletedClient.delete()
    return redirect("indexthirdparties")

def deletesupplier(request,id_supplier=None):
    if id_supplier:
        deleteSupplier = Supplier.objects.get(pk=id_supplier)
        deleteSupplier.delete()
    return redirect("indexthirdparties")
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.core.serializers import serialize
from django.utils.timezone import now
from .modelsDefinition.ProductModel import Product
from .formsDefinitions.productFormDefinition import ProductForm


# Create your views here.

def index(request):
    context = {}
    return render(request,"main/index/index.html",context)

def products(request):
    productList = Product.objects.all()
    
    data = serialize("json",productList)
    context = {"productList":data}
    return render(request,"main/products/index.html",context)

def upsertProducts(request,id_product= None):
    
    initdata = {}

    if request.method == 'POST':

        form = ProductForm(request.POST)
       

        if form.is_valid():
            
        

       
            id_product      = form.cleaned_data['idProduct']
            name            = form.cleaned_data['Name']
            classification  = form.cleaned_data['Classification']
            uom             = form.cleaned_data['Uom']

            if not id_product:
                Product.objects.create(
                        Uom = uom
                    ,   Classification= classification
                    ,   Name = name
                )
            else:
                updatedProduct                  = Product.objects.get(pk = id_product)
                updatedProduct.Uom              = uom
                updatedProduct.Classification   = classification
                updatedProduct.Name             = name
                updatedProduct.Updated          = now
                updatedProduct.UpdatedBy        = 'SERVER'
                updatedProduct.save()

            return HttpResponseRedirect("products")        

    else:
        if id_product != None:
            product = Product.objects.get(pk = id_product)
            initialData = {
                    "Name"            : product.Name
                ,   "Classification"  : product.Classification.pk
                ,   "Uom"             : product.Uom.pk
                ,   "idProduct"       : product.pk
            }
            form = ProductForm(initialData)
        else:   
            form = ProductForm()
    


    context = {
         "idProduct":id_product
        ,"form": form
    }
    return render(request,"main/products/upsert.html",context)
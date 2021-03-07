from django.shortcuts import render
from django.core.serializers import serialize
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
    form = ProductForm()
    context = {
         "idProduct":id_product
        ,"form": form
    }
    return render(request,"main/products/upsert.html",context)
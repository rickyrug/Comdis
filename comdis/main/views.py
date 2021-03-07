from django.shortcuts import render, HttpResponse, HttpResponseRedirect,redirect
from django.core.serializers import serialize
from django.utils.timezone import now

from .formsDefinitions.productFormDefinition import ProductForm
from .modelsDefinition.UomModel import Uom
from .modelsDefinition.ClassificationModel import Classification


# Create your views here.

def index(request):
    context = {}
    return render(request,"main/index/index.html",context)


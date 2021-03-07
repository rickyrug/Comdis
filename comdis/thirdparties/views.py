from django.shortcuts import render, HttpResponse, HttpResponseRedirect,redirect
from django.core.serializers import serialize
from django.utils.timezone import now

# Create your views here.

def index(request):
    context = {}
    return render(request,"thirdparties/index.html",context)
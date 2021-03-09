from django import forms
from main.models import Country, City

def getContries():
    items = Country.objects.values_list('id','Name')
    choices = tuple([(u'', '-----')] + list(items))
    return choices

def getCities():
    items = City.objects.values_list('id','Name')
    choices = tuple([(u'', '-----')] + list(items))
    return choices


class CustomerForm(forms.Form):
    Name        = forms.CharField(label     ="Nombre: ", max_length=255, required=True)
    City        = forms.ChoiceField(label   = "Ciudad: ", choices=getCities() ,required=True)
    Country     = forms.ChoiceField(label   = "País: ", choices=getContries() ,required=True)
    RFC         = forms.CharField(label     ="RFC: ", max_length=255, required=True)
    ZipCode     = forms.CharField(label     ="ZipCode: ", max_length=255, required=False)
    Address     = forms.CharField(label="Dirección: ", max_length=255, required=False)
    Phone1      = forms.CharField(label="Telefono1: ", max_length=25, required=False)
    Phone2      = forms.CharField(label="Telefono2: ", max_length=25, required=False)
    idCustomer  = forms.CharField(widget=forms.HiddenInput, required=False)

class SupplierForm(forms.Form):
    Name        = forms.CharField(label="Nombre: ", max_length=255, required=True)
    City        = forms.ChoiceField(label= "Ciudad: ", choices=getCities() ,required=True)
    Country     = forms.ChoiceField(label= "País: ", choices=getContries() ,required=True)
    RFC         = forms.CharField(label="RFC: ", max_length=255, required=True)
    ZipCode     = forms.CharField(label="ZipCode: ", max_length=255, required=False)
    Address     = forms.CharField(label="Dirección: ", max_length=255, required=False)
    Phone1      = forms.CharField(label="Telefono1: ", max_length=25, required=False)
    Phone2      = forms.CharField(label="Telefono2: ", max_length=25, required=False)
    idSupplier  = forms.CharField(widget=forms.HiddenInput, required=False)

class ClientContact(forms.Form):
    Name        = forms.CharField(label="Nombre: ", max_length=255, required=True)
    Phone       = forms.CharField(label="Teléfono: ", max_length=25, required=True)
    Email       = forms.CharField(label="Mail: ", max_length=255, required=True)
    idCliente   = forms.CharField(widget=forms.HiddenInput, required=False)


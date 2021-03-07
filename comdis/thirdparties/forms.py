from django import forms

class CustomerForm(forms.Form):
    Name        = forms.CharField(label="Nombre: ", max_length=255, required=True)
    City        = forms.CharField(label="Ciudad: ", max_length=255, required=True)
    Country     = forms.CharField(label="País: ", max_length=255, required=True)
    RFC         = forms.CharField(label="RFC: ", max_length=255, required=True)
    ZipCode     = forms.CharField(label="ZipCode: ", max_length=255, required=False)
    Address     = forms.CharField(label="Dirección: ", max_length=255, required=False)
    Phone1      = forms.CharField(label="Telefono1: ", max_length=25, required=False)
    Phone2      = forms.CharField(label="Telefono2: ", max_length=25, required=False)
    idCustomer  = forms.CharField(widget=forms.HiddenInput, required=False)

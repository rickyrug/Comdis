from django import forms
from ..modelsDefinition.ClassificationModel import Classification
from ..modelsDefinition.UomModel            import Uom

class ProductForm(forms.Form):
    def getClassChoises():
        items = Classification.objects.values_list('id','Name')
        choices = tuple([(u'', '-----')] + list(items))
        return choices
    
    def getUomChoises():
        items = Uom.objects.values_list('id','Name')
        choices = tuple([(u'', '-----')] + list(items))        
        return choices
    
    ClassificationChoises = getClassChoises()
    UomChoises = getUomChoises()

    #Name           = forms.TextInput(attrs={'class':'form-control','required':True})
    Name            = forms.CharField(label="Nombre: ", max_length=255, required=True)
    Classification  = forms.ChoiceField(label= "Clasificación: ", choices=ClassificationChoises)
    Uom             = forms.ChoiceField(label = "Unidad de medida: ", choices=UomChoises)
    idProduct       = forms.CharField(widget=forms.HiddenInput, required=False)

    
   

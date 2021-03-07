from django.contrib import admin
from .modelsDefinition.UomModel import Uom
from .modelsDefinition.ClassificationModel import Classification
from .modelsDefinition.BankModel import Bank

# Register your models here.

# class UomAdmin(admin.ModelAdmin):
#     fields = ('name', 'code')

admin.site.register(Uom)
admin.site.register(Classification)
admin.site.register(Bank)

from django.contrib import admin
from .models import Client
from .models import Supplier
# Register your models here.

admin.site.register(Client)
admin.site.register(Supplier)
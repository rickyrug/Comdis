from django.db import models
from django.utils.timezone import now
from main.models import Country, City

class Client(models.Model):
    id = models.BigAutoField(primary_key=True)  # Add this line
    Name    = models.CharField(max_length=255,null=False)
    Country = models.ForeignKey(Country, on_delete= models.DO_NOTHING)
    City    = models.ForeignKey(City,on_delete=models.DO_NOTHING)
    ZipCode = models.CharField(max_length=255,null=False)
    RFC     = models.CharField(max_length=255,null=False)
    Address = models.CharField(max_length=255,null=False)
    Phone1  = models.CharField(max_length=25,null=True)
    Phone2  = models.CharField(max_length=25,null=True)


    Created = models.DateTimeField(null= False,default=now)
    CreatedBy = models.CharField(max_length=50, null= False,default='SERVER')
    Updated = models.DateTimeField(null= True,default=now)
    UpdatedBy = models.CharField(max_length=50, null= True,default='SERVER')

    def __str__(self):
        return self.Name

    class Meta:
        db_table = 'Client'

class Supplier(models.Model):
    id = models.BigAutoField(primary_key=True)  # Add this line
    Name = models.CharField(max_length=255,null=False)
    Country = models.ForeignKey(Country, on_delete= models.DO_NOTHING)
    City    = models.ForeignKey(City,on_delete=models.DO_NOTHING)
    ZipCode = models.CharField(max_length=255,null=False)
    RFC     = models.CharField(max_length=255,null=False)
    Address = models.CharField(max_length=255,null=False)
    Phone1  = models.CharField(max_length=25,null=True)
    Phone2  = models.CharField(max_length=25,null=True)

    Created = models.DateTimeField(null= False,default=now)
    CreatedBy = models.CharField(max_length=50, null= False,default='SERVER')
    Updated = models.DateTimeField(null= True,default=now)
    UpdatedBy = models.CharField(max_length=50, null= True,default='SERVER')

    def __str__(self):
        return self.Name
    
    class Meta:
        db_table = 'Supplier'

class ClientContact(models.Model):
    id = models.BigAutoField(primary_key=True)  # Add this line
    idCliente = models.ForeignKey(Client,on_delete=models.DO_NOTHING)
    Name      = models.CharField(max_length=255,null=False)
    Phone     = models.CharField(max_length=25,null=False)
    Email     = models.CharField(max_length=255,null=False, default="")

    Created = models.DateTimeField(null= False,default=now)
    CreatedBy = models.CharField(max_length=50, null= False,default='SERVER')
    Updated = models.DateTimeField(null= True,default=now)
    UpdatedBy = models.CharField(max_length=50, null= True,default='SERVER')

    def __str__(self):
        return self.Name
    
    class Meta:
        db_table = 'ClientContact'
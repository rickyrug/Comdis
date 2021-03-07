from django.db import models
from django.utils.timezone import now

class Client(models.Model):
    Name    = models.CharField(max_length=255,null=False)
    Country = models.CharField(max_length=255,null=False)
    City    = models.CharField(max_length=255,null=False)
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
    Name = models.CharField(max_length=255,null=False)
    Country = models.CharField(max_length=255,null=False)
    City    = models.CharField(max_length=255,null=False)
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
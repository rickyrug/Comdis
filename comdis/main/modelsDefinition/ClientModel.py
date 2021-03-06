from django.db import models

class Client(models.Model):
    Name    = models.CharField(max_length=255,null=False)
    Country = models.CharField(max_length=255,null=False)
    City    = models.CharField(max_length=255,null=False)
    ZipCode = models.CharField(max_length=255,null=False)
    RFC     = models.CharField(max_length=255,null=False)
    Address = models.CharField(max_length=255,null=False)
    Created = models.DateTimeField(null= False)
    CreatedBy = models.CharField(max_length=50, null= False)
    Updated = models.DateTimeField(null= False)
    UpdatedBy = models.CharField(max_length=50, null= False)

    class Meta:
        db_table = 'Client'
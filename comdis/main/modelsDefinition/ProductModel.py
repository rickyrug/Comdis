from django.db import models
from django.utils.timezone import now
from .UomModel import Uom
from .ClassificationModel import Classification


class Product(models.Model):
    Name = models.CharField(max_length=255,null=False)
    Uom  = models.ForeignKey(Uom, on_delete=models.DO_NOTHING)
    Classification = models.ForeignKey(Classification, on_delete=models.DO_NOTHING)
    


    Created = models.DateTimeField(null= False,default=now)
    CreatedBy = models.CharField(max_length=50, null= False,default='SERVER')
    Updated = models.DateTimeField(null= True,default=now)
    UpdatedBy = models.CharField(max_length=50, null= True,default='SERVER')

    def __str__(self):
        return self.Name

    class Meta:
        db_table = 'Product'
from django.db import models
from django.utils.timezone import now

class Bank(models.Model):
    Name =  models.CharField(max_length=255,null=False) 
    Code =  models.CharField(max_length=3,null=False) 

    Created = models.DateTimeField(null= False,default=now)
    CreatedBy = models.CharField(max_length=50, null= False,default='SERVER')
    Updated = models.DateTimeField(null= True,default=now)
    UpdatedBy = models.CharField(max_length=50, null= True,default='SERVER')

    def __str__(self):
        return self.Name

    class Meta:
        db_table = 'Bank'

from django.db              import models
from django.utils.timezone  import now
from main.models            import Classification
from main.models            import Uom
# Create your models here.

class Product(models.Model):
    id = models.BigAutoField(primary_key=True)  # Add this line
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

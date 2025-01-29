from django.db import models # type: ignore

# Create your models here.
class Product(models.Model):
    product_id = models.IntegerField(primary_key=True)
    product_name = models.CharField(max_length=200)
    product_price = models.FloatField()
    product_quantity = models.IntegerField()

    def __str__(self):
        return self.product_name

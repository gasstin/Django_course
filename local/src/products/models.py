from django.db import models

# Create your models here.
class Products(models.Model):
    title       =  models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=100)
    summary = models.TextField(default='This a test summary')
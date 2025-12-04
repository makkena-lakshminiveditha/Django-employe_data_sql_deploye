from django.db import models

# Create your models here.
class employe_model(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=10,decimal_places=2)
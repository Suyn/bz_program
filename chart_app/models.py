from django.db import models

# Create your models here.
class City(models.Model):
    city = models.CharField(max_length=20)
    num = models.CharField(max_length=20)
    class Meta:
        db_table = 'city'
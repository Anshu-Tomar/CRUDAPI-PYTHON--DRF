from django.db import models

# Create your models here.
class employee(models.Model):
    firstName = models.CharField(max_length=10)
    lastName = models.CharField(max_length=10)
    empid = models.IntegerField()

def _str_(self):
    return self.firstName

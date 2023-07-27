from django.db import models

# Create your models here.

class Request(models.Model):
    educatorType = models.CharField(max_length=20)
    educatorId = models.IntegerField()
    educatorName = models.CharField(max_length=30)
    parentId = models.IntegerField()
    parentName = models.CharField(max_length=30)

class Deals(models.Model):
    educatorType = models.CharField(max_length=20)
    educatorId = models.IntegerField()
    educatorName = models.CharField(max_length=30)
    parentId = models.IntegerField()
    parentName = models.CharField(max_length=30)
    

class services(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, unique=True)
    image = models.ImageField(upload_to='pics')
    description = models.TextField(default='')
    cost = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)

    def __str__(self):
        return (self.name)


class feedback(models.Model):
    Name = models.CharField(max_length=250)
    Surname = models.CharField(max_length=250)
    Email = models.EmailField(max_length=250)
    Comment = models.TextField(max_length=450)
    



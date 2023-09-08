from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Items(models.Model):
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=1000,default="image_link")
    number = models.IntegerField(max_length=50,default=0)
    link = models.CharField(unique=True, max_length=200)
    SearchableFields= ['name'] 

    def __str__(self):
        return self.name
    

class Waste(models.Model):
    link = models.ForeignKey(Items,on_delete=models.CASCADE)
    wname = models.CharField(max_length=100)
    wpic = models.CharField(max_length=200)
    wpre = models.CharField(max_length=250)
    wrecipe = models.IntegerField(max_length=50,default=0)

    def __str__(self) :
        return self.wname
    
    def __iter__(self):
        return [ self.wname, 
            self.wpic, 
            self.wpre, 
            self.wrecipe] 
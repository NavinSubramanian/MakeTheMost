from django.db import models
from django.conf import settings
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
    
class RecipeList(models.Model):
    wname = models.ForeignKey(Waste,on_delete=models.CASCADE)
    itemlink = models.CharField(max_length=100,default="item_link")
    recipename = models.CharField(max_length=100)
    recipetime = models.IntegerField(max_length=50, default=0)
    resdesc = models.CharField(max_length=1000,default="description")
    recipeimg = models.CharField(max_length=500,default="image_url")
    recipelink = models.CharField(max_length=200)

    def __str__(self):
        return self.recipename

    def __iter__(self):
        return [
            self.itemlink,
            self.recipename,
            self.resdesc,
            self.recipe,
            self.recipelink
        ]
    
class RecipeDetail(models.Model):
    recipename = models.ForeignKey(RecipeList,on_delete=models.CASCADE)
    recipedesc = models.CharField(max_length=1000)
    recipeimage = models.CharField(max_length=500,default="image_url")
    recipeingrediants = models.CharField(max_length=500)
    recipesteps = models.CharField(max_length=1000)

    def __str__(self):
        return self.recipedesc

    def __iter__(self):
        return [
            self.recipedesc,
            self.recipeimage,
            self.recipeingrediants,
            self.recipesteps
        ]
    
class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=0)
    recipename =  models.ForeignKey(RecipeList, related_name="comments", on_delete=models.CASCADE)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    title = models.CharField(max_length=50)
    pub_date = models.TimeField(auto_now=False, auto_now_add=False)
    body = models.TextField()
    image = models.ImageField(upload_to = 'images/', height_field=None, width_field=None, max_length=None)
    icon  = models.ImageField(upload_to= 'images/', height_field=None, width_field=None, max_length=None)
    url = models.CharField(max_length=50)
    votes = models.IntegerField(default = 1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    
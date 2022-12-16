from django.db import models

class Question(models.Model):
    text = models.CharField(max_length=200)

class Product(models.Model):
    name = models.CharField(max_length=200)
    img_url = models.URLField(  default='https://images.unsplash.com/photo-1671036089231-a56464fdaadd?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHw0fHx8ZW58MHx8fHw%3D&auto=format&fit=crop&w=500&q=60')
    price = models.FloatField()
    quantity = models.IntegerField()
      # with their title name
    def __str__(self):
        return self.name
    
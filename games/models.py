from tkinter import CASCADE
from django.db import models
from django.contrib.auth import get_user_model
class Game(models.Model):
    title=models.CharField(max_length=50)
    description= models.TextField()
    owner=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    slug=models.SlugField(unique=True)
    price=models.DecimalField(max_digits=6,decimal_places=2)
    created=models.DateTimeField(auto_now=True)
    updated=models.DateTimeField(auto_now=True)
    image=models.ImageField(blank=True)
    def __str__(self) :
        return f'{self.title}'

# Create your models here.

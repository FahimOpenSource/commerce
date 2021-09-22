from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class AuctionListing(models.Model):
    title = models.CharField(max_length=20)
    url = models.URLField(max_length=500, blank=True)
    description = models.TextField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=20)
    Auction = models.ManyToManyField(AuctionListing, blank=True, related_name='category')

    def __str__(self):
         return self.name
'''
class Comment(models.Model):
'''

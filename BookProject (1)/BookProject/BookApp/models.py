from django.db import models

# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    year_of_establishment = models.DateField()

class Book(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=100)
    page_number = models.IntegerField()
    isbn = models.CharField(max_length=100)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    dimensions = models.CharField(max_length=100)
    year_of_publication = models.IntegerField()
    cover_type = [
        ("h","hardCover"),
        ("s","softCover"),
    ]
    cover = models.CharField(choices=cover_type,max_length=2)
    category_type = [
        ("r","Romance"),
        ("t","Thriller"),
        ("k","Classic"),
        ("d","Drama"),
        ("h","History"),
    ]
    price = models.IntegerField()
    category = models.CharField(choices=category_type,max_length=2)

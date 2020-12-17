from django.db import models


class Measure(models.Model):
    type = models.CharField(max_length=50)

class Store(models.Model):
    pass

class Manufacture(models.Model):
    pass

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=16, decimal_places=2)
    measure = models.ForeignKey(Measure, on_delete=models.CASCADE)
    is_sale = models.BooleanField()
    sale_price = models.DecimalField(max_digits=16, decimal_places=2)
    qty = models.IntegerField()
    img = models.ImageField(default='not_found.jpg')



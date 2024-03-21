from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    stock = models.IntegerField()
    # image = models.ImageField(upload_to='product_images', blank=True)

    def __str__(self):
        return self.name

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    comment = models.TextField()
    author = models.CharField(max_length=255)
    rating = models.IntegerField()

def __str__(self):
    return f"{self.Product.name} - {self.author} - {self.rating}"


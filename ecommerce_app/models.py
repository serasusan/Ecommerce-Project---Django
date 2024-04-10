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
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)    

        def __str__(self):
            return self.name
        
        class Meta:
            ordering = ['-updated_at']

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    comment = models.TextField()
    author = models.CharField(max_length=255)
    rating = models.IntegerField()

def __str__(self):
    return f"{self.Product.name} - {self.author} - {self.rating}"


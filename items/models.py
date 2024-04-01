from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.TextField(max_length=150)
    description = models.TextField()
    product_Img = models.ImageField(null=True,blank=True,upload_to='images/')

    

    def __str__(self):
        return self.name

from django.db import models

# Create your models here.
class category(models.Model):
    category_name = models.CharField(max_length = 50)
    description = models.CharField(max_length= 100)
    
class product(models.Model):
    title = models.CharField(max_length=50)
    price = models.FloatField()
    discounted_price = models.FloatField()
    image = models.CharField(max_length=400)
    p_category = models.ForeignKey(category, related_name='products', on_delete = models.CASCADE)
    
class review(models.Model):
    product = models.ForeignKey(product, related_name = 'reviews', on_delete = models.CASCADE)
    customer_review = models.TextField()
    rating = models.FloatField()
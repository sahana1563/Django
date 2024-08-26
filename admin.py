from django.contrib import admin
from .models import category, product, review
# Register your models here.

admin.site.register(category)
admin.site.register(product)
admin.site.register(review)
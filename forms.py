from django import forms
from .models import product, category, review

class ProductForm(forms.ModelForm):
    class Meta:
        model = product
        fields = '__all__'

class CategoryForm(forms.ModelForm):
    class Meta:
        model = category
        fields = '__all__'

class ReviewsForm(forms.ModelForm):
    class Meta:
        model = review
        fields = '__all__'
from django import forms
from app import models

class ItemForm(forms.ModelForm):
    class Meta:
        model = models.Item
        fields = ['name', 'description']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = models.Category
        fields = ['categoria']

class AuthorForm(forms.ModelForm):
    class Meta:
        model = models.Author
        fields = ['name', 'description']

from django.contrib import admin
from .models import Category, Good, BlogArticle

admin.register(Category)
admin.register(Good)
admin.register(BlogArticle)
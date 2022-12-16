from django.contrib import admin

from .models import Question
from .models import Product


class QuestionAdmin(admin.ModelAdmin):
    fields = ['text']

class ProductAdmin(admin.ModelAdmin):
    fields = ['name','price','quantity', 'img_url']
    

admin.site.register(Question)
admin.site.register(Product)
# Register your models here.

from django.contrib import admin

# Register your models here.
from . models import Cetegory, Product


@admin.register(Cetegory)
class CetegoryAdmin(admin.ModelAdmin):

    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
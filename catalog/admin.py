from django.contrib import admin

from catalog.models import Category, Product, Version


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category', 'preview')
    list_filter = ('category',)
    search_fields = ('name', 'description')

@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('product', 'version_number', 'version_name', 'is_active')
    list_filter = ('product',)
    search_fields = ('version_number', 'version_name',)



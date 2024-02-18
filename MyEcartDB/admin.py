from django.contrib import admin

from .models import CategoryTable, ProductImagesTable, ProductsTable, SpecialOffersTable

# Register your models here.


admin.site.register(ProductsTable)
admin.site.register(CategoryTable)
admin.site.register(SpecialOffersTable)
admin.site.register(ProductImagesTable)
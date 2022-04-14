from django.contrib import admin
from .models import Product,Image,Category,Product_alternative,Product_accessor,Brand,Variant,FavoriteProduct
# Register your models here. 
admin.site.register(Product)
admin.site.register(Image)
admin.site.register(Category) 
admin.site.register(Product_alternative) 
admin.site.register(Product_accessor) 
admin.site.register(Brand) 
admin.site.register(Variant) 
admin.site.register(FavoriteProduct) 
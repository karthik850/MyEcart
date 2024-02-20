from django.db import models
from django.contrib.auth.models import User



class CategoryTable(models.Model):
    categoryName = models.CharField(max_length=100);
    categoryImageUrl = models.URLField(blank=True)
    def __str__(self):
        return self.categoryName

#holds all subcription details
class ProductsTable(models.Model):
    productName = models.CharField(max_length=100);
    productDescription = models.TextField(null=True)
    productInStock = models.BooleanField(default=True)
    productAmount = models.FloatField()
    productDiscount = models.FloatField(null=True,blank=True) 
    productCategory = models.ForeignKey(CategoryTable, related_name="productCategory", on_delete=models.CASCADE,default=1)
    producImageUrl = models.URLField(blank=True)
    

    def __str__(self):
        return self.productName

class SpecialOffersTable(models.Model):
    specialOffersName = models.CharField(max_length=100);
    specialOffersDescription = models.TextField(null=True)
    productInStock = models.BooleanField(default=True)
    productAmount = models.FloatField()
    productDiscount = models.FloatField(null=True,blank=True) 
    specialOffersCategory = models.ForeignKey(CategoryTable, related_name="specialOffersCategory", on_delete=models.CASCADE,default=1)
    specialOffersImageUrl = models.URLField(blank=True)
    

    def __str__(self):
        return self.specialOffersName
    
class ProductImagesTable(models.Model):
    productName = models.ForeignKey(ProductsTable, related_name="productDetails", on_delete=models.CASCADE,default=1)
    imageUrl = models.URLField(blank=True)


    def __str__(self):
        return self.productName.productName

# class ProductDetailsTable(models.Model):
#     productName = models.ForeignKey(ProductsTable, related_name="productDetails", on_delete=models.CASCADE,default=1)
#     primaryImage = models.URLField(blank=True)
#     secondImage = models.URLField(blank=True)
#     thirdImage = models.URLField(blank=True)
#     fourthImage = models.URLField(blank=True)
#     fifthImage = models.URLField(blank=True)

#     def __str__(self):
#         return self.productName.productName





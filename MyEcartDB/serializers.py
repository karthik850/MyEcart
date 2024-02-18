from rest_framework import serializers
from django.contrib.auth.models import User
import json

from .models import CategoryTable, ProductsTable, SpecialOffersTable, ProductImagesTable

class CategoryDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryTable
        fields = '__all__'

class productImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImagesTable
        fields = '__all__'

class ProductsDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductsTable
        fields = '__all__'
    categoryName = CategoryDataSerializer(many=False, source='productCategory')
    productImage = productImagesSerializer(many= True, source='productDetails' )
    def __init__(self, *args, **kwargs):
        super(ProductsDataSerializer, self).__init__(*args, **kwargs)
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        category_Name = representation.pop('categoryName')
        product_Image = representation.pop('productImage')
        # Convert list of category and concat to product data
        representation['categoryName'] = category_Name
        representation['productImages'] = product_Image
        return representation


class SpecialOffersSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecialOffersTable
        fields = '__all__'

    categoryName = CategoryDataSerializer(many=False, source='specialOffersCategory')
    def __init__(self, *args, **kwargs):
        super(SpecialOffersSerializer, self).__init__(*args, **kwargs)
        # # Exclude the field you want to exclude
        # excluded_field = 'selectedPlan'  
        # if excluded_field in self.fields:
        #     del self.fields[excluded_field]
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        category_Name = representation.pop('categoryName')
        # Convert list of benefits and concat to subscription data
        representation['categoryName'] = category_Name
        return representation
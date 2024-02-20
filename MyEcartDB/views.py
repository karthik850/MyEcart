from rest_framework import generics,status

from .models import ProductsTable, CategoryTable, SpecialOffersTable
from .serializers import  CategoryDataSerializer, ProductsDataSerializer, ProductsDetailsSerializer, SpecialOffersSerializer
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

@api_view(["GET"])
def getProductDetails(request):
    query = ""
    try:
        query = request.GET.get("category")
    except:
        pass
    try:
        if(query):
            category = CategoryTable.objects.get(categoryName=query)
            ProductsData = ProductsTable.objects.filter(productCategory = category)
        else:
            ProductsData = ProductsTable.objects.all()
        serializer = ProductsDataSerializer(ProductsData, many=True)
    except:
        return Response({"error":"Failed to return data"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["GET"])
def getProductDetailsForID(request,productID):
    # try:
    ProductsData = ProductsTable.objects.get(id=productID)
    print(ProductsData)
    serializer = ProductsDetailsSerializer(ProductsData, many=False)
    # except:
    #     return Response({"error":"Failed to return data"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def getSpecialOffersDetails(request):
    try:
        SpecialOffersData = SpecialOffersTable.objects.all()
        serializer = SpecialOffersSerializer(SpecialOffersData, many=True)
    except:
        return Response({"error":"Failed to return data"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["GET"])
def getCategorysDetails(request):
    try:
        CategoryData = CategoryTable.objects.all()
        serializer = CategoryDataSerializer(CategoryData, many=True)
    except:
        return Response({"error":"Failed to return data"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["GET"])
def getCategorysDetailsForID(request,categoryID):
    try:
        CategoryData = CategoryTable.objects.get(id=categoryID)
        serializer = CategoryDataSerializer(CategoryData, many=False)
    except:
        return Response({"error":"Failed to return data"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["GET"])
def getCategorysDetailsForQUery(request):
    try:
        query = request.GET.get("category")
        print(query)
        CategoryData = CategoryTable.objects.get(categoryName="Shoes")
        serializer = CategoryDataSerializer(CategoryData, many=False)
    except:
        return Response({"error":"Failed to return data"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return Response(serializer.data, status=status.HTTP_200_OK)

    
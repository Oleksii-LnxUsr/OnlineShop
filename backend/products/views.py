from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from products.models import Product
from products.serializers import ProductSerializer, DetailProductSerializer


class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = DetailProductSerializer
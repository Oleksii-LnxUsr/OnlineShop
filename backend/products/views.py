from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from products.models import Product, Category, Brand, Color, Configuration
from products.serializers import ProductSerializer, DetailProductSerializer
from products.filters import ProductFilter


class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]
    filterset_class = ProductFilter


class ProductDetailView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = DetailProductSerializer
    

class FilterOptionsView(APIView):
    """Based on the selected filters, it returns parameters available for further filtering"""

    def get(self, request, *args, **kwargs):
        selected_category = request.query_params.get("category", None)
        selected_brand = request.query_params.get("brand", None)
        selected_color = request.query_params.get("color", None)

        products = Product.objects.all()

        if selected_category:
            selected_category = selected_category.split(",")
            products = products.filter(category__id__in=selected_category)

        if selected_brand:
            selected_brand = selected_brand.split(",")
            products = products.filter(brand__id__in=selected_brand)

        if selected_color:
            selected_color = selected_color.split(",")
            configurations = Configuration.objects.filter(color__id__in=selected_color)
            products = products.filter(
                id__in=configurations.values_list("product_id", flat=True)
            )

        available_categories = Category.objects.filter(product__in=products).distinct()
        available_brands = Brand.objects.filter(product__in=products).distinct()
        available_colors = Color.objects.filter(
            configuration__product__in=products
        ).distinct()

        response_data = {
            "categories": [
                {"id": cat.id, "name": cat.name} for cat in available_categories
            ],
            "brands": [
                {"id": brand.id, "name": brand.name} for brand in available_brands
            ],
            "colors": [
                {"id": color.id, "name": color.name, "hex_code": color.hex_code}
                for color in available_colors
            ],
        }

        return Response(response_data)

from django.db.models import Prefetch
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from products.models import Product, Configuration
from products.serializers import ProductSerializer, DetailProductSerializer
from products.filters import ProductFilter
from products.services import get_filtered_products, get_available_filters


class ProductListView(ListAPIView):
    """
    API view to retrieve a list of products with related categories, brands,
    configurations, and images.

    This view supports filtering, searching, and ordering of products.
    """
    queryset = (
        Product.objects.all()
        .select_related("category", "brand")
        .prefetch_related(
            Prefetch(
                "configuration_set",
                queryset=Configuration.objects.select_related("color").prefetch_related(
                    "image_set"
                ),
            )
        )
    )
    serializer_class = ProductSerializer
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]
    filterset_class = ProductFilter


class ProductDetailView(RetrieveAPIView):
    """
    API view to retrieve the details of a single product with its related category,
    brand, configurations, and images.
    """
    queryset = (
        Product.objects.all()
        .select_related("category", "brand")
        .prefetch_related("configuration_set__color", "configuration_set__image_set")
    )
    serializer_class = DetailProductSerializer


class FilterOptionsView(APIView):
    """
    API View to get available filters based on the parameters already selected.
    This view accepts a GET request with filter parameters and returns the available
    categories, brands and colors for further filtering.
    """
    def get(self, request, *args, **kwargs):
        # Get selected filter options from a query
        selected_categories = request.query_params.get("category", None)
        selected_brands = request.query_params.get("brand", None)
        selected_colors = request.query_params.get("color", None)

        # Receive products filtered by selected parameters
        products = get_filtered_products(
            selected_categories, selected_brands, selected_colors
        )

        # Get available filters based on filtered products
        response_data = get_available_filters(products)

        return Response(response_data)

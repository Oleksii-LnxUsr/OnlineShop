from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from products.models import Product
from products.serializers import ProductSerializer, DetailProductSerializer
from products.filters import ProductFilter
from products.services import get_filtered_products, get_available_filters


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
        products = get_filtered_products(selected_categories, selected_brands, selected_colors)

        # Get available filters based on filtered products
        response_data = get_available_filters(products)

        return Response(response_data)

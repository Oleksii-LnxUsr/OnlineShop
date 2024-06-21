from django.urls import path
from products.views import ProductListView, ProductDetailView, FilterOptionsView

urlpatterns = [
    path("products/", ProductListView.as_view(), name="product-list"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="product-detail"),
    path("products/filters/", FilterOptionsView.as_view(), name="product-filters"),
]

import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from products.models import Product


@pytest.mark.django_db
def test_product_list_view(product):
    """Test for checking the product list (ProductListView)."""
    client = APIClient()
    response = client.get(reverse("product-list"))

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
    assert response.data[0]["name"] == product.name

@pytest.mark.django_db
def test_product_detail_view(product):
    """Test for checking the product detail view (ProductDetailView)."""
    client = APIClient()
    response = client.get(reverse("product-detail", args=[product.id]))

    assert response.status_code == status.HTTP_200_OK
    assert response.data["name"] == product.name

@pytest.mark.django_db
def test_filter_options_view(client, product):
    """Test to check whether filters are available (FilterOptions View)."""
    response = client.get(reverse("product-filters"))

    assert response.status_code == status.HTTP_200_OK

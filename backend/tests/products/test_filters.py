import pytest
from products.models import Product
from products.filters import ProductFilter
from tests.factories import CategoryFactory, BrandFactory, ProductFactory


@pytest.mark.django_db
def test_product_filter():
    """Test to check product filtration."""
    category1 = CategoryFactory(name="Electronics")
    category2 = CategoryFactory(name="Furniture")
    brand1 = BrandFactory(name="BrandX")
    brand2 = BrandFactory(name="BrandY")
    product1 = ProductFactory(name="Laptop", category=category1, brand=brand1)
    product2 = ProductFactory(name="Table", category=category2, brand=brand2)

    filter_data = {"category": "Electronics"}
    filterset = ProductFilter(filter_data, queryset=Product.objects.all())
    filtered_qs = filterset.qs

    assert len(filtered_qs) == 1
    assert filtered_qs[0].name == "Laptop"

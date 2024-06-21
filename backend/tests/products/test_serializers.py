import pytest
from products.serializers import ProductSerializer, ConfigurationSerializer
from products.models import Product


@pytest.mark.django_db
def test_product_serializer(product, configuration):
    """Test to check the serialization of the Product model."""
    serializer = ProductSerializer(product)
    data = serializer.data

    assert data["name"] == product.name
    assert data["category"]["name"] == product.category.name
    assert data["brand"]["name"] == product.brand.name
    assert len(data["configuration"]) == 1
    assert data["configuration"][0]["color"]["name"] == configuration.color.name

import pytest
from products.models import Product, Configuration


@pytest.mark.django_db
def test_product_creation(product):
    """Test to verify the creation of a Product model instance."""
    assert product.name is not None
    assert isinstance(product, Product)

@pytest.mark.django_db
def test_configuration_creation(configuration):
    """Test to verify the creation of a Configuration model instance."""
    assert configuration.attributes == {"ram": "16GB"}
    assert isinstance(configuration, Configuration)

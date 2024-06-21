import pytest
from products.models import Category, Brand, Color, Product, Configuration, Image
from tests.factories import CategoryFactory, BrandFactory, ColorFactory, ProductFactory, ConfigurationFactory, ImageFactory

@pytest.fixture
def category():
    return CategoryFactory()

@pytest.fixture
def brand():
    return BrandFactory()

@pytest.fixture
def color():
    return ColorFactory()

@pytest.fixture
def product(category, brand):
    return ProductFactory(category=category, brand=brand)

@pytest.fixture
def configuration(product, color):
    return ConfigurationFactory(product=product, color=color)

@pytest.fixture
def image(configuration):
    return ImageFactory(configuration=configuration)

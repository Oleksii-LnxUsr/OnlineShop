import factory
from factory.django import DjangoModelFactory
from products.models import Product, Configuration, Brand, Category, Image, Color


class CategoryFactory(DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Faker("word")


class BrandFactory(DjangoModelFactory):
    class Meta:
        model = Brand

    name = factory.Faker("company")
    logo = factory.django.ImageField(color="blue")


class ColorFactory(DjangoModelFactory):
    class Meta:
        model = Color

    name = factory.Faker("color_name")
    hex_code = factory.Faker("hex_color")


class ProductFactory(DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.Faker("word")
    category = factory.SubFactory(CategoryFactory)
    brand = factory.SubFactory(BrandFactory)


class ConfigurationFactory(DjangoModelFactory):
    class Meta:
        model = Configuration

    product = factory.SubFactory(ProductFactory)
    color = factory.SubFactory(ColorFactory)
    attributes = factory.Dict({"ram": "16GB"})
    quantity = factory.Faker("random_int", min=0, max=100)


class ImageFactory(DjangoModelFactory):
    class Meta:
        model = Image

    configuration = factory.SubFactory(ConfigurationFactory)
    image = factory.django.ImageField(color="blue")

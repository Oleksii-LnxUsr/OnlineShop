from rest_framework import serializers
from .models import Product, Configuration, Image, Brand, Color


# List serializers


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ["id", "image"]


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = "__all__"


class ConfigurationSerializer(serializers.ModelSerializer):
    color = ColorSerializer(read_only=True)
    images = ImageSerializer(many=True, read_only=True, source="image_set")

    class Meta:
        model = Configuration
        fields = ["id", "color", "images"]


class ProductSerializer(serializers.ModelSerializer):
    configuration = ConfigurationSerializer(
        many=True, read_only=True, source="configuration_set"
    )

    class Meta:
        model = Product
        fields = ["id", "name", "category", "brand", "configuration"]
        depth = 2


# Retrive serializers


class DetailConfigurationSerializer(serializers.ModelSerializer):
    color = ColorSerializer(read_only=True)
    images = ImageSerializer(many=True, read_only=True, source="image_set")

    class Meta:
        model = Configuration
        fields = ["id", "color", "images", "attributes"]


class DetailProductSerializer(serializers.ModelSerializer):
    configuration = DetailConfigurationSerializer(
        many=True, read_only=True, source="configuration_set"
    )

    class Meta:
        model = Product
        fields = ["id", "name", "category", "brand", "configuration"]
        depth = 2

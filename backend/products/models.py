from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey("Category", on_delete=models.PROTECT)
    brand = models.ForeignKey("Brand", on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "product"


class Configuration(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    color = models.ForeignKey("Color", on_delete=models.PROTECT)
    attributes = models.JSONField()

    def __str__(self):
        return f"{self.product.name} | {self.color.name}"

    class Meta:
        db_table = "configuration"


class Color(models.Model):
    name = models.CharField(max_length=50)
    hex_code = models.CharField(max_length=7)

    def __str__(self):
        return f"{self.name} | {self.hex_code}"

    class Meta:
        db_table = "color"


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "category"


class Brand(models.Model):
    name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to="media/logos")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "brand"


class Image(models.Model):
    configuration = models.ForeignKey(Configuration, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="media/products")

    def __str__(self):
        return self.configuration.product.name

    class Meta:
        db_table = "image"

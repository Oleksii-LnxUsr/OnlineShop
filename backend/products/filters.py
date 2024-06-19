from django_filters import FilterSet, NumberFilter, CharFilter
from products.models import Product


class ProductFilter(FilterSet):
    category = NumberFilter(field_name="category__id")
    brand = NumberFilter(field_name="brand__id")
    color = CharFilter(field_name="configuration__color__name", lookup_expr="iexact")

    class Meta:
        model = Product
        fields = ["category", "brand", "color"]

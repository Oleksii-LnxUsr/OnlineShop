from django_filters import FilterSet, NumberFilter, CharFilter
from products.models import Product


class MultipleValuesCharFilter(CharFilter):
    """Custom filter for filtering by multiple values ​​separated by commas."""
    def filter(self, qs, value):
        if not value:
            return qs
        values = value.split(",")
        lookup = f"{self.field_name}__in"
        return qs.filter(**{lookup: values})


class ProductFilter(FilterSet):
    """
    A set of filters for the Product model.

    filter products by category, brand and color. Each filter
    can take multiple values, separated by commas.
    """
    category = MultipleValuesCharFilter(field_name="category__name")
    brand = MultipleValuesCharFilter(field_name="brand__name")
    color = MultipleValuesCharFilter(field_name="configuration__color__name")

    class Meta:
        model = Product
        fields = ["category", "brand", "color"]

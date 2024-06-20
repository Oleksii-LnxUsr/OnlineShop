from django.db.models import Count, Q, F
from products.models import Product, Configuration, Category, Brand, Color


def get_filtered_products(selected_categories, selected_brands, selected_colors):
    """Filter products based on selected categories, brands and colors."""
    filters = Q()

    if selected_categories:
        filters &= Q(category__name__in=selected_categories.split(","))

    if selected_brands:
        filters &= Q(brand__name__in=selected_brands.split(","))

    if selected_colors:
        filters &= Q(configuration__color__name__in=selected_colors.split(","))

    # Filter products based on collected filters and remove duplicates
    products = Product.objects.filter(filters).distinct()
    return products


def annotate_product_filters(products):
    """Annotate products to get category, brand, and color fields."""
    return products.annotate(
        annotated_category_id=F("category__id"),
        annotated_category_name=F("category__name"),
        annotated_brand_id=F("brand__id"),
        annotated_brand_name=F("brand__name"),
        annotated_color_id=F("configuration__color__id"),
        annotated_color_name=F("configuration__color__name"),
        annotated_color_hex_code=F("configuration__color__hex_code"),
    ).values(
        "annotated_category_id",
        "annotated_category_name",
        "annotated_brand_id",
        "annotated_brand_name",
        "annotated_color_id",
        "annotated_color_name",
        "annotated_color_hex_code",
    ).distinct()

def create_unique_dicts(available_filters):
    """Create unique dictionaries for categories, brands and colors."""
    categories = {
        f["annotated_category_id"]: f["annotated_category_name"]
        for f in available_filters
    }
    brands = {
        f["annotated_brand_id"]: f["annotated_brand_name"] for f in available_filters
    }
    colors = {
        f["annotated_color_id"]: {
            "name": f["annotated_color_name"],
            "hex_code": f["annotated_color_hex_code"],
        }
        for f in available_filters
    }
    return categories, brands, colors

def get_available_filters(products):
    """Get available categories, brands and colors for further filtering based on the filtered products."""
    # Annotating product data to obtain the required fields
    available_filters = annotate_product_filters(products)
    
    # Create dictionaries for unique categories, brands and colors
    categories, brands, colors = create_unique_dicts(available_filters)

    # Return data in a format convenient for use on the client
    return {
        "categories": [{"id": k, "name": v} for k, v in categories.items()],
        "brands": [{"id": k, "name": v} for k, v in brands.items()],
        "colors": [
            {"id": k, "name": v["name"], "hex_code": v["hex_code"]}
            for k, v in colors.items()
        ],
    }
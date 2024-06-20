from django.db.models import Count, Q, F
from products.models import Product, Configuration, Category, Brand, Color


def get_filtered_products(selected_categories, selected_brands, selected_colors):
    filters = Q()

    if selected_categories:
        filters &= Q(category__name__in=selected_categories.split(","))

    if selected_brands:
        filters &= Q(brand__name__in=selected_brands.split(","))

    if selected_colors:
        filters &= Q(configuration__color__name__in=selected_colors.split(","))

    products = Product.objects.filter(filters).distinct()
    return products


def get_available_filters(products):
    available_filters = products.annotate(
        annotated_category_id=F('category__id'),
        annotated_category_name=F('category__name'),
        annotated_brand_id=F('brand__id'),
        annotated_brand_name=F('brand__name'),
        annotated_color_id=F('configuration__color__id'),
        annotated_color_name=F('configuration__color__name'),
        annotated_color_hex_code=F('configuration__color__hex_code')
    ).values(
        'annotated_category_id', 'annotated_category_name',
        'annotated_brand_id', 'annotated_brand_name',
        'annotated_color_id', 'annotated_color_name', 'annotated_color_hex_code'
    ).distinct()

    categories = {f['annotated_category_id']: f['annotated_category_name'] for f in available_filters}
    brands = {f['annotated_brand_id']: f['annotated_brand_name'] for f in available_filters}
    colors = {
        f['annotated_color_id']: {'name': f['annotated_color_name'], 'hex_code': f['annotated_color_hex_code']}
        for f in available_filters
    }

    return {
        "categories": [{"id": k, "name": v} for k, v in categories.items()],
        "brands": [{"id": k, "name": v} for k, v in brands.items()],
        "colors": [{"id": k, "name": v['name'], "hex_code": v['hex_code']} for k, v in colors.items()],
    }
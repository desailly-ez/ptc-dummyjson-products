"""
utils.py - functions for sorting and filtering the products.
Both functions use functional programming techniques (sorted, filter, lambda).
"""


def sort_products(products):
    """Sort the products by title in ascending order (A -> Z).

    sorted() makes a new list and leaves the original list unchanged.
    The lambda tells sorted() to compare the titles.
    lower() makes sure "apple" and "Apple" are sorted the same way.
    A missing title is treated as an empty text.
    """
    return sorted(products, key=lambda product: (product.get("title") or "").lower())


def filter_products(products, category=""):
    """Filter the products on category.

    If the category is empty, all products are returned.
    The comparison is case-insensitive, so "Beauty" and "beauty" both work.
    filter() keeps only the products for which the lambda returns True.
    """
    if category:
        products = filter(
            lambda product: (product.get("category") or "").lower() == category.strip().lower(),
            products,
        )

    return list(products)


def get_categories(products):
    """Return a sorted list of all different categories.

    map() takes the category out of every product,
    set() removes the duplicates and sorted() puts them in order.
    """
    return sorted(set(map(lambda product: product.get("category"), products)) - {None})

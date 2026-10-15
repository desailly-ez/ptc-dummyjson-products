"""
data.py - backend functions that get and process the product data.
"""

import requests

# The API endpoint with the products
API_URL = "https://dummyjson.com/products"


def fetch_products():
    """Fetch product data from the DummyJSON API.

    Returns a list of products (dictionaries).
    If something goes wrong, an error message is printed and an empty
    list is returned, so the website does not crash.
    """
    try:
        # limit=0 means: give me ALL products (the default is only 30)
        response = requests.get(API_URL, params={"limit": 0}, timeout=10)

        # Status code 200 means the request was successful
        if response.status_code == 200:
            # The products are inside the "products" key of the JSON
            return response.json()["products"]

        print(f"Error: API returned status code {response.status_code}")

    except requests.RequestException as error:
        print(f"Error while fetching products: {error}")

    return []


def product_generator(products):
    """Generator function that yields the products one by one.

    Only the fields that we show in the table are kept.
    'yield' gives back one product at a time instead of a whole list.
    """
    for product in products:
        yield {
            "id": product.get("id"),
            "title": product.get("title"),
            "category": product.get("category"),
            "brand": product.get("brand", "N/A"),  # not every product has a brand
            "price": product.get("price"),
            "rating": product.get("rating"),
            "stock": product.get("stock"),
        }

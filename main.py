"""
main.py - entry point of the PTC Products App.

This file only connects the parts together:
    src/data.py   -> gets the data from the API (backend)
    src/utils.py  -> sorts and filters the data (data processing)
    templates/    -> the HTML page (frontend)
"""

from flask import Flask, render_template, request

from src.data import fetch_products, product_generator
from src.utils import sort_products, filter_products, get_categories

# Create the Flask application
app = Flask(__name__)


@app.route("/")
def home():
    """Route for the home page: gets, filters, sorts and shows the products."""

    # 1. Get the products from the API
    products = fetch_products()

    # 2. Process the products with the generator and put them in a list
    products = list(product_generator(products))

    # 3. Make the list of categories for the filter (before filtering!)
    categories = get_categories(products)

    # 4. Read the user input from the URL, e.g. /?category=beauty
    category = request.args.get("category", "")

    # 5. Filter the products on the category the user typed
    products = filter_products(products, category)

    # 6. Sort the products by title, A -> Z
    products = sort_products(products)

    # 7. Send everything to the HTML template
    return render_template(
        "index.html",
        products=products,
        categories=categories,
        selected_category=category,
    )


# Only start the server when this file is run directly (python main.py)
if __name__ == "__main__":
    app.run(debug=True)

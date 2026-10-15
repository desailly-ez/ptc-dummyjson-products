# PTC Products App

Personal Python 2 (DS304) final assignment for PTC Data Science.

## Description

A simple web application built with Python and Flask.
It retrieves product data from the DummyJSON API, shows it in a table
and lets the user sort and filter the results.

## Features

- Retrieve product data from the DummyJSON API
- Display the products in a table
- Sort the products by title (ascending)
- Filter the products by category
- Generator function for processing the data
- Functional programming (`sorted`, `filter`, `map`, `lambda`) for sorting and filtering

## Technologies

- Python
- Flask
- Requests
- HTML
- CSS
- GitHub

## Project structure

```
ptc-dummyjson-products/
├── main.py              # Flask app and route (entry point)
├── requirements.txt     # Dependencies
├── README.md
├── .gitignore
├── src/
│   ├── __init__.py
│   ├── data.py          # Fetch data from the API + generator function
│   └── utils.py         # Sort and filter functions
├── templates/
│   └── index.html       # HTML page (Jinja2 template)
└── static/
    └── style.css        # CSS styling
```

## Installation

1. Clone the repository

   ```
   git clone https://github.com/<your-username>/ptc-dummyjson-products.git
   cd ptc-dummyjson-products
   ```

2. Create and activate a virtual environment (Anaconda)

   ```
   conda create -n python2_project python=3.12
   conda activate python2_project
   ```

3. Install the dependencies

   ```
   pip install -r requirements.txt
   ```

4. Run the application

   ```
   python main.py
   ```

5. Open the browser at

   ```
   http://127.0.0.1:5000
   ```

## How to use

- The page shows all products, sorted by title (A-Z).
- Type or choose a category in the filter box and click **Filter**.
- Click **Reset** to show all products again.

## API

[DummyJSON Products](https://dummyjson.com/products)

## Group members

Individual assignment - <your name>

from flask import Flask, jsonify, request
import requests 

app = Flask(__name__)

# Define valid companies and categories
VALID_COMPANIES = ["AMZ", "EBY", "WMT"]  
VALID_CATEGORIES = ["Laptop", "Mobile", "TV"]


# we should not include token to uplpad on git hub but i Don't have time to make a seoerate .env file
BASE_URL = "https://http://20.244.56.144/test/companies/"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNYXBDbGFpbXMiOnsiZXhwIjoxNzE4NzkyNTE5LCJpYXQiOjE3MTg3OTIyMTksImlzcyI6IkFmZm9yZG1lZCIsImp0aSI6IjFiZTIxNWQ5LTA4ODYtNGU4OS1hZmQwLTIzNTAwYjNjMThjOSIsInN1YiI6ImthcmFuMTAwNzIwMDJAZ21haWwuY29tIn0sImNvbXBhbnlOYW1lIjoiQUJDSV9ORElBIiwiY2xpZW50SUQiOiIxYmUyMTVkOS0wODg2LTRlODktYWZkMC0yMzUwMGIzYzE4YzkiLCJjbGllbnRTZWNyZXQiOiJMZk9Hb3RPbmVCYmtGVVJMIiwib3duZXJOYW1lIjoiQUJDMTIzIiwib3duZXJFbWFpbCI6ImthcmFuMTAwNzIwMDJAZ21haWwuY29tIiwicm9sbE5vIjoiQTYwMjA1MjIxMjU5In0.7jy89jhKd67P-AvlvWcmI3HSyIZKvESHkZ_tPmJMmsY"

headers = {
    'Authorization': f"Bearer: {token}"
}

def get_products_from_ecommerce(company, category, n, sort_by, sort_order, min_price=None, max_price=None, page=1):
    # Simulate API calls to e-commerce companies
    url = f"{BASE_URL}{company}/{category}/products?top={n}&page={page}"
    if sort_by:
        url += f"&sort={sort_by}"
    if sort_order:
        url += f"&order={sort_order}"
    if min_price and max_price:
        url += f"&price_range={min_price},{max_price}"
    response = requests.get(url, headers = headers)

    # Parse response and extract relevant product data
    if response.status_code == 200:
        products = response.json()
        return products
    else:
        return None


@app.route('/products/companies/<company>/categories/<category>/products', methods=['GET'])
def get_top_products(company, category):
    if company not in VALID_COMPANIES or category not in VALID_CATEGORIES:
        return jsonify({"error": "Invalid company or category"}), 400

    n = request.args.get('top', 10)  # default number of products
    min_price = request.args.get('minPrice')
    max_price = request.args.get('maxPrice')
    sort_by = request.args.get('sort_by', None)
    sort_order = request.args.get('sort_order', None)
    page = request.args.get('page', 1)

    products = get_products_from_ecommerce(company, category, n, sort_by, sort_order, min_price, max_price, page)
    if not products:
        return jsonify({"error": "Error retrieving products"}), 500

    # Process and format product data
    formatted_products = []
    for product in products:
        formatted_products.append({
            "productName": product["name"],
            "price": product["price"],
            # Add other relevant product details (rating, discount, availability)
        })

    return jsonify(formatted_products)


@app.route('/products/<product_id>', methods=['GET'])
def get_product_details(product_id):
    # Simulate API calls to e-commerce companies
    url = f"{BASE_URL}product/{product_id}"
    response = requests.get(url, headers = headers)

    if response.status_code == 200:
        product = response.json()
        # Process and format product data 
        formatted_product = {
            "productName": product["name"],
            "price": product["price"],
            # Add other relevant product details (rating, discount, availability)
        }
        return jsonify(formatted_product)
    else:
        return jsonify({"error": "Product not found"}), 404


if __name__ == '__main__':
    app.run()

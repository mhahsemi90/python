import keepa
import json

# Set your Keepa API key
API_KEY = 'your_api_key_here'

# Set the Amazon locale to search in
AMAZON_LOCALE = keepa.AmazonLocale.US

# Set the product category to search in
PRODUCT_CATEGORY = keepa.Category.ELECTRONICS

# Set the desired price and discount filters
DESIRED_PRICE = 100
DESIRED_DISCOUNT = 20

# Connect to the Keepa API
api = keepa.Keepa(API_KEY)

# Search for Amazon deals using the desired filters
products = api.search(AMAZON_LOCALE, PRODUCT_CATEGORY, desired_price=DESIRED_PRICE, desired_discount=DESIRED_DISCOUNT)

# Convert the search results to a JSON string
json_data = json.dumps(products)

# Write the JSON data to a file
with open('products.json', 'w') as f:
    f.write(json_data)

# Read the product data from the JSON file
with open('products.json', 'r') as f:
    products = json.load(f)

# Analyze the product data
for product in products:
    print(f"Product name: {product['name']}")
    print(f"Product price: {product['price']}")
    print(f"Product rank: {product['rank']}")
    print(f"Product rating: {product['rating']}")
    print()
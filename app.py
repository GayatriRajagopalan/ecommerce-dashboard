from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Mongo connection
mongo = MongoClient(port=27017)
db = mongo['ecommerce_project']
carts_col = db['carts']
products_col = db['products']
users_col = db["users"]

# Example endpoint: Get all carts with product details
@app.route('/carts', methods=['GET'])
def get_carts():
    pipeline = [
        {"$unwind": "$products"},
        {"$lookup": {
            "from": "products",
            "localField": "products.productId",
            "foreignField": "id",
            "as": "product_info"
        }},
        {"$unwind": "$product_info"},
        {"$project": {
            "_id": 0,
            "cart_id": "$id",
            "userId": 1,
            "productId": "$products.productId",
            "quantity": "$products.quantity",
            "product_name": "$product_info.title",
            "price": "$product_info.price"
        }}
    ]
    carts = list(carts_col.aggregate(pipeline))
    return jsonify(carts)

 #Example endpoint: Get all products
@app.route('/products', methods=['GET'])
def get_products():
    products = list(products_col.find({}, {"_id": 0}))
    return jsonify(products)

# # Example endpoint: Get all users
@app.route('/users', methods=['GET'])
def get_users():
    users = list(users_col.find({}, {"_id": 0}))
    return jsonify(users)


if __name__ == "__main__":
    app.run(debug=True)
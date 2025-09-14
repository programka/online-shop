from flask import Flask, jsonify

app = Flask(__name__)

# Эмуляция базы товаров
products = [
    {"id": 1, "name": "Product A", "price": 100},
    {"id": 2, "name": "Product B", "price": 150}
]

@app.route('/api/products')
def get_products():
    return jsonify(products)

@app.route('/api/hello')
def hello():
    return jsonify(message="Hello from backend!")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

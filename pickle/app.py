from flask import Flask, render_template

# Corrected paths: template in 'template', static files in 'static'
import os

print("Working dir:", os.getcwd())
print("Files in current dir:", os.listdir())
print("Files in template folder:", os.listdir("template"))

app = Flask(__name__,template_folder='template')

# Routes

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/products')
def products():
    return render_template('product.html')

@app.route('/product-detail')
def product_detail():
    return render_template('product-detail.html')

@app.route('/cart')
def cart():
    return render_template('cart.html')

@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)

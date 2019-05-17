# -*- coding: utf-8 -*-

from flask import Flask, render_template

# create an instance of Flask class.
app = Flask(__name__)
# Configurations
app.config.from_object('config')


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')


@app.route('/sign_up', methods=['GET'])
def sign_up():
    return render_template('sign_up.html')


@app.route('/my_products', methods=['POST'])
def my_products():
    return render_template('my_products.html')


@app.route('/buy_products', methods=['GET'])
def buy_products():
    return render_template('buy_products.html')


@app.route('/demand', methods=['GET'])
def demand():
    return render_template('demand.html')
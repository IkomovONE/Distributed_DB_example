from flask import Flask, render_template, request
from pymongo import MongoClient           #Importing necessary libraries



app = Flask(__name__)    #Using Flask to initialize frontend server



client = MongoClient("localhost:27017")     #Setting up mongoDB to connect to databases

europe_db = client["Europe"]     #Establishing 3 databases, 3 continents

asia_db = client["Asia"]

us_db = client["US"]


users_eu = europe_db["Users"]
users_asia = asia_db["Users"]     #users
users_us = us_db["Users"]

sellers_eu = europe_db["Sellers"]
sellers_asia = asia_db["Sellers"]   #sellers
sellers_us = us_db["Sellers"]

products_eu = europe_db["Products"]
products_asia = asia_db["Products"]    #products
products_us = us_db["Products"]

orders_eu = europe_db["Orders"]
orders_asia = asia_db["Orders"]    #orders
orders_us = us_db["Orders"]



@app.route("/", methods=["GET", "POST"])    #creating a route
def home():
    users, sellers, products, orders = None, None, None, None

    if request.method == "POST":
        location = request.form["location"]   #Using POST method

        
        if location == "Europe":
            
            users = list(users_eu.find({}))  
            sellers = list(sellers_eu.find({}))      
            products = list(products_eu.find({}))
            orders = list(orders_eu.find({}))
            
        elif location == "Asia":

            users = list(users_asia.find({}))
            sellers = list(sellers_asia.find({}))
            products = list(products_asia.find({}))
            orders = list(orders_asia.find({}))

        elif location == "US":

            users = list(users_us.find({}))
            sellers = list(sellers_us.find({}))
            products = list(products_us.find({}))
            orders = list(orders_us.find({}))

    return render_template("index.html", users=users, sellers=sellers, products=products, orders=orders)  #rendering using index.html

if __name__ == "__main__":
    app.run(debug=True)    #running the app




#RUN USING flask --app store run



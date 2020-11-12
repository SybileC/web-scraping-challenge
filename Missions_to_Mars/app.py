from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

@app.route("/")
def index():
    mars_data = mongo.db.collection.find_one()

    # Return template and data
    return render_template("index.html", astrology=mars_data)

@app.route("/scrape")
def scrape():
    mars_info = scrape_mars.scrape_info()
    print(mars_info)

    mongo.db.collection.update({}, mars_info, upsert=True)

    return reditect("/")




if __name__ == "__main__":
    app.run(debug=True)
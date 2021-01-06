from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")


@app.route("/")
def index():
    #  Find one record of data from the mongo database
    # mars = mongo.db.mars
    mars_data = mongo.db.scraping_codes.find_one()

    # Return template and data
    return render_template("index.html", astrology=mars_data)

@app.route("/scrape")
def scrape():
    mars_data = mongo.db.scraping_codes
    mars_info = scrape_mars.scrape_info()
    print(mars_info)

    # mongo.db.collection.update({}, mars_info, upsert=True)
    mars_data.update({}, mars_info, upsert=True)

    return redirect("/", code=302)




if __name__ == "__main__":
    app.run(debug=True)
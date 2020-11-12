from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

@app.route("/scrape")
def scrape():
    mars_info = scrape_mars.scrape_info()
    return render_template("index.html", mars = mars_info)


if __name__ == "__main__":
    app.run(debug=True)
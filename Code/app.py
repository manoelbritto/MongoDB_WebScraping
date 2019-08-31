from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/dbscrape_app"
mongo = PyMongo(app)

# Or set inline
# mongo = PyMongo(app, uri="mongodb://localhost:27017/craigslist_app")


@app.route("/")
def index():
    listings = mongo.db.listings.find_one()
    return render_template("index.html", listings=listings)


@app.route("/images")
def image():
    listings = mongo.db.listings.find_one()
    return render_template("pages/images.html", listings=listings)


@app.route("/scrape")
def scraper():

    listings = mongo.db.listings
    listings.remove()
    listings_data = scrape_mars.scrape()
    listings.insert(listings_data)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)

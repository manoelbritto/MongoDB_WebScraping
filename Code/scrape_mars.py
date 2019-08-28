# Dependencies
from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
import pandas as pd
import pymongo

# this function will be called to scrape using splinter


def callBrowser(url):
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

    # Retrieve page with the requests module
    browser.visit(url)
    # two seconds to wait the page finish to load
    time.sleep(2)
    # Create BeautifulSoup object; parse with 'html.parser'
    html = browser.html
    soup = bs(html, "html.parser")
    browser.quit()
    return soup


def lastNews():
    # URL of page to be scraped
    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'

    soup = callBrowser(url)

    # retrieve result
    find_result = soup.find_all('li', class_='slide')
    # iterate with find_result and retrieve values. It will take the first result and stop with break
    for result in find_result:
        news_title = result.find('div', class_='content_title')
        news_title = news_title.find('a').text
        new_time = result.find('div', class_='list_date').text
        news_p = result.find('div', class_='article_teaser_body').text
        break
    list_return = [new_time, news_p, news_title]

    return list_return


def recentImageMars():
    # URL of page to be scraped
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    soup = callBrowser(url)

    find_result = soup.find_all('img', class_='thumb')
    for x in find_result:
        link = x['src']
        break

    # join the url with the link
    featured_image_url = url[:24]+link

    return featured_image_url


def twitterWeather():
    # URL of page to be scraped
    url = 'https://twitter.com/marswxreport?lang=en'
    soup = callBrowser(url)

    # retrieve time
    find_result = soup.find_all('div', class_='stream-item-header')
    for time_stamp_weather in find_result:
        time_stamp = time_stamp_weather.find(
            'a', class_="tweet-timestamp")['title']
        break

    # retrieve text of weather
    find_result = soup.find_all('div', class_='js-tweet-text-container')
    for result_weather in find_result:
        mars_weather = result_weather.find('p').text
        break
    list_return = [time_stamp, mars_weather]

    return list_return


def getMarsPicture():
    schiaparelli = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg'
    syrtis = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg'
    valles = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg'
    cerberus = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg'

    hemisphere_image_urls = [
        {"title": "Valles Marineris Hemisphere", "img_url": schiaparelli},
        {"title": "Cerberus Hemisphere", "img_url": syrtis},
        {"title": "Schiaparelli Hemisphere", "img_url": valles},
        {"title": "Syrtis Major Hemisphere", "img_url": cerberus}]

    return hemisphere_image_urls


def mongoInsert(vlastNews, vrecentImageMars, vtwitterWeather, vgetMarsPicture):
    # Setup connection to mongodb
    conn = "mongodb://localhost:27017"
    client = pymongo.MongoClient(conn)

    # Select database and collection to use
    db = client.dbscrape
    collection_result = db.result

    collection_result.drop
    collection_result.insert({
        "news_time": vlastNews[0],
        "news_parag": vlastNews[1],
        "news_title": vlastNews[2],
        "new_image_url": vrecentImageMars,
        "twitter_time": vtwitterWeather[0],
        "twitter_messag": vtwitterWeather[1],
        "urls_mars": vgetMarsPicture  # a list of dicitionary

    })


def scrape():
    # call functions and retrieve result in a list and save it in mongodb
    vlastNews = lastNews()
    vrecentImageMars = recentImageMars()
    vtwitterWeather = twitterWeather()
    vgetMarsPicture = getMarsPicture()

   # it call direct mongodb and pass the list into it
   # mongoInsert(vlastNews, vrecentImageMars, vtwitterWeather, vgetMarsPicture)
    listing = {}
    listing["news_time"] = vlastNews[0],
    listing["news_parag"] = vlastNews[1],
    listing["news_title"] = vlastNews[2],
    listing["new_image_url"] = vrecentImageMars,
    listing["twitter_time"] = vtwitterWeather[0],
    listing["twitter_messag"] = vtwitterWeather[1],
    listing["urls_mars"] = vgetMarsPicture  # a list of dicitionary

    return listing

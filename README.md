# Project: News of Mars
This project has the goal to scrape data from web pages using python libraries, for instance, splinter and beautifulsoup. At the end of the process, the data will be saved in non-SQL database (MongoDB) and dynamically displayed onto the HTLM webpage using Flask and Bootstrap.

## Getting start:
To run this code is necessary to have some library installed on your machine:<br>
**MongoDB:**<br>
https://www.mongodb.com/download-center/community<br>
**Anaconda:**<br>
https://www.anaconda.com/distribution/<br>

**Libraries:**
```
pip install beautifulsoup4
pip install html5lib
pip install splinter
pip install pymongo
pip install pandas
pip install flask
```
<br>Then, you have to start MongoDB services and execute app.py:
**Command to start MongoDB service:**<br>
mongod <br>
**Execute the program:** <br>
python app.py<br>

## Scraping pages (extracting data) from:
https://mars.nasa.gov/news/<br>
https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars<br>
https://twitter.com/marswxreport?lang=en<br>
https://space-facts.com/mars/<br>
https://astropedia.astrogeology.usgs.gov/download<br>

## Web Page shows the result:
The scrape program will execute after pushing  the button *“Push here to news from Mars”*<br>
**Page 1**<br>
![GitHub Logo](/images/page1-1.PNG)<br><br>
![GitHub Logo](/images/page1-2.PNG)<br><br>
**Page 2**<br>
![GitHub Logo](/images/page2.PNG)<br><br>
Data retrieved in MongoDB:<br>
![GitHub Logo](/images/mongodb.PNG)<br><br>

## Coding:
Jupyter notebook: this [program](https://github.com/manoelbritto/MongoDB_WebScraping/blob/master/Code/mission_to_mars.ipynb) has all the functionalities to scrape the data from different webpages; however, it doesn’t retrieve data into MongoDB and doesn’t show onto Webpage.

There are two main Python code:
1. [app.py](https://github.com/manoelbritto/MongoDB_WebScraping/blob/master/Code/app.py) is the main program to rote the pages,  save it into MongoDB, and call the functions inside the scrape_mars.py
1. [scrape_mars.py](https://github.com/manoelbritto/MongoDB_WebScraping/blob/master/Code/scrape_mars.py) is the program that has many functions created to scrape the webpages using Beatifulsoup and splinter libraries.

## Feature:
- MongoDB database
- Python with:
	- Flask
	- PyMongo
	- splinter
	- BeautifulSoup
	- Pandas
- Html and CSS with Bootstrap 4

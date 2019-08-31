# Project: News of Mars
This project has the goal to scrape data from web pages using python libraries, for instance, splinter and beautifulsoup. At the end of the process, the data will be saved in non-sql database (MongoDB) and dynamically displayed onto HTLM webpage using Flask and Bootstrap.

## Getting start:
To run this code is necessary to have some library installed in your machine:
** Mongodb: **
https://www.mongodb.com/download-center/community
** Anaconda: **
https://www.anaconda.com/distribution/

** Libraries: **
```
pip install beautifulsoup4
pip install html5lib
pip install splinter
python -m pip install pymongo
pip install pandas
pip install flask
```

Then, you have to start MongoDB services and execute app.py:
Command to start mongodb service:
mongod 
Execute the program:
python app.py

## Scraping pages (extracting data) from:
https://mars.nasa.gov/news/
https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars
https://twitter.com/marswxreport?lang=en
https://space-facts.com/mars/
https://astropedia.astrogeology.usgs.gov/download

## Web Page shows the result:
The scrape program will execute after push the button “Push here to news from Mars”
 

 


 

Data retrieved in MongoDB:
 

## Coding:
Jupyter notebook: this program has all the functionalities to scrape the data from different webpages, however, it doesn’t include retrieve data into mongoDB and doesn’t show onto Webpage.

Python code: There are two python code:
1 app.py is the main program to rote the pages,  save it into mongodb, and call the functions inside the scrape_mars.py
2. scrape_mars.py is the program that has many functions created to scrape the webpages using Beatifulsoup and splinter libraries.

## Feature:
MondoDB
Python with:
	flask
	PyMongo
splinter
BeautifulSoup
pandas

Html and CSS with Bootstrap 4


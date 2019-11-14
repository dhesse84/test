import pandas as pd
import urllib.request
from splinter import Browser
from bs4 import BeautifulSoup as bs
import time

def scrape_info():
    # this dictionary will hold everything we pull from all the sites
    scraped_data = {}

    # site 1 -
    news_url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"

    # use [splinter &] beautiful soup to parse the url above
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

    browser.visit(news_url)
    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    # use bs to find() [divs] and filter on the class_='content_tile'
    found_titles = soup.find_all('div',class_='content_title')

    news_title = found_titles[0].text
    scraped_data['news_title'] = news_title

    # use bs to find() the example_title_div and filter on the class_='article_teaser_body'
    found_teasers = soup.find_all('div',class_='article_teaser_body')

    news_p = found_teasers[0].text
    scraped_data['news_p'] = news_p
    
    return scraped_data


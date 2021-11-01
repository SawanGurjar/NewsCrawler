# -*- coding: utf-8 -*-
"""news_crawler_splitted.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DYeY42b4vmKWuFN_Ov0RjZd_OyclHeIv

# News Crawler Application
*This is an interactive Jupyter Notebook which retrieves top news about a company (as asked by the user). Powered by News API*

This project was imagined after Facebook's stock price **dropped about 40%** between the closing on July 25, 2018 and opening of July 26, 2018. One of the main factors in the sudden drop in facebook's stock price was it's earning report missing expectations on revenue and showing a slowing user growth. This project is an attempt to help an investor keep track of big news about companies in an attempt to protect them from such a loss.

The following describes the workflow behind the application and how it captures major new sources at any given point of time.

#Requirements
"""

pip install newsapi-python

"""# All the imports

### For user input
"""

from ipywidgets import widgets
from ipywidgets import *

"""**Widgets** are eventful **python objects** that have a representation in the browser, often as a control like a slider, textbox, etc.
You can use widgets to build **interactive GUIs for your notebooks**.
You can also use widgets to synchronize stateful and stateless information between Python and JavaScript.
"""

from traitlets import *

"""**Traitlets** is a framework that lets Python classes have attributes with type checking, dynamically calculated default values, and ‘on change’ callbacks.
The package also includes a mechanism to use traitlets for configuration, loading values from files or from command line arguments. This is a distinct layer on top of traitlets, so you can use traitlets in your code without using the configuration machinery.
"""

from IPython.display import display, Markdown

"""To display in a markdown format"""

import unicodedata

"""This module provides access to the Unicode Character Database (UCD) which defines character properties for all Unicode characters.

(To convert unicode to string) 
"""

from newsapi import NewsApiClient

"""Use the **unofficial Python client library** to *integrate News API into your Python application* without having to make HTTP requests directly.
(NewsApiClient to find URLs of all the trending news)
"""

import requests

"""Requests allows you to send HTTP/1.1 requests extremely easily. There’s no need to manually add query strings to your URLs, or to form-encode your PUT & POST data — but nowadays, just use the json method!
(Requests is used to get an html markup from a URL)
"""

from bs4 import BeautifulSoup

"""Beautiful Soup is a library that makes it easy **to scrape information from web pages**. It sits atop an HTML or XML parser, providing Pythonic idioms for iterating, searching, and modifying the parse tree.

# Ask user about their choice of the topic

We'll start by asking the user about what topic they're interested in. Run the cell and enter a name of a company and press _enter_

### Get user choice about the topic
"""

text_input = widgets.Text()
print("Enter the topic you want to find news about: ")
display(text_input)

"""### Confirm user choice"""

def handle_submit(sender):
    print("Alright, let's show you news about", text_input.value)
    
text_input.on_submit(handle_submit)

"""Store user's topic choice for use in the rest of the notebook. (Note: need to convert from unicode to string for ease of use later)

### Convert user's topic preference into a string ready for API query
"""

# company_name = unicodedata.normalize('NFKD', text_input.value).encode('ascii','ignore')
# company_name = text_input.value.encode('ascii','ignore')

"""# Find top news article URLs

Next, we'll use the **News API** to find the top trending news about the company from CNBC and BBC News (in order to find a diversified, yet reputable mix of news articles). Currently we're only fetching 5 news articles, but that value can be changed.

### Call to NewsApi
"""

newsapi = NewsApiClient(api_key='27a062ac4e3340bead02d732875bddff')
# q = topic_name
all_articles = newsapi.get_everything(q = 'google',
                                      sources='bloomberg',
                                      language='en',
                                      sort_by='relevancy',
                                      page_size = 5)

"""### Create a list of URLs to crawl through from the API"""

list_url = []
for item in all_articles['articles']:
    list_url.append(unicodedata.normalize('NFKD', item['url']).encode('ascii','ignore'))

"""### Iterate through URLs and capture text

Here we'll utilize the beautiful soup library to parse through html content and store only the article content. For each url:
1. We fetch the HTML
2. Parse the HTML document using Beautiful Soup 
3. Find and store the content of news article inside the webpage
"""

# Iterate through list of urls, capture text on each and make presentable
article_content = []
for i in list_url:
    page = requests.get(i)
    soup = BeautifulSoup(page.content, 'html.parser')
    content = soup.find_all(['p'])
    for line in content:
        line_string = unicodedata.normalize('NFKD', line.get_text()).encode('ascii','ignore')
        if (len(line_string)>20):
            article_content.append(line_string)
    article_content.append(',')

"""### Display the articles

Use the Display class to present the articles in Markdown
"""

counter = 1
display(Markdown("# Article " + str(counter)))
for line in article_content:
    if(line == ','):
        counter = counter + 1
        if (not(counter<=5)):
            break;
        display(Markdown("# Article " + str(counter)))
        continue
    display(Markdown(line))

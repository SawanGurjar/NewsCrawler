# NewsCrawler Application
*This is an **Interactive Jupyter Notebook application** which retrieves top news on a topic (as asked by the user) from trustworthy news sources, powered by News API.*

When we try to find news on any topic, generally we search on Google and find the results filled with *fake news or biased news*,  and mostly belong to *unverified or unreliable resources*. Since Google hasn't indexed most of the parts of the internet, the results aren't soo accurate. This ends up in spreading fake news sometimes. One of the solutions is to get news from the websites or sources that we can trust like BBC, CNN, The Times of India, The Hindu, etc. This will help us to stay away from articles that are meant to propagate fake news. NewsCrawler is an application that can perform a *search within the selected RSS feeds*. The possibility to filter the news by keywords, which is very useful when the user is interested in a particular topic can be anything like, Crypto-currency, Prime Minister of India,  stock prices of a company, etc. It is no longer necessary to access the websites of a specific source, as you can log into them from NewScrawler. NewScrawler works based on the concept of *web scraping using news APIs*. It can be run on Jupyter Notebook, or Google Colab.

Requirements
------------

To use NewsCrawler Application you need to install some dependencies.<br>
- To install python3 on ubuntu, Open the terminal and run the command below:<br>
	`$ sudo apt install python3.6`
- To install Jupyter Notebook on ubuntu:
	+ Install the virtualenv (Python tool used for creating isolated Python environments.)<br>
		`$ sudo -H pip3 install virtualenv`
	+ Create a virtual environment for launching Jupyter
		``` 
		$ mkdir jupyter_dir
		$ cd jupyter_dir
		$ virtualenv jupyter_env
		```
	+ Activate the virtual environment using the source command-line tool.<br>
		`$ source jupyter_env/bin/activate`
	+ Install and launch Jupyter Notebook
		```	
		$ pip3 install jupyter
		$ jupyter notebook
		```

- For user input we use:<br>
	```
	$ pip install ipywidgets
	$ pip install traitlets
	
	```
- NewsApiClient to find URLs of all the news on given topic.:<br>
	`$ pip install newsapi-python`

News articles
-------------

### Find news article URLs
We use the News API to find the top trending news about the topic from trustworthy sources like CNBC, BBC News, etc. (to find a diversified, yet reputable mix of news articles can be found by selecting multiple sources at a time).
We're only fetching 5 news articles, but we can fetch any number of articles available by changing the value of `page_size`.

Some trustworthy sources:
+ bbc-news, cnn, espn,
+ the-hindu, the-times-of-india, news24,
+ google-news, crypto-coins-news, bloomberg etc.


### Call to NewsApi
Python wrapper around A JSON API for live news and blog headline

### Create list of URLs
Create a list of URLs to crawl through from the API

### Iterate through URLs and capture text
Here we'll utilize the beautiful soup library to parse through html content and store only the article content. For each url:
+ We fetch the HTML
+ Parse the HTML document using Beautiful Soup
+ Find and store the content of news article inside the webpage

### Display the articles
Use the Display class to present the articles in Markdown
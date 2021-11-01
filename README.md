# NewsCrawler Application
*This is an interactive Jupyter Notebook application which retrieves top news on a topic (as asked by the user) from trustworthy news sources, powered by News API.*

When we try to find news on any topic, generally we search on Google and find the results filled with *fake news or biased news*,  and mostly belong to *unverified or unreliable resources*. Since Google hasn't indexed most of the parts of the internet, the results aren't soo accurate. This ends up in spreading fake news sometimes. One of the solutions is to get news from the websites or sources that we can trust like BBC, CNN, The Times of India, The Hindu, etc. This will help us to stay away from articles that are meant to propagate fake news. NewsCrawler is an application that can perform a *search within the selected RSS feeds*. The possibility to filter the news by keywords, which is very useful when the user is interested in a particular topic can be anything like, Crypto-currency, Prime Minister of India,  stock prices of a company, etc. It is no longer necessary to access the websites of a specific source, as you can log into them from NewScrawler. NewScrawler works based on the concept of *web scraping using news APIs*. It can be run on Jupyter Notebook, or Google Colab.

Requirements
------------

To use NewsCrawler Application you need to install some dependencies.<br>
- To install python3 on ubuntu, Open the terminal and run the command below:<br>
	`sudo apt install python3.6`
- To install Jupyter Notebook on ubuntu:
	+ Install the virtualenv (Python tool used for creating isolated Python environments.)
		`sudo -H pip3 install virtualenv`
	+ Create a virtual environment for launching Jupyter
		``` 
			mkdir jupyter_dir
			cd jupyter_dir
			virtualenv jupyter_env
		```
	+ Activate the virtual environment using the source command-line tool.
		`source jupyter_env/bin/activate`
	+ Install and launch Jupyter Notebook
			`pip3 install jupyter
			jupyter notebook`

- For user input we use:<br>
	`pip install ipywidgets`
	`pip install traitlets`
- NewsApiClient to find URLs of all the news on given topic.:<br>
	`pip install newsapi-python`


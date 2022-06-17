import os
from dotenv import load_dotenv

# load the .env file variables
load_dotenv()


# your app code here
consumer_key = os.environ.get('CONSUMER_KEY')

import tweepy
import requests

# Creamos cliente

client = tweepy.Client( bearer_token=bearer_token,
consumer_key=consumer_key,
consumer_secret=consumer_secret,
return_type = requests.Response,
wait_on_rate_limit=True)

query = '#100daysofcode (pandas OR python) -is:retweet'
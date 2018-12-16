from requests import *
from twitter import Twitter, OAuth, TwitterHTTPError
from numpy import *
import random

"""Authentification"""

consumer_key = '3TXjVmZEpRzMr2fBWlruWDovF'
consumer_secret = '4YABDShWyzcl3MI5M4WE4xua767GkZTjO7eDSMuallzCieCsEF'
access_token_key = '4082832802-e2PeM6xleEgAVioztlJg4MG6sx8LQwmTKgasY5D'
access_token_secret = 'V7dvg2HoXNelQyHk87YPTaLXWrCm5II9gbZfCLWh9634y'

t = Twitter(auth=OAuth(access_token_key, access_token_secret,consumer_key, consumer_secret))
x = t.statuses.home_timeline()

"""Action of Posting (cf Post.py)"""

startrepeat(Post(), 1200) #we repeat and generate n every 20 minutes

"""Extra posting actions of a human : interactions with others.
Here we develop a tool to react to positive and negative tweets (Sentiment analysis)"""

"""The first 'tweet' in the timeline"""
x[0]
"""The screen name of the user who wrote the first 'tweet'"""
x[0]['user']['screen_name']

for i in range(0,99): #let's take the first 100 tweets of the timeline and analyze whether or not they are positive
  if Sentiment(x[i]) == True: 
  # Send a direct message
    t.direct_messages.new(user=x[i]['user'],text="Nice tweet!")
    i = i+1
    


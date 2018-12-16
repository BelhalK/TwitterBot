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

"""Wether or not it is time to post"""
freq = 60 # cf explanation
n = random.sample(range(1,100), 1)
links = ['http://techcrunch.com/2015/10/31/the-path-to-expertise/',
          'http://techcrunch.com/2015/10/31/how-to-extract-more-than-capital-from-your-vcs/',
          'http://techcrunch.com/2015/10/31/checking-in-on-windows-10-2/']


def post(): 
"""m = 13 cf for explanation"""
  if n > 100*poisson(1,13):
   if random.sample(range(1,2),1) = 1: #generate another random between 1 and 2 to chose the type of tweet to post
      for items in links:
"""In case we post a tweet. First choice, build a tweet with previous 
calculus of probabilities of successive words"""
          t.statuses.update(status = Tweet_content1() + links[i]) #'check out this' kind of message + link to article
    
"""Otherwise, summary of press articles and tweet of key words and/or quotes"""
   else: 
          t.statuses.update(status = Tweet_content2())


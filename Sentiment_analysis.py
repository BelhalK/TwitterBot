from twitter import *
from numpy import *
import random
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews

"""Sentiment analysis returns True if nice tweets and False if not"""

classifier = NaiveBayesClassifier.train(trainfeats)

def Sentiment(tweet):
  tweet = [str] """the input is a tweet, ie a string of letters and space"""
  output = [ ]
  for item in input:
    items = item.split(' ') 
"""we define each word, separated by a blank space, of the tweet as elements of the new list"""
    for i in xrange(o,len(items)):
      output.insert(0, items[i]) """the new list is made of every word of the tweet"""

"""analysis of each word thanks to a classifier"""
  for item in output:
    p = 0 """count of positive words"""
    n = 0 """count of negative words"""
    
    if item is in classifier:
      p = p+1
    else : 
      n = n+1
      
  print p,n
  if p>n :
    Sentiment(tweet) = True  """If more pos than neg then tweet is nice"""
  else :
    Sentiment(tweet) = False """If not then tweet is bad """
    
  return Sentiment(tweet)    
  

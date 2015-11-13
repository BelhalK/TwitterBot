from twitter import *
from numpy import *
from nltk.parse.generate import generate, demo_grammar
from nltk import CFG
import random

"""Compute a tweet with probabilities of succesive words in massive tweets database with n-gram models
I chose to tak a bigram model in order to have probabilities of pair of words rather than single 
In that sense, we are evaluating probabilities of two successive words"""

input_list = [tweet1,tweet2,...,tweetn]

def find_bigrams(input_list):
  bigram_list = []
  for i in range(len(input_list)-1):
      bigram_list.append((input_list[i], input_list[i+1]))
  
  return bigram_list
  
"""Using NLTK grammar to generate context-free sentences"""

def Tweet_content1():
  grammar = CFG.fromstring(demo_grammar)

  for sentence in generate(grammar, n=4): """generating sentence of 4 words depth"""
    print(' '.join(sentence))
    
    return sentence

  
  
  


  

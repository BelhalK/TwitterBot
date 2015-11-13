from twitter import *
from numpy import *
import random
from pyteaser import SummarizeUrl

"""Summarize articles"""

def Tweet_content2():
  url = 'http://techcrunch.com/2015/10/31/the-path-to-expertise/'
  summaries = SummarizeUrl(url)
  return summaries 

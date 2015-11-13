from twitter import *
from numpy import *
import random

e = 2.718281828459045 #Poisson coefficient

#Poisson Law   
def poisson(k,m):
    return e**(-m)*m**k/fact(k) #Poisson Law

  

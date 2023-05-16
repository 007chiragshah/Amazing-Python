#Urllib package is the URL handling module for python. It is used to fetch URLs (Uniform Resource Locators).
#It uses the urlopen function and is able to fetch URLs using a variety of different protocols.

#Urllib is a package that collects several modules for working with URLs, such as:

#urllib.request for opening and reading.
#urllib.parse for parsing URLs
#urllib.error for the exceptions raised
#urllib.robotparser for parsing robot.txt files



#1. urllib.request

#This module helps to define functions and classes to open URLs (mostly HTTP).
# One of the most simple ways to open such URLs is : urllib.request.urlopen(url)
#Example
'''
import urllib.request
request = urllib.request.urlopen('https://www.geeksforgeeks.org/')
print(request.read())

'''
#2. urllib.parse

#This module helps to define functions to manipulate URLs and their components parts, to build or break them.
# It usually focuses on splitting a URL into small components; or joining different URL components into URL
# strings.

#Example

from urllib.parse import *

parse_url = urlparse('https://www.geeksforgeeks.org / python-urllib-module/')
print(parse_url)
print("\n")
print()
unparse_url = urlunparse(parse_url)
print(unparse_url)

#Note:- The different components of a URL are separated and joined again. Try using some other URL for
#       better understanding.

#Different other functions of urllib.parse are :

# Function                                              	Use
# urllib.parse.urlparse	        |  Separates different components of URL
# urllib.parse.urlunparse	    |  Join different components of URL
# urllib.parse.urlsplit	        |  It is similar to urlparse() but doesn’t split the params
# urllib.parse.urlunsplit	    |  Combines the tuple element returned by urlsplit() to form URL
# urllib.parse.urldeflag	    |  If URL contains fragment, then it returns a URL removing the fragment.


#For url error we can use the try and except method
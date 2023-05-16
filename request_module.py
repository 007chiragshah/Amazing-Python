import requests

#Making a Request

# Python requests module has several built-in methods to make Http requests to specified URI using GET, POST, PUT,
# PATCH or HEAD requests. A Http request is meant to either retrieve data from a specified URI or to push data to
# a server. It works as a request-response protocol between a client and a server. Let’s demonstrate how to make a
# GET request to an endpoint. GET method is used to retrieve information from the given server using a given URI.
# The GET method sends the encoded user information appended to the page request. The page and the encoded information
# are separated by the ‘?’ character.

#For example:   https://www.google.com/search?q=hello

# Making a GET request
r = requests.get('https://api.github.com/users/naveenkrnl')

# check status code for response received
# success code - 200
print(r)

# print content of request
print(r.content)

# Http Request Methods –
#---------------------------------------------------------------------------------------------------------------
# Method  |	                                    Description
#---------------------------------------------------------------------------------------------------------------
#  GET	  |   GET method is used to retrieve information from the given server using a given URI.
#--------------------------------------------------------------------------------------------------------------
#  POST	  |   POST request method requests that a web server accepts the data enclosed in the body of the request
#         |   message, most likely for storing it
#--------------------------------------------------------------------------------------------------------------
#  PUT	  |   The PUT method requests that the enclosed entity be stored under the supplied URI. If the URI
#         |   refers to an already existing resource, it is modified and if the URI does not point to an existing
#         |   resource, then the server can create the resource with that URI.
#---------------------------------------------------------------------------------------------------------------
#  DELETE |   The DELETE method deletes the specified resource
#---------------------------------------------------------------------------------------------------------------
#  HEAD	  |   The HEAD method asks for a response identical to that of a GET request, but without the response
#         |   body.
#---------------------------------------------------------------------------------------------------------------
#  PATCH  |   It is used for modify capabilities. The PATCH request only needs to contain the changes to the
#         |    resource, not the complete resource
#---------------------------------------------------------------------------------------------------------------

# Response object
# When one makes a request to a URI, it returns a response. This Response object in terms of python is returned
# by requests.method(), method being – get, post, put, etc. Response is a powerful object with lots of functions
# and attributes that assist in normalizing data or creating ideal portions of code.

# For example, response.status_code returns the status code from the headers itself, and one can check if the
# request was processed successfully or not.
# Response object can be used to imply lots of features, methods, and functionalities.

#Example

# Making a get request
response = requests.get('https://api.github.com/')

# print request object
print(response.url)

# print status code
print(response.status_code)

#Response Methods
#--------------------------------------------------------------------------------------------------------------
#      Method	      |                                  Description
#--------------------------------------------------------------------------------------------------------------
# response.headers	    | It returns a dictionary of response headers.
#--------------------------------------------------------------------------------------------------------------
# response.encoding	    | IT returns the encoding used to decode response.content.
#---------------------------------------------------------------------------------------------------------------
# response.elapsed	    | It returns a timedelta object with the time elapsed from sending the request to the
#                       | arrival of the response.
#---------------------------------------------------------------------------------------------------------------
# response.close()	    | It closes the connection to the server.
#---------------------------------------------------------------------------------------------------------------
# response.content	    | It returns the content of the response, in bytes.
#---------------------------------------------------------------------------------------------------------------
# response.cookies	    | It returns a CookieJar object with the cookies sent back from the server.
#---------------------------------------------------------------------------------------------------------------
# response.history	    | It returns a list of response objects holding the history of request (url).
#--------------------------------------------------------------------------------------------------------------
# response.             | It returns True if the response is the permanent redirected url, otherwise False.
# is_permanent_redirect |
#---------------------------------------------------------------------------------------------------------------
# response.is_redirect	| It returns True if the response was redirected, otherwise False.
#---------------------------------------------------------------------------------------------------------------
# response.iter_content() | It iterates over the response.content.
#---------------------------------------------------------------------------------------------------------------
# response.json()	    | It returns a JSON object of the result (if the result was written in JSON format, if not
#                       | it raises an error).
#---------------------------------------------------------------------------------------------------------------
# response.url	        | It returns the URL of the response.
#---------------------------------------------------------------------------------------------------------------
# response.text	        | It returns the content of the response, in unicode.
#---------------------------------------------------------------------------------------------------------------
# response.status_code	| It returns a number that indicates the status (200 is OK, 404 is Not Found).
#----------------------------------------------------------------------------------------------------------------
# response.request	    | It response.request returns the request object that requested this response.
#---------------------------------------------------------------------------------------------------------------
# response.reason	    | It returns a text corresponding to the status code.
#---------------------------------------------------------------------------------------------------------------
# response.raise_for_status()	| It returns an HTTPError object if an error has occurred during the process.
#---------------------------------------------------------------------------------------------------------------
# response.ok	        | It returns True if status_code is less than 200, otherwise False.
#---------------------------------------------------------------------------------------------------------------
# response.links	    | It returns the header links.
#---------------------------------------------------------------------------------------------------------------


#Authentication using Python Requests
# Authentication refers to giving a user permissions to access a particular resource.
# Since, everyone can’t be allowed to access data from every URL, one would require authentication primarily.
# To achieve this authentication, typically one provides authentication data through Authorization header or a
# custom header defined by server.

#Example

from requests.auth import HTTPBasicAuth

# Making a get request
response = requests.get('https://api.github.com / user, ',auth=HTTPBasicAuth('user', 'pass'))

#Replace “user” and “pass” with your username and password. It will authenticate the request and return a response 200
#or else it will return error 403.

# print request object
print(response)



#SSL Certificate Verification

# Requests verifies SSL certificates for HTTPS requests, just like a web browser.
# SSL Certificates are small data files that digitally bind a cryptographic key to an organization’s details.
# Often, an website with a SSL certificate is termed as secure website. By default, SSL verification is enabled,
# and Requests will throw a SSLError if it’s unable to verify the certificate.

#Let us try to access a website with an invalid SSL certificate, using Python requests

# Making a get request
response = requests.get('https://expired.badssl.com/')

# print request object
print(response)


#one can also pass the link to the certificate for validation via python requests only.
# Making a get request
response = requests.get('https://github.com', verify='/path/to/certfile')

# print request object
print(response)

#This would work in case the path provided is correct for SSL certificate for github.com.

#To disable certificate verification, at the client side, one can use verify attribute.
# Making a get request
response = requests.get('https://expired.badssl.com/', verify=False)

# print request object
print(response)





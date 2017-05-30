# Set up the parameters we want to pass to the API.
# This is the latitude and longitude of New York City.
from urllib2 import Request, urlopen, URLError
import requests
from rapidconnect import RapidConnect
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
f=open("input.txt","r")

s=''
for i in f:
    for word in i:
        s=s+word
f.close()
print s
parameters = {"target": 'hi', "q": s , "key": 'AIzaSyCvA9lwJ2pSdjrsA2rHR93I33k9mgYdjU4'}

# Make a get request with the parameters.
response = requests.get("https://translation.googleapis.com/language/translate/v2", params=parameters)

# Print the content of the response (the data the server returned)
print(response.content)
out=open("output","w")
out.write(response.content)
out.close()


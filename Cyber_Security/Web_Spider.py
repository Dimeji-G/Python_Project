from html.parser import HTMLParser
from urllib.request import urlopen
import urllib

class myParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if (tag == "a"):
            for a in attrs:
                if (a[0] == 'href'):
                    link = a[1]
                    if (link.find('http') >= 0):
                        print (link)
                        newParse = myParser()
                        newParse.feed(link)

url = input ("Enter the URI to spider: ")
#url = "https://droidvilla.com/"
request = urllib.request.urlopen(url)
#request = req.urlopen(url)
parser =  myParser()
parser.feed(str(request.read()))

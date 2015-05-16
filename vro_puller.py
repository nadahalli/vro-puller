from lxml.html import parse
from urllib2 import urlopen
import re

from flask import Flask
app = Flask(__name__)

def vro_puller(id):
    vro_url = 'https://www.valueresearchonline.com/funds/newsnapshot.asp?schemecode=%d' % id
    tree = parse(urlopen(vro_url))
    for node in tree.xpath('//span[@class=\"snapshot-rating\"]/img'):
         return re.search('/funds/fundSelector/img/(.?)Star\.png', node.get('src')).group(1)
    return -1
    
@app.route("/<int:id>")
def hello(id):
    return vro_puller(id)

if __name__ == "__main__":
    app.debug = True
    app.run()

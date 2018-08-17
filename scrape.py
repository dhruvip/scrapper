import requests
import urllib
import os

def save_image(file_name, item_link):
        resource = urllib.request.urlopen(item_link)
        output = open(file_name+".jpg","wb")
        output.write(resource.read())
        output.close()

#save_image('test', 'https://images-eu.ssl-images-amazon.com/images/I/41TwNfZ5LzL._AC_UL260_SR200,260_.jpg')

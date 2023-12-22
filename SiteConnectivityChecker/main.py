# import urllib
# use urllib.request to get the data from the url
# write a function that takes a url
# returns a response

import urllib.request as urllib

def main(url):
    print("checking connetivity....")
    
    resp = urllib.urlopen(url)
    print(f"Connected to {url} successfully")
    print(f"The response code was {resp.getcode()}")


print("This is a site connectivity checker program")
input_url = input("Input the url of the site you want to check: ")

main(input_url)
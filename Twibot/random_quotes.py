#Getting Random Quotes from the API
from time import sleep
import requests

api_url="https://programming-quotes-api.herokuapp.com/Quotes/random"
def get_quote():
    response = requests.get(api_url)
    res = response.json()
    quote = res["en"] + "  " +res["author"]
    
    if len (quote) <= 280:
        return quote
    else:
        quote = quote()
    return quote


    

# #############################################################################

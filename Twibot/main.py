
import tweepy
from credentials import *
from random_quotes import *
import time 

    #Authentication to twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET) 
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    #Creating the API
api = tweepy.API(auth, wait_on_rate_limit=True)

def tweet_quote_today():

    #Creating a tweet
    def tweet_quote():
        api.update_status(get_quote())
    #Make a tweet every day 
    def tweet_quote_daily():
        while True:
            tweet_quote()
            time.sleep(21600)
    return tweet_quote_daily()


        

#Run main
if __name__ == "__main__":
    tweet_quote_today() # Run the program 

# #############################################################################
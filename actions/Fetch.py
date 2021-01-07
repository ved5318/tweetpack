import tweepy
from st2common.runners.base_action import Action

'''__all__ = [
    'GeTweet'
]'''

'''consumer_key = "AyeMkToNVdtICkcXSynim0ASn"
consumer_secret = "ec4ffvb8SLaC79U080hyqWR0oqxWmcNM7iollCuoTrikIfhIbs"
access_key= "786601883691515904-ujfS8pA1yvVm7pNpjNL5qM31JaXnZGq"
access_secret = "3B1tlDerb7EAeF3NdFVcrr3vqWifiX8gzsLYS8h0V6Tdz"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
'''
class Myaction(Action):

    def run(self, username, consumer_key, consumer_secret, access_key, access_secret):
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_key, access_secret)
        api = tweepy.API(auth,wait_on_rate_limit=True)
        for Tweet in api.user_timeline(username):
            text = str(Tweet.text.encode("utf-8"))
            if "Stackstorm" not in text:
                continue
            print(text)    
            return (True, text)
    '''tweets = api.user_timeline(username)
    for tweet in api.search(q="Stackstorm", lang="en", rpp=10):
        return(tweet.text.encode("utf-8"))'''


'''consumer_key = "AyeMkToNVdtICkcXSynim0ASn"
consumer_secret = "ec4ffvb8SLaC79U080hyqWR0oqxWmcNM7iollCuoTrikIfhIbs"
access_key= "786601883691515904-ujfS8pA1yvVm7pNpjNL5qM31JaXnZGq"
access_secret = "3B1tlDerb7EAeF3NdFVcrr3vqWifiX8gzsLYS8h0V6Tdz"
'''

    


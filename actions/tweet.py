import tweepy 
from st2common.runners.base_action import Action

class GeTweet(Action):

    def run(self, message, username, consumer_key, consumer_secret, access_key, access_secret):
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_key, access_secret)
        api = tweepy.API(auth,wait_on_rate_limit=True)
        api.update_status(status = message)   
            return True
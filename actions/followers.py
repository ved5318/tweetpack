import tweepy 
from st2common.runners.base_action import Action
 
class GeTfol(Action):

    def run(self, screen_name, consumer_key, consumer_secret, access_key, access_secret):
        
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_key, access_secret)
        api = tweepy.API(auth,wait_on_rate_limit=True)
        for follower in api.followers(screen_name): 
            print(follower.screen_name)    
        return True
              
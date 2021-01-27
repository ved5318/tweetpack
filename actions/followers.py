import tweepy 
from st2common.runners.base_action import Action
# assign the values accordingly 
# consumer_key = "AyeMkToNVdtICkcXSynim0ASn"
# consumer_secret = "ec4ffvb8SLaC79U080hyqWR0oqxWmcNM7iollCuoTrikIfhIbs"
# access_key= "786601883691515904-ujfS8pA1yvVm7pNpjNL5qM31JaXnZGq"
# access_secret = "3B1tlDerb7EAeF3NdFVcrr3vqWifiX8gzsLYS8h0V6Tdz"
  
# # authorization of consumer key and consumer secret 
# auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
  
# # set access to user's access key and access secret  
# auth.set_access_token(access_key, access_secret) 
  
# # calling the api  
# api = tweepy.API(auth) 
  
# # the screen_name of the targeted user 
# screen_name = "@vedprakash531"
  
# # printing the latest 20 followers of the user 
# for follower in api.followers(screen_name): 
#     print(follower.screen_name) 
class GeTfol(Action):

    def run(self, screen_name, consumer_key, consumer_secret, access_key, access_secret):
        
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_key, access_secret)
        api = tweepy.API(auth,wait_on_rate_limit=True)
        for follower in api.followers(screen_name): 
            print(follower.screen_name)    
        return True
              
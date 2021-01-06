import tweepy
import json
import requests
from Fetch import text
from st2common.runners.base_action import Action

'''consumer_key = ""
consumer_secret = ""
access_key= ""
access_secret = ""
username = ""'''

'''consumer_key = "AyeMkToNVdtICkcXSynim0ASn"
consumer_secret = "ec4ffvb8SLaC79U080hyqWR0oqxWmcNM7iollCuoTrikIfhIbs"
access_key= "786601883691515904-ujfS8pA1yvVm7pNpjNL5qM31JaXnZGq"
access_secret = "3B1tlDerb7EAeF3NdFVcrr3vqWifiX8gzsLYS8h0V6Tdz"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

username = "@vedprakash531"'''
class Myaction(Action):

    def run(self):
        url = "https://hooks.slack.com/services/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"
        payload = {"text": text }
        r = requests.post(url, data=json.dumps(payload))
        print(r.text)
        return(True, r.text)
        '''auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_key, access_secret)
        api = tweepy.API(auth,wait_on_rate_limit=True)
        for Tweet in api.user_timeline(username):
            text = str(Tweet.text.encode("utf-8"))
            if "Stackstorm" not in text:
                continue'''    
            
#print(run(username))
'''def notify_slack(text):
  url = "https://hooks.slack.com/services/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"
  payload = {"text": text }
  r = requests.post(url, data=json.dumps(payload))
  print(r.text)


class TweetListener(StreamListener):

  def on_data(self, data):
    tweet = api.user_timeline(username)
    tweet = json.loads(data)
    notify_slack(tweet['text'])
    return True
    def on_error(self, status):
      print("Error: %s" % status)


listener = TweetListener()
auth = OAuthHandler(consumer_key , consumer_secret)
auth.set_access_token(access_key, access_secret)

stream = Stream(auth, listener)
stream.filter(track=['stackstorm'])'''
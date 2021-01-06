import tweepy
import json
import requests
from Fetch import text
from st2common.runners.base_action import Action

username = "@vedprakash531"
class Myaction(Action):

    def run(self):
        url = "https://hooks.slack.com/services/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"
        payload = {"text": text }
        r = requests.post(url, data=json.dumps(payload))
        print(r.text)
        return(True, r.text)   
            
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
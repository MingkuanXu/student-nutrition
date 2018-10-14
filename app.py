import tweepy
import wget

consumer_key = "IcGlRhFdmCBNYrrxJe42rG8X0"
consumer_secret = "mLK6PAIgRaAlhfnWMjCAH1HyQD5vQMgXtREAukSNThXxCuwpFq"
access_token = '1388376492-6rr3u1KbSjvoKTbQWWkmTyynqBfw7L6GnREQer5'
token_secret = '55DpiudGed4FQ6iYCT453MynH2x7ezfkj2lgfikmLr3QD'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret )
auth.set_access_token(access_token, token_secret)

""" token = session.get('request_token')
session.delete('request_token')
auth.request_token = token

key = auth.access_token
secret = auth.access_token_secret

try:
    auth.get_access_token(verifier)
except tweepy.TweepError:
    print 'Error! Failed to get access token.' """


api = tweepy.API(auth)

class MyStreamListener(tweepy.StreamListener):

    def onStatus(self, status):
        return status.text


tweets = api.user_timeline(screen_name='stutrition',
    count=5, include_rts=False,
    exclude_replies=False)
last_id = tweets[-1].id

 
while (True):
    more_tweets = api.user_timeline(screen_name='stutrition',
    count=5,
    include_rts=False,
    exclude_replies=False,
    max_id=last_id-1)

    # There are no more tweets
    if (len(more_tweets) == 0):
        break
    else:
        last_id = more_tweets[-1].id-1
        tweets = tweets + more_tweets

media_files = set()
for status in tweets:
    media = status.entities.get('media', [])
    if(len(media) > 0):
        media_files.add(media[0]['media_url'])

for media_file in media_files:
    wget.download(media_file)
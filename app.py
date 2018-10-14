import tweepy

consumer_key = 'sJ54pjXvx5pc5SXTM6wAabgl7'
consumer_secret = 'AqHSZ1YD9DXIm3vaPeF95DMRMhcmn93bqhaKdOWtqFIdvoMhKc'
access_token = '1388376492-6rr3u1KbSjvoKTbQWWkmTyynqBfw7L6GnREQer5'
token_secret = '55DpiudGed4FQ6iYCT453MynH2x7ezfkj2lgfikmLr3QD '

auth = tweepy.OAuthHandler(consumer_key, consumer_secret )

# Redirect user to Twitter to authorize
redirect_user(auth.get_authorization_url())

# Get access token
auth.get_access_token("verifier_value")

# Construct the API instance
api = tweepy.API(auth)

""" token = session.get('request_token')
session.delete('request_token')
auth.request_token = token

key = auth.access_token
secret = auth.access_token_secret

try:
    auth.get_access_token(verifier)
except tweepy.TweepError:
    print 'Error! Failed to get access token.' """


api.update_status('hacking')

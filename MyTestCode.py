import tweepy

consumer_key = 'you should use your token and keys'
consumer_secret = 'you should use your token and keys'
access_token = 'you should use your token and keys'
access_token_secret = 'you should use your token and keys'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#tweet = 'Hello, world!'
#api.update_status(status=tweet)

#Find 
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
    print()

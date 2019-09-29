import tweepy

consumer_key = "ck"
consumer_secret = "cs"
access_key = "ak"
access_secret = "as"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

#tweet = 'Hello, world!'
#api.update_status(status=tweet)

#Find 
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
    print()

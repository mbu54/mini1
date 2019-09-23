import tweepy

consumer_key = "lYmWSI2ENc88tLXxZSopPGxBi"
consumer_secret = "lPBR9EHewblDyL9qelcIcNVY7y13FI546mUk7sP3WayXmGbQBT"
access_key = "1174513228434612224-FZb71pFwevK4TBUOVEHcTFFGmYBufT"
access_secret = "Sh3sxKlSYcRjVQiSs3i9gOidJjNeKNLkP60yof8HzvbpA"

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

 tweepy
import os
import tweepy as tw
import pandas as pd

#Twitter API credentials
consumer_key = "..."
consumer_secret = "..."
access_key = "..."
access_secret = "..."

def get_tweet(username):
  twitter_feed = []
  # Authorize 
  auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_key,access_secret)
  auth_tweet = tweepy.API(auth)
  Someone_tweets = auth_tweet.user_timeline(screen_name=username,count=50)
  for tweet in Someone_tweets:
    twitter_feed = twitter_feed + [tweet.text]
  return importtwitter_feed

#print(twitter_ano)

def hashtags(search_words,date_since):
# Authorize 
  twitter_emp = []
  
  auth = tw.OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_key,access_secret)
  api = tw.API(auth, wait_on_rate_limit=True)
  tweets = tw.Cursor(api.search,q=search_words,lang="en",since=date_since).items(50)
  # Iterate and print tweets
  for tweet_tag in tweets:
    #twitter_ctime=twitter_emp+[tweet_tag.created_at]
    twitter_emp=twitter_emp+[tweet_tag.text]
  return twitter_emp
  
def hashtags_ctime(search_words,date_since):
# Authorize 
  twitter_ctime=[]
  auth = tw.OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_key,access_secret)
  api = tw.API(auth, wait_on_rate_limit=True)
  tweets = tw.Cursor(api.search,q=search_words,lang="en",since=date_since).items(50)
  # Iterate and print tweets
  for tweet_tag in tweets:
    #twitter_ctime=twitter_emp+[tweet_tag.created_at]
    twitter_ctime=twitter_ctime+[tweet_tag.created_at]
  return twitter_ctime

#Content for sb Timeline
twitter_results=get_tweet("@realDonaldTrump") 

#Content for Harhstags
wanted_words = "#wildfires"
wangted_date_since = "2018-11-16"
twiter_tag_content=hashtags(wanted_words,wangted_date_since)
twitter_created_time=hashtags_ctime(wanted_words,wangted_date_since)
print(twitter_created_time)
#strip http for sb  
twitter_ano1=[]
for s in twitter_results:
  if s.find('https')>0:
    s=s[0:s.find('https')-1]
    #print(s)
    twitter_ano1.append(s)

#strip http for hashtags
twitter_ano2=[]
for s in twiter_tag_content:
  if s.find('https')>0:
    s=s[0:s.find('https')-1]
    #print(s)
    twitter_ano2.append(s)
#print(twitter_ano2)

#strip datetime.datetime for hashtags
twitter_ano3=[]
for s in twitter_created_time:
  print (type(s))
  #if s.find(' datetime.datetime')>0:
   # s=s[0:s.find(' datetime.datetime')-1]
    #print(s)
    #twitter_ano3.append(s)

#print(twitter_ano3)

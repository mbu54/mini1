# time entry for twitter

import tweepy as tw
import os
import pandas as pd
import twitter_codes as codes

#Twitter API credentials
consumer_key = codes.ck
consumer_secret = codes.cs
access_key = codes.ak
access_secret = codes.ac

def get_tweet(username):
  twitter_feed = []
  twitter_feed_time = []
  # Authorize 
  auth = tw.OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_key,access_secret)
  auth_tweet = tw.API(auth)
  Someone_tweets = auth_tweet.user_timeline(screen_name=username,count=10,tweet_mode="extended")
  for tweet in Someone_tweets:
    if "retweeted_status" in tweet._json:
      twitter_feed = twitter_feed + [tweet._json["retweeted_status"]["full_text"]]
      twitter_feed_time = twitter_feed_time + [tweet.created_at]
    else:
      twitter_feed = twitter_feed + [tweet.full_text]
      twitter_feed_time = twitter_feed_time + [tweet.created_at]
  return twitter_feed, twitter_feed_time

#print(twitter_ano)

def hashtags(search_words,date_since,date_until):
# Authorize 
  twitter_emp = []
  
  auth = tw.OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_key,access_secret)
  api = tw.API(auth, wait_on_rate_limit=True)
  tweets = tw.Cursor(api.search,q=search_words,lang="en",since=date_since,until=date_until,tweet_mode="extended").items(10)
  # Iterate and print tweets
  for tweet_tag in tweets:
    if "retweeted_status" in tweet_tag._json:
      twitter_emp = twitter_emp + [tweet_tag._json["retweeted_status"]["full_text"]]
    else:
      twitter_emp=twitter_emp+[tweet_tag.full_text]
  return twitter_emp
  
def hashtags_ctime(search_words,date_since,date_until):
# Authorize 
  twitter_ctime=[]
  auth = tw.OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_key,access_secret)
  api = tw.API(auth, wait_on_rate_limit=True)
  tweets = tw.Cursor(api.search,q=search_words,lang="en",since=date_since,until=date_until).items(10)
  # Iterate and print tweets
  for tweet_tag in tweets:
    #twitter_ctime=twitter_emp+[tweet_tag.created_at]
    twitter_ctime=twitter_ctime+[tweet_tag.created_at]
  return twitter_ctime

#Content for sb Timeline
twitter_results,twitter_results_time=get_tweet("@realDonaldTrump") 
'''
for i in range(10):
  print(i, ":",twitter_results[i])
'''

#Content for Harhstags
wanted_words = "#trump"
wangted_date_since = "2019-09-27"
wangted_date_until = "2019-09-28"
twitter_tag_content=hashtags(wanted_words,wangted_date_since,wangted_date_until)
twitter_created_time=hashtags_ctime(wanted_words,wangted_date_since,wangted_date_until)
#print(twitter_created_time)
#strip http for sb  
i = 0
for s in twitter_results:
  if s.find('https')>=0:
    s=s[0:s.find('https')]
    #print(s)
    twitter_results[i] = s
  i += 1
#strip # signs
i = 0
for s in twitter_results:
  twitter_results[i] = s.replace("#","")
  i += 1
#strip @ signs
i = 0
for s in twitter_results:
  twitter_results[i] = s.replace("@","")
  i += 1

for i in range(len(twitter_results)):
  print(i,':',twitter_results_time[i],':',twitter_results[i])
  print()

#strip http for hashtags
i = 0
for s in twitter_tag_content:
  if s.find('https')>=0:
    s=s[0:s.find('https')-1]
    #print(s)
    twitter_tag_content[i] = s
  i += 1
#strip # signs
i = 0
for s in twitter_tag_content:
  twitter_tag_content[i] = s.replace("#","")
  i += 1
#strip @ signs
i = 0
for s in twitter_tag_content:
  twitter_tag_content[i] = s.replace("@","")
  i += 1
'''
for i in range(len(twitter_tag_content)):
  print(i,twitter_tag_content[i])
  print()
'''

#strip datetime.datetime for hashtags
twitter_ano3=[]
for s in twitter_created_time:
  #print (s)
  twitter_ano3.append(s)
  #if s.find(' datetime.datetime')>0:
   # s=s[0:s.find(' datetime.datetime')-1]
    #print(s)
    #twitter_ano3.append(s)
#print(type(twitter_ano3))

#print(twitter_ano3)
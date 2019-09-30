# twitter functions

import tweepy as tw
import os
import pandas as pd
from pandas.plotting import register_matplotlib_converters
import twitter_codes as codes
from google.cloud import language_v1
from google.cloud.language_v1 import enums
import six
import matplotlib.pyplot as plt
import datetime

register_matplotlib_converters(explicit = True)
#Twitter API credentials
consumer_key = codes.ck
consumer_secret = codes.cs
access_key = codes.ak
access_secret = codes.ac

def get_tweet(username,num_tweets):
  twitter_feed = []
  twitter_feed_time = []
  # Authorize 
  auth = tw.OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_key,access_secret)
  auth_tweet = tw.API(auth)
  Someone_tweets = auth_tweet.user_timeline(screen_name=username,count=num_tweets,tweet_mode="extended")
  for tweet in Someone_tweets:
    if "retweeted_status" in tweet._json:
      twitter_feed = twitter_feed + [tweet._json["retweeted_status"]["full_text"]]
      twitter_feed_time = twitter_feed_time + [tweet.created_at]
    else:
      twitter_feed = twitter_feed + [tweet.full_text]
      twitter_feed_time = twitter_feed_time + [tweet.created_at]
  return twitter_feed, twitter_feed_time


def hashtags(search_words,date_since,date_until):
  twitter_feed = []
  twitter_feed_time = []
  # Authorize
  auth = tw.OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_key,access_secret)
  api = tw.API(auth, wait_on_rate_limit=True)
  tweets = tw.Cursor(api.search,q=search_words,lang="en",since=date_since,until=date_until,tweet_mode="extended").items(10)
  # Iterate and print tweets
  for tweet in tweets:
    if "retweeted_status" in tweet._json:
      twitter_feed = twitter_feed + [tweet._json["retweeted_status"]["full_text"]]
      twitter_feed_time = twitter_feed_time + [tweet.created_at]
    else:
      twitter_feed=twitter_feed+[tweet.full_text]
      twitter_feed_time = twitter_feed_time + [tweet.created_at]
  return twitter_feed,twitter_feed_time
  
def handletweets(handle, num_tweets):
  tweet_out = []
  tweet_out_time = []
  twitter_results,twitter_results_time=get_tweet(handle, num_tweets) 
  i = 0
  #strip links 
  for s in twitter_results:
    if s.find('https')>=0:
      s=s[0:s.find('https')]
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
  # remove empty tweets after cleaning
  i = 0
  for s in twitter_results:
    if len(s) != 0:
      tweet_out.append(s)
      tweet_out_time.append(twitter_results_time[i])
    i += 1
  '''
  for i in range(len(twitter_results)):
    print(i,':',twitter_results_time[i],':',twitter_results[i])
    print()
  '''
  return tweet_out,tweet_out_time


def hashtagtweets(hash_tag,wanted_date_since,wanted_date_until):
  twitter_tag_content,twitter_tag_content_time=hashtags(hash_tag,wanted_date_since,wanted_date_until) 
  # strip links
  i = 0
  for s in twitter_tag_content:
    if s.find('https')>=0:
      s=s[0:s.find('https')-1]
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
    print(i,':',twitter_tag_content_time[i],':',twitter_tag_content[i])
    print()
  '''
  return twitter_tag_content, twitter_tag_content_time

def sentiment_analysis(content):

  client = language_v1.LanguageServiceClient()

  # content = 'Your text to analyze, e.g. Hello, world!'

  if isinstance(content, six.binary_type):
    content = content.decode('utf-8')

  type_ = enums.Document.Type.PLAIN_TEXT
  document = {'type': type_, 'content': content}

  response = client.analyze_sentiment(document)
  sentiment = response.document_sentiment
  return sentiment.score
  #print('Score: {}'.format(sentiment.score))
  #print('Magnitude: {}'.format(sentiment.magnitude))

def get_sentiment(text_list):
  sentiment_list = []

  for i in range(len(text_list)):
    sentiment_list.append(sentiment_analysis(text_list[i]))

  return sentiment_list


handle = "@BarackObama" #CHANGE THIS
number_tweets = 50 #CHANGE THIS
'''
hash_tag = "#trump"
wanted_date_since = "2019-09-27"
wanted_date_until = "2019-09-28"
'''
tweet_text,tweet_time = handletweets(handle, number_tweets)
tweet_sentiment = get_sentiment(tweet_text)

#tweet_text2,tweet_time2 = hashtagtweets(hash_tag,wanted_date_since,wanted_date_until)
'''
for i in range(len(tweet_text)):
  print(tweet_time[i], ":", tweet_text[i])
  print(tweet_time[i], ":", tweet_sentiment[i])
  print()
'''
sentiment_mean = sum(tweet_sentiment)/len(tweet_sentiment)
print("The average sentiment of",handle, "over the last",number_tweets,"tweets is",sentiment_mean)
# plot the sentiment
fig, ax = plt.subplots()
plt.plot_date(tweet_time, tweet_sentiment)
ax.xaxis.set_tick_params(rotation=30, labelsize=10)
plt.xlabel("Time of Tweet")
plt.ylabel("Google Sentiment")

plt.show()
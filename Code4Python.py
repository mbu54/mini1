import tweepy

#Twitter API credentials
consumer_key = "epSN7DLvzimhRPbFikys8n1Vb"
consumer_secret = "r6MnsK1VLPnSopb9RUakdKvqHGW0WfVbqqiicfX6ZofJrJvzlO"
access_key = "1171550663857332226-VOPUcYhjRmVD9KnaNp8PUtC8ABMWkw"
access_secret = "pQVMIyzT354TbGfwH99g1f0j2K29ZpesLZZ4wXYdGvQtG"

def get_tweet():
  twitter_feed = []
  # Authorize 
  auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_key,access_secret)
  auth_tweet = tweepy.API(auth)
  public_tweets = auth_tweet.home_timeline()
  for tweet in public_tweets:
    twitter_feed = twitter_feed + [tweet.text]
  return twitter_feed

twitter_feed=get_tweet()  
twitter_ano=[]
for s in twitter_feed:
  if s.find('https')>0:
    s=s[0:s.find('https')-1]
    #print(s)
    twitter_ano.append(s)

print(twitter_ano)





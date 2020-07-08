import tweepy
import time
import csv
import pandas as pd

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
tweets_text  = tweepy.Cursor(api.search,q="blacklivesmatter -filter:retweets",result_type="popular",count=5,lang='en',tweet_mode='extended').items(5)

tweets_dict ={}
tweets_no = 0

for tweet in tweets_text:
    tweet.full_text = [x for x in tweet.full_text.split(' ')[:-1]]
    tweet.full_text = ' '.join(tweet.full_text)
    print (tweet.user.name,tweet.created_at, tweet.full_text)
    tweets_no += 1
    tweets_dict[tweets_no] = [tweet.user.name,tweet.created_at, tweet.full_text]
df = pd.DataFrame.from_dict(tweets_dict,orient='index',columns=['name','tweet'])
df.to_csv('tweet.csv',index=False,encoding='utf-8-sig')

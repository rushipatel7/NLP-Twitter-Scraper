import tweepy
import time
import csv
import pandas as pd
consumer_key = "kDLqXCiWUxPdsiu5rTFu0Ektu"
consumer_secret = "YaQVmi3jP4xNsjttWLBi4AGlhsduqlqYxM04ao3vIbLqbMlVQH"
access_token = "1083760447604453376-gnnhJutuddhffgtIDy2sxR3q79biuX"
access_token_secret = "5iqN6mrcQSBizSROcE3Lhtet1EJcklkgVT9ZeXRngQUBi"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
tweets_text  = tweepy.Cursor(api.search,q="blacklivesmatter",count=50,lang='en',since="2017-04-03").items(50)
# csvFile = open('tweets.csv', 'a')
# csvWriter = csv.writer(csvFile)

tweets_dict ={}
tweets_no = 0
for tweet in tweets_text:
    print (tweet.created_at, tweet.text)
    
    tweets_no += 1
    tweets_dict[tweets_no] = [tweet.created_at, tweet.text]

df = pd.DataFrame.from_dict(tweets_dict,orient='index',columns=['name','tweet'])
df.to_csv('scrape-data')




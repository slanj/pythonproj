import json
import os
import re
import csv
import time
import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

# Variables that contains the user credentials to access Twitter API
with open('secret') as f:
    secret = json.loads(f.read())

consumer_key = secret['consumer_key']
consumer_secret = secret['consumer_secret']
access_token = secret['access_token']
access_token_secret = secret['access_token_secret']

# This is a basic listener that just prints received tweets to stdout.
def body_cleanup(text):
    # Here you can put any pre-processing routines
    return text

def preproc(tweet):
    txt = body_cleanup(tweet['text'])
    data = {'text': txt, 'src': 'twitter'}
    if 'coordinates' in tweet:
        data['coordinates'] = tweet['coordinates']
    if 'place' in tweet:
        data['place'] = tweet['place']
    if 'created_at' in tweet:
        time_struct = time.strptime(tweet['created_at'], "%a %b %d %H:%M:%S +0000 %Y")
        data['created_at'] = int(time.mktime(time_struct))
    to_prn = json.dumps(data)
    return to_prn, data

class StdOutListener(StreamListener):
    ''' Handles data received from the stream. '''

    def __init__(self):
        StreamListener.__init__(self)
        self.base = open('twitbase.tsv', 'a+', encoding='utf-8')
        self.tsv_writer = csv.writer(self.base, delimiter='\t')
        if os.stat("twitbase.tsv").st_size == 0:
            self.tsv_writer.writerow(['text', 'src', 'coordinates', 'place', 'created_at'])

    def on_data(self, data):
        tweet = json.loads(data)
        # Prints the text of the tweet
        if 'text' in tweet:
            for_print, for_db = preproc(tweet)
            print(for_print)
            self.save_row(for_db)
        return True

    def save_row(self, row):
        to_save = []
        for item in row:
            to_save.append(row[item])
        self.tsv_writer.writerow(to_save)

    def on_error(self, status_code):
        print('Got an error with status code: ' + str(status_code))
        return True # To continue listening

    def on_timeout(self):
        print('Timeout...')
        return True # To continue listening


# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Creation of the actual interface, using authentication
api = tweepy.API(auth)

listener = StdOutListener()
stream = Stream(auth, listener)
stream.filter(track=['#ai', '#ml'], languages=['en'])
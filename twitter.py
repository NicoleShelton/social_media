import tweepy
import os

ckey = os.environ['api_key']
csecret = os.environ['api_secret']
atoken = os.environ['access_token_key']
asecret = os.environ['access_token_secret']

OAUTH_KEYS = {'consumer_key': ckey,
            'consumer_secret': csecret,
            'access_token_key': atoken,
            'access_token_secret': asecret}
auth = tweepy.OAuthHandler(OAUTH_KEYS['consumer_key'],
                        OAUTH_KEYS['consumer_secret'])
api = tweepy.API(auth)

def posts(hashtag, num_items):

    cricTweet = tweepy.Cursor(api.search, q=hashtag).items(num_items)

    return list(cricTweet)

def get_html(id):
    cricTweet = api.get_oembed(id=id)['html']

    return cricTweet
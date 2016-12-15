import tweepy

ckey = "7WIPrVysPZD4NM5UtMXWmDyTq"
csecret = "HvZJjJcpsZ6uVl0TWySq1keR45XrYJgIeAtU17XrB79ZKiuB7k"
atoken = "808326668213436416-DEQ09Y2Jx9zpTLDtkPPNXadLPIS1i28"
asecret = "kjedNjuX84ShbJuJEZHketCTMylbp3RzGxFwJNmCGTJNe"

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
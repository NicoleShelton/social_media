import tweepy, os
from random import choice
from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

quotes = """Life is happening for you, Not to you. -Unknown
It always seems impossible until it's done. -Nelson Mandela
If you can dream it, you can do it. -Walt Disney
Quality is not an act, it is a habbit -Aristotle
The secret of getting ahead is getting started. -Mark Twain
Don't watch the clock; do what it does. Keep going. -Sam Levenson
What you do today can improve all your tomorrows. -Ralph Marston
Problems are not stop signs, they are guidelines. -Robert H. Schuller
Accept the challenges so that you can feel the exhilaration of victory. -George S. Patton
You cannot have a positive life and a negative mind. -Joyce Meryer
Keep your face to the sunshine and you cannot see a shadow. -Helen Keller
What did the sea say to the sand? Nothing it simply waved.
Why don't teddy bears ever really eat at their picnics? Because their already stuffed.
Why was the toilet paper rolling down the mountain? To get to the bottom.
Apparently taking a day off is not something you should do when you work for a calendar company.
I wondered why the baseball was getting bigger, then it hit me.
Why don't some couples go to the gym? Because some relationships don't work out.
So what if I don't know what apocalypse means!? It's not the end of the world.
Need an ark to save 2 of every animal? I noah guy.
When Peter Pan punches, they Neverland.
I use to have a fear of hurdles, but I got over it.""".split("\n")

ckey = os.environ['api_key']
csecret = os.environ['api_secret']
atoken = os.environ['access_token_key']
asecret = os.environ['access_token_secret']
auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
api = tweepy.API(auth)

@sched.scheduled_job('cron', day_of_week='mon-fri', hour=16)
def daily_post():
    line = choice(quotes)
    api.update_status(line)

sched.start()
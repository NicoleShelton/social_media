from flask import Flask, request
import os
from twitter import posts, get_html

app = Flask(__name__)


@app.route('/')
def root():
    return open('static/twitter.html').read()


@app.route("/get_tweets/")
def get_tweets():
    tag = request.values.get('tag', 'cat')
    tweets = posts(tag, 20)
    s = """<link href="https://fonts.googleapis.com/css?family=Shadows+Into+Light" rel="stylesheet"> 
    <link href='/static/twitter.css' rel='stylesheet'>
    <h1>Twitter Posts</h1>
    <table>"""
    # s += '\n'.join(
    #     '<tr><td>{}</td></tr>'.format(get_html(t.id)) for t in tweets)
    x = '<tr>' # initialize new string of table data
    for i in range(len(tweets)):  # iterate over length of the tweet list by index
        x += '<td>{}</td>'.format(get_html(tweets[i].id, 1/100)) # tweets[i] is single tweet data
        if i % 3 == 2: 
            x += '</tr><tr>' # every three items closes row and opens new one
    x += '</tr>' # closes table data string
    s += x  # concatenate table data with rest of html
    s += '</table>'
    return s


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
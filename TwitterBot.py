#!/usr/bin/env python
import sys
import praw
from twython import Twython


#Constant vars for accessing PRAW and the Twitter API
#Twitter API constants
CONSUMER_KEY = 'BkqDnu2faXUu1ruxoeftABiZf'
CONSUMER_SECRET = 's9vlxR0nN4b3gy8zM8gLE3ZPxdXZPhZ3lOUhkpVqNxKkuQRbcX'
ACCESS_KEY = '1215100225259479040-HEKO1mLUz3ySBzD900EjUpQ6LuZUf5'
ACCESS_SECRET = '9c20iwxQCa6RcHCjcgide5iL4T7yRRyfGz74oMQFCRwIe'

#PRAW constants
CLIENT_ID = 'mi0i5MOCS5aAdw'
CLIENT_SECRET = 'udwboa3H0NNqtkrD_5m5YMYw7dY'
USER_AGENT = 'Pi Bot.v.1'

reddit = praw.Reddit(client_id = CLIENT_ID,
                     client_secret = CLIENT_SECRET,
                     user_agent = USER_AGENT)
print(reddit.read_only)
#Create a copy of the Twython object with all our keys and secrets to allow easy commands.
twitter = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET) 

#Using our newly created object, utilize the update_status to send in the text passed in through CMD
#twitter.update_status(status=sys.argv[1])

#Grab top hot submission from r/politics
subreddit = reddit.subreddit('politics')
for submission in subreddit.hot(limit=1):
    url = (submission.url)
    twitter.update_status(status = url)
    print("succesfully tweeted URL") 


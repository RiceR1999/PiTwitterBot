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

#Initilize the python wrapper for the reddit API
reddit = praw.Reddit(client_id = CLIENT_ID,
                     client_secret = CLIENT_SECRET,
                     user_agent = USER_AGENT)

#Did we sucessfully initilize?
print("Reddit api init: "+ str(reddit.read_only))

#Create a copy of the Twython object with all our keys and secrets to allow easy commands.
twitter = Twython(CONSUMER_KEY,
                  CONSUMER_SECRET,
                  ACCESS_KEY,
                  ACCESS_SECRET) 

#Did we successfully initilize?
print("Twitter api init: " + str(bool(twitter.verify_credentials()))) 



#Grab top hot submission from r/politics ignoring pinned posts by moderators
subreddit = reddit.subreddit('politics')
mods = []
for moderator in subreddit.moderator():
    mods.append(moderator.name)

#Post a status update including the posts URL and title
for submission in subreddit.hot(limit=3):
        if submission.author.name in mods:
            print("author is a r/politics mod, skipping submission")
        else: 
            url = (submission.url)
            twitter.update_status(status = url + str(submission.title))
            print("succesfully tweeted URL")

#!/usr/bin/env python
import sys
import praw
from twython import Twython

#Define our constant variables, this is all the data we wrote down in the first part of the tutorial.
CONSUMER_KEY = 'BkqDnu2faXUu1ruxoeftABiZf'
CONSUMER_SECRET = 's9vlxR0nN4b3gy8zM8gLE3ZPxdXZPhZ3lOUhkpVqNxKkuQRbcX'
ACCESS_KEY = '1215100225259479040-HEKO1mLUz3ySBzD900EjUpQ6LuZUf5'
ACCESS_SECRET = '9c20iwxQCa6RcHCjcgide5iL4T7yRRyfGz74oMQFCRwIe'

#Create a copy of the Twython object with all our keys and secrets to allow easy commands.
api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET) 

#Using our newly created object, utilize the update_status to send in the text passed in through CMD
api.update_status(status=sys.argv[1])

#Iterate through a subreddit and print submission titles
for submission in reddit.:

#!/usr/bin/env python
import sys
import praw
import time
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
print(time.ctime() + ":" + " Reddit api init: "+ str(reddit.read_only))

#Create a copy of the Twython object with all our keys and secrets to allow easy commands.
twitter = Twython(CONSUMER_KEY,
                  CONSUMER_SECRET,
                  ACCESS_KEY,
                  ACCESS_SECRET) 

#Did we successfully initilize?
print(time.ctime() + ":" + " Twitter api init: " + str(bool(twitter.verify_credentials()))) 



#Grab top hot submission from r/politics ignoring pinned posts by moderators
print(time.ctime() + ":" + " r/poliBOT is ready to initilize, do you want to continue (y/n): ")
runString = sys.stdin.readline()
runString = runString.strip()

print("\n")

subreddit = reddit.subreddit('politics')
mods = []
currentSub = []
first = True

def check_new_posts():
    for submission in subreddit.hot(limit=3):
        if submission.author.name in mods:
            print(time.ctime() + ':' + " author is a r/politics mod, skipping submission")
        elif first is True:
            currentSub.insert(0,submission)
            url = (submission.permalink)
            twitter.update_status(status = str(submission.title) + ' ' + submission.url)
            print(time.ctime() + ':' + " succesfully tweeted initial submission!")
        elif submission not in currentSub:
            currentSub.insert(0,submission)
            currentSub.pop()
            url = (submission.permalink)
            twitter.update_status(status = str(submission.title) + ' ' + submission.url)
            print(time.ctime() + ':' + " succesfully tweeted new submission!")
        else:
            print(time.ctime() + ':' +  " no new submissions since last check....")

def populate_modlist():
    for moderator in subreddit.moderator():
        mods.append(moderator.name)

if runString is 'y':

    while runString == 'y':
      try:
          if first == True:
              populate_modlist()
              check_new_posts()
              time.sleep(60)
              print('\n')
              first = False
          else:
              check_new_posts()
              time.sleep(60)
              print('\n')
              
      except KeyboardInterrupt:
          print("Keyboard interruption, r/poliBOT shutting down....")
          exit()
      except Exception as e:
          print('Error:', e)
          time.sleep(5)
    
else:
 print("r/poliBOT exiting with no initilization.")
 exit()




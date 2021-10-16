# AtaturkQuoteBot v3.9 by MrZpzp

import praw
import quotesl
import photosl
import time
import os
import random


def login():
    print("Logging in...")
    #Fill here
    reddit = praw.Reddit(client_id="my client id",
                         client_secret="my client secret",
                         user_agent="my user agent",
                         username="username",
                         password="password",
                        )
    print("Logged in!")

    return reddit


def reply(p_type):
  
  choose_from = random.choice([photosl.photos, quotesl.quotes])

  print("Related words found in " + 
                    p_type.id)

  if choose_from is quotesl.quotes:
    random_index = random.randint(0, len(quotesl.quotes) - 1)

    p_type.reply(choose_from[random_index] + " \n\n "
                                    "*-M.Kemal Atatürk* \n\n "
                                    "^(I am a bot and this action was performed automatically.)" + "\n\n" + "[INFO|BİLGİ](https://www.reddit.com/user/mkemalataturk/comments/pcp0q0/ataturkquotebot_says_hellooo/)")
  else:
    random_index2 = random.randint(0, len(photosl.photos) - 1)

    p_type.reply("Merhaba ben bir botum ve paylaşımında 'Atatürk' geçtiği için geldim.Senin için bir tane " + choose_from[random_index2] + " paylaştım. "+ " \n\n "
                                                    
                                    "^(I am a bot and this action was performed automatically.)" + "\n\n" + "[INFO|BİLGİ](https://www.reddit.com/user/mkemalataturk/comments/pcp0q0/ataturkquotebot_says_hellooo/)")
            

  print("Replied to " + p_type.id)


def main(reddit):

  subreddit = reddit.subreddit('Ata+Turkey+TurkeyJerky+KGBTR+ArsivUnutmaz+AteistTurk+BLKGM+Turkmenistan+Otuken+MuslumanTurk+Tiele')
      
  print("Collecting  last 3 mentions,last 50 comments and last 10 posts from new...")

  time.sleep(1)
  for mention in reddit.inbox.mentions(limit = 3):
    if  mention.new and mention.author != reddit.user.me():
      mention.mark_read()
      time.sleep(1)
      reply(mention)
  
      
  for submission in subreddit.new(limit=10):
    submission_lower = submission.title.lower()
    if submission.score >= 7:
        
      if "atatürk" in submission_lower and submission.saved is False and submission.author != reddit.user.me():
        time.sleep(1)
        reply(submission)
        submission.save()


  for comment in subreddit.comments(limit=50):
    comment_lower = comment.body.lower()
    if comment.score >= 5:
      
      if "atatürk" in comment_lower and comment.saved is False and comment.author != reddit.user.me():
        time.sleep(1)
        reply(comment)  
        comment.save()

        
  print("Collect Completed.")

  print("Sleeping for 300 seconds...")
  time.sleep(300)

 
reddit = login()


while True:
  try:
    main(reddit)
  except Exception as e:
    print(str(e) + " ,sleeping 120 seconds...")
    time.sleep(120)

# "Bilim, gerçeği bilmektir." -M.Kemal Atatürk

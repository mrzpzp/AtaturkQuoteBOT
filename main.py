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

def get_saved_comments():
    if not os.path.isfile("replied_to.txt"):
        replied_to = []
    else:
        with open("replied_to.txt", "r") as f:
            replied_to = f.read()
            replied_to = replied_to.split("\n")
            replied_to = list(filter(None, replied_to))

    return replied_to

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

    p_type.reply("Merhaba ben bir botum ve paylaşımında 'Atatürk'geçtiği için geldim.Senin için bir tane " + choose_from[random_index2] + " paylaştım. "+ " \n\n "
                                                    
                                    "^(I am a bot and this action was performed automatically.)" + "\n\n" + "[INFO|BİLGİ](https://www.reddit.com/user/mkemalataturk/comments/pcp0q0/ataturkquotebot_says_hellooo/)")
            

  print("Replied to " + p_type.id)

  replied_to.append(p_type.id)

  with open("replied_to.txt", "a") as f:
    f.write(p_type.id + "\n")
      

def main(reddit, replied_to):

  subreddit = reddit.subreddit('Ata+Turkey+TurkeyJerky+KGBTR+ArsivUnutmaz+AteistTurk+BLKGM+Turkmenistan+Otuken')
      
  print("Collecting  last 3 mentions,last 50 comments and last 10 posts from new...")

  time.sleep(1)
  for mention in reddit.inbox.mentions(limit = 3):
    if  mention.id not in replied_to and mention.author != reddit.user.me():
      time.sleep(1)
      reply(mention)
      
  for submission in subreddit.new(limit=10):
    submission_lower = submission.title.lower()
    submission.id = "t3_" + submission.id
    if "atatürk" in submission_lower and submission.id not in replied_to and submission.author != reddit.user.me():
      time.sleep(1)
      reply(submission)

  yes_or_no = random.randint(0,3)
  for comment in subreddit.comments(limit=50):
    if yes_or_no == 1:
      comment_lower = comment.body.lower()
      if "atatürk" in comment_lower and comment.id not in replied_to  and comment.author != reddit.user.me():
        time.sleep(1)
        reply(comment)    


  print("Collect Completed.")

  print("Sleeping for 300 seconds...")
  time.sleep(300)

 
reddit = login()
replied_to = get_saved_comments()


while True:
  try:
    main(reddit, replied_to)
  except Exception as e:
    print(str(e) + " ,sleeping 120 seconds...")
    time.sleep(120)
    main(reddit, replied_to)

# "Bilim, gerçeği bilmektir." -M.Kemal Atatürk

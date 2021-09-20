# AtaturkQuoteBot v3.4 by MrZpzp

import praw
import quotesl
import photosl
import time
import os
import random


def bot_login():
    print("Logging in...")  # Don't forget to fill this area
    reddit = praw.Reddit(client_id='client_id',   
                    client_secret='client_secret',
                    user_agent='user_agent',
                    username='username',
                    password='password')
    print("Logged in!")

    return reddit

def run_bot(reddit, comments_replied_to):
    subreddit = reddit.subreddit('Ata')  # This is where the subreddit names will go.
    

    print("Collecting mentions,last 30 comments and last 7 posts from new")

    choose_from = random.choice([quotesl.quotes , photosl.photos, quotesl.quotes])

    yes_or_no = random.randint(0,2)
    

    for mention in reddit.inbox.mentions(limit = 10):
  
        if  mention.id not in comments_replied_to and mention.author != reddit.user.me(
        ):
            print("mention found in mention " +
                  mention.id)
            random_index = random.randint(0, len(quotesl.quotes) - 1)
            random_index2 = random.randint(0, len(photosl.photos) - 1)
            
            if choose_from == quotesl.quotes:
              mention.reply(choose_from[random_index] + " \n\n "
                                                  "*-M.Kemal Atatürk* \n\n "
                                                   "^(I am a bot and this action was performed automatically.)" + "\n\n" + "[INFO|BİLGİ](https://www.reddit.com/user/mkemalataturk/mentions/pcp0q0/ataturkquotebot_says_hellooo/)")
           

            print("Replied to mention " + mention.id)

            comments_replied_to.append(mention.id)

            with open("comments_replied_to.txt", "a") as f:
                f.write(mention.id + "\n")
    
    
    
    
    for submission in subreddit.new(limit=7):
        submission_lower = submission.title.lower()

        submission.id = "t3_" + submission.id
        if "atatürk" in submission_lower and submission.id not in comments_replied_to and submission.author != reddit.user.me(
        ):
            print("Post with \"related words\" found in post " +
                  submission.id)
            random_index = random.randint(0, len(quotesl.quotes) - 1)
            random_index2 = random.randint(0, len(photosl.photos) - 1)
            
            if choose_from == quotesl.quotes:
              submission.reply(choose_from[random_index] + " \n\n "
                                                  "*-M.Kemal Atatürk* \n\n "
                                                   "^(I am a bot and this action was performed automatically.)" + "\n\n" + "[INFO|BİLGİ](https://www.reddit.com/user/mkemalataturk/comments/pcp0q0/ataturkquotebot_says_hellooo/)")
            
            elif choose_from == photosl.photos:
              submission.reply(choose_from[random_index2] + " \n\n "
                                                  
                                                  "^(I am a bot and this action was performed automatically.)" + "\n\n" + "[INFO|BİLGİ](https://www.reddit.com/user/mkemalataturk/comments/pcp0q0/ataturkquotebot_says_hellooo/)")

            

            print("Replied to post " + submission.id)

            comments_replied_to.append(submission.id)

            with open("comments_replied_to.txt", "a") as f:
                f.write(submission.id + "\n")
          

    for comment in subreddit.comments(limit=50):
        
        if yes_or_no == 1:
            comment_lower = comment.body.lower()
            if "atatürk " in comment_lower and comment.link_id not in comments_replied_to  and comment.author != reddit.user.me(
              ):
                
                print("Comment with \"related words\" found in comment " +
                      comment.id)
                random_index = random.randint(0, len(quotesl.quotes) - 1)
                random_index2 = random.randint(0, len(photosl.photos) - 1)
                
                if choose_from == quotesl.quotes:
                    comment.reply(choose_from[random_index] + " \n\n "
                                                      "*-M.Kemal Atatürk* \n\n "
                                                      "^(I am a bot and this action was performed automatically.)" + "\n\n" + "[INFO|BİLGİ](https://www.reddit.com/user/mkemalataturk/comments/pcp0q0/ataturkquotebot_says_hellooo/)")
                
                elif choose_from == photosl.photos:
                    comment.reply(choose_from[random_index2] + " \n\n "
                                                      
                                                      "^(I am a bot and this action was performed automatically.)" + "\n\n" + "[INFO|BİLGİ](https://www.reddit.com/user/mkemalataturk/comments/pcp0q0/ataturkquotebot_says_hellooo/)")

                

                print("Replied to comment " + comment.id)

                comments_replied_to.append(comment.link_id)

                with open("comments_replied_to.txt", "a") as f:
                    f.write(comment.link_id + "\n")
        else:
          continue    
          
    print("Collect Completed.")

    print("Sleeping for 240 seconds...")
    time.sleep(240)


def get_saved_comments():
    if not os.path.isfile("comments_replied_to.txt"):
        comments_replied_to = []
    else:
        with open("comments_replied_to.txt", "r") as f:
            comments_replied_to = f.read()
            comments_replied_to = comments_replied_to.split("\n")
            comments_replied_to = list(filter(None, comments_replied_to))

    return comments_replied_to

reddit = bot_login()
comments_replied_to = get_saved_comments()

while True:
    run_bot(reddit, comments_replied_to)


#I am not a professional coder and this code is definetly not perfect but it gets the job done.
#This code is mainly based on yashar1/reddit-comment-bot but with huge improvements.

# "Bilim, gerçeği bilmektir." -M.Kemal Atatürk

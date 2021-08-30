# AtaturkQuoteBot v3.0 by MrZpzp

import praw
import quotesl
import photosl
import time
import os
import random




def bot_login():
    print("Logging in...")
    reddit = praw.Reddit(client_id=os.environ['client_id'],
                    client_secret=os.environ['client_secret'],
                    user_agent=os.environ['user_agent'],
                    username=os.environ['username'],
                    password=os.environ['password'])
    print("Logged in!")

    return reddit

def run_bot(reddit, comments_replied_to):
    subreddit = reddit.subreddit('Ata+Turkey+TurkeyJerky+KGBTR+ArsivUnutmaz')


    print("Collecting last 150 comments and top 7 post from hot ")

    choose_from = random.choice([quotesl.quotes , photosl.photos, quotesl.quotes , quotesl.quotes])

    for submission in subreddit.hot(limit=7):
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
                                                  "^(I am a bot and this action was performed automatically.Please contact u/mrzpzp for complaints and questions.)"
            )
            elif choose_from == photosl.photos:
              submission.reply(choose_from[random_index2] + " \n\n "
                                                  
                                                  "^(I am a bot and this action was performed automatically.Please contact u/mrzpzp for complaints and questions.)"

            )

            print("Replied to post " + submission.id)

            comments_replied_to.append(submission.id)



            with open("comments_replied_to.txt", "a") as f:
                f.write(submission.id + "\n")


        elif "mustafa kemal" in submission_lower and submission.id not in comments_replied_to and submission.author != reddit.user.me(
        ):
            print("Post with \"related words\" found in post " +
                  submission.id)
            random_index = random.randint(0, len(quotesl.quotes) - 1)
            random_index2 = random.randint(0, len(photosl.photos) - 1)

            if choose_from == quotesl.quotes:
              submission.reply(choose_from[random_index] + " \n\n "
                                                  "*-M.Kemal Atatürk* \n\n "
                                                  "^(I am a bot and this action was performed automatically.Please contact u/mrzpzp for complaints and questions.)"
            )
            elif choose_from == photosl.photos:
              submission.reply(choose_from[random_index2] + " \n\n "
                                                  
                                                  "^(I am a bot and this action was performed automatically.Please contact u/mrzpzp for complaints and questions.)"

            )

            print("Replied to post " + submission.id)

            comments_replied_to.append(submission.id)

            with open("comments_replied_to.txt", "a") as f:
                f.write(submission.id + "\n")
        


    for comment in subreddit.comments(limit=150):

        comment_lower = comment.body.lower()
        if "atatürk" in comment_lower and comment.link_id not in comments_replied_to and comment.author != reddit.user.me(
        ):
            print("Comment with \"related words\" found in comment " +
                  comment.link_id)
            random_index = random.randint(0, len(quotesl.quotes) - 1)
            random_index2 = random.randint(0, len(photosl.photos) - 1)

            if choose_from == quotesl.quotes:
              comment.reply(choose_from[random_index] + " \n\n "
                                                  "*-M.Kemal Atatürk* \n\n "
                                                  "^(I am a bot and this action was performed automatically.Please contact u/mrzpzp for complaints and questions.)"
            )
            elif choose_from == photosl.photos:
              comment.reply(choose_from[random_index2] + " \n\n "
                                                  
                                                  "^(I am a bot and this action was performed automatically.Please contact u/mrzpzp for complaints and questions.)"

            )
            
            print("Replied to comment " + comment.link_id)

            comments_replied_to.append(comment.link_id)



            with open("comments_replied_to.txt", "a") as f:
                f.write(comment.link_id + "\n")


        elif "mustafa kemal" in comment_lower and comment.link_id not in comments_replied_to and comment.author != reddit.user.me(
        ):
            print("String with \"related words\" found in comment " +
                  comment.link_id)
            random_index = random.randint(0, len(quotesl.quotes) - 1)
            random_index2 = random.randint(0, len(photosl.photos) - 1)

            if choose_from == quotesl.quotes:
              comment.reply(choose_from[random_index] + " \n\n "
                                                  "*-M.Kemal Atatürk* \n\n "
                                                  "^(I am a bot and this action was performed automatically.Please contact u/mrzpzp for complaints and questions.)"
            )
            elif choose_from == photosl.photos:
              comment.reply(choose_from[random_index2] + " \n\n "
                                                  
                                                  "^(I am a bot and this action was performed automatically.Please contact u/mrzpzp for complaints and questions.)"

            
            )
            print("Replied to comment " + comment.link_id)

            comments_replied_to.append(comment.link_id)

            with open("comments_replied_to.txt", "a") as f:
                f.write(comment.link_id + "\n")

    
        
    print("Collect Completed.")

    print("Sleeping for 180 seconds...")
    time.sleep(180)


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

# "Bilim, gerçeği bilmektir." -M.Kemal Atatürk
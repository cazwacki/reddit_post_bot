import praw
import json

# Parse config
with open('config.json', 'r') as file:
    bot_config = json.load(file)

subreddit = 'discordservers'
title = 'Hi, you should come to the Dreamland! We\'re a small, 18+ social server looking to make friends! We do occasional movie nights and game nights, but it\'s fine if you just want to chat! We would love to meet you. :-)'
url = 'https://discord.gg/u2hGGhD2Ra'
comment = 'This was posted automatically, so I can\'t easily respond to messages here. If you have any questions, please feel free to message me on Discord (sage#5429)! I look forward to meeting you :-)!' 

reddit = praw.Reddit(
    client_id=bot_config['client_id'],
    client_secret=bot_config['client_secret'],
    password=bot_config['password'],
    username=bot_config['username'],
    user_agent=bot_config['user_agent']
)

reddit.validate_on_submit=True

new_post = reddit.subreddit(subreddit).submit(title, 
    url=url, 
    nsfw='true')

new_post.reply(comment)
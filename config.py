import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

# file_path
blacklist_file = './data/blacklist.txt'
downloaded_post = './data/downloaded_posts.txt'

# vk_data
access_token = os.getenv('access_token')
community_ids = os.getenv('community_ids').split(',') # Должно быть написано так: community_ids=123,321,456,654 etc
hashtags = {
    '123': 'example1',
      '234': 'example2',
        '345': 'example3',
          '456': 'example4',
            '678': 'example5'} # x = {123: 'example1', 234: 'example2', 345: 'example3'} etc

# telegram_data
BOT_TOKEN = os.getenv('BOT_TOKEN')
CHANNEL_ID = os.getenv('CHANNEL_ID')
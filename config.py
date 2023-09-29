import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

# file_path
blacklist_file = './data/blacklist.txt'
downloaded_post = './data/downloaded_posts.txt'

# vk_data
access_token = os.getenv('access_token')
community_ids = os.getenv('community_ids').split(',') # 

# telegram_data
BOT_TOKEN = os.getenv('BOT_TOKEN')
CHANNEL_ID = os.getenv('CHANNEL_ID')
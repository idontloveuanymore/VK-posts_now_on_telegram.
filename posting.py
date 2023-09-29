import os
import telebot

from config import *
from downloading import *
from moderation import *

# Инициализируем телеграмм бота ps обязательно права администратора
bot = telebot.TeleBot(BOT_TOKEN)

def send_media_to_channel(channel_id, media_paths):
    for media_path in media_paths:
        if media_path.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
            with open(media_path, 'rb') as photo:
                bot.send_photo(chat_id=channel_id, photo=photo)
            print(f'Image sent and deleted: {media_path}')
        elif media_path.lower().endswith('.mp4'):
            with open(media_path, 'rb') as video:
                bot.send_video(chat_id=channel_id, video=video)
            print(f'Video sent and deleted: {media_path}')
        else:
            print(f'Unsupported file format: {media_path}')
        
        os.remove(media_path)

# Функция для отправки медиа в ваш канал
def perform_action_after_downloading(media_paths):
    send_media_to_channel(CHANNEL_ID, media_paths)
    print("Media were sent if they were in the folder.")
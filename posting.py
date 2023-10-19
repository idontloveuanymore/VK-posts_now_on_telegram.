import os
import telebot
import time

from config import BOT_TOKEN, CHANNEL_ID, hashtags

# Функция отвечающая за добавление хештега к альбому с фотографиями
def add_hashtag(group_id):
    if group_id in hashtags:
        return '#' + hashtags[group_id]
    else:
        return "#Help_me_im_break"

def send_media_to_channel(channel_id, media_paths):
    # Перенес инициализацию бота прямо в функцию
    bot = telebot.TeleBot(BOT_TOKEN)

    for media_path in media_paths:
        directory_path = os.path.dirname(media_path)
        file_names = os.listdir(directory_path)

        # Создаем словарь который будет соотносить айди групп с их медиа (пока тока фотографии)
        photo_dict = {}
        for file_name in file_names:
            group_id = file_name.split('_')[0]
            if group_id in photo_dict:
                photo_dict[group_id].append(file_name)
            else:
                photo_dict[group_id] = [file_name]

        # Отправка фотографий(теперь в альбомах)
        for group_id, photos in photo_dict.items():
            media = []
            for photo in photos:
                with open(os.path.join(directory_path, photo), 'rb') as file:
                    media.append(telebot.types.InputMediaPhoto(media=file.read()))

            try:
                message = bot.send_media_group(channel_id, media)
                time.sleep(3)  # Ждем пока фотачки отправятся, а то хештег добавится неверно

                # Добавляем хештег/несколько, если необходимо
                last_message_id = message[-1].message_id
                hashtag = add_hashtag(group_id)
                # Основная проблема, по которой мы не могли сразу добавить caption(если вставить caption прямо в send_media_group будет ошибка) решается вот этим:
                bot.edit_message_caption(chat_id=channel_id, message_id=last_message_id, caption=hashtag)

            except Exception as e:
                print(f"Error sending or editing message: {e}")

        # Удаяем все файлы (чистим папку), чтобы не было повторной отправки
        for file_name in file_names:
            file_path = os.path.join(directory_path, file_name)
            try:
                if os.path.isfile(file_path):
                    os.remove(file_path)
                else:
                    os.rmdir(file_path)
            except Exception as e:
                print(f"Error deleting file: {e}")

# Функция для отправки медиа в ваш канал(если есть желаение можно добавить что-то еще)
def perform_action_after_downloading(media_path):
    send_media_to_channel(CHANNEL_ID, media_path)
    print("Media were sent if they were in the folder.")
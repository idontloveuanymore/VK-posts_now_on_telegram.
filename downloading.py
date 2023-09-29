import os
import re
import requests
import urllib.request

from config import *
from moderation import *
from posting import *

# Функция для получения последнего поста (так как закреп - поста 2)
def get_latest_posts(community_id, access_token):
    api_url = f"https://api.vk.com/method/wall.get"
    params = {
        "owner_id": f"-{community_id}",
        "count": 2,
        "access_token": access_token,
        "v": "5.131"
    }
    response = requests.get(api_url, params=params)
    data = response.json()
    return data["response"]["items"]

# Сохраняем изображения из скаченных постов
def download_media_from_posts(posts, output_folder, downloaded_post_ids):
    downloaded_media = []
    for post in posts:
        post_id = post["id"]

        if post_id in downloaded_post_ids:
            print(f"Post ID {post_id} already downloaded. Skipping...")
            continue
        # Скачиваем, только если пост содержит изображения
        if "attachments" in post:
            for attachment in post["attachments"]:
                if attachment["type"] == "photo":
                    photo_sizes = attachment["photo"]["sizes"]
                    largest_size = max(photo_sizes, key=lambda x: x["width"])
                    photo_url = largest_size["url"]
                    filename = os.path.join(output_folder, f"{post_id}_{attachment['photo']['id']}.jpg")
                    urllib.request.urlretrieve(photo_url, filename)
                    print(f"Downloaded: {filename}")
                    downloaded_media.append(filename)
                    downloaded_post_ids.add(post_id)

    return downloaded_media

# Считывание уже загруженных айди постов из файла (это понадобится для модерации)
downloaded_post_ids = read_downloaded_post_ids(downloaded_post)
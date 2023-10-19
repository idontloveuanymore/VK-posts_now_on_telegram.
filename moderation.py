import os
import re

# Функция для чтения айди постов
def read_downloaded_post_ids(filename):
    if filename is None:
        return set()
    
    if not os.path.exists(filename):
        return set()

    with open(filename, "r", encoding='utf-8') as file:
        return set(map(int, file.read().splitlines()))

# Функция для записи айди постов в документ
def write_post_ids_to_file(post_ids, filename):
    with open(filename, "a", encoding='utf-8') as file:
        for post_id in post_ids:
            file.write(f"{post_id}\n")

# Функция проверяющая пост на наличие 'запрещенных' слов из блеклиста
def contains_blacklisted_words(post, blacklist_file):
    with open(blacklist_file, "r", encoding='utf-8') as file:
        blacklist = set(line.strip() for line in file)

    if "text" in post:
        post_text = post["text"].lower()
        for word in blacklist:
            if word in post_text:
                return True

    if "text" in post:
        post_text = post["text"]
        # Так же добавил проверку на ссылки
        url_pattern = r'https?://\S+|www\.\S+'
        if re.search(url_pattern, post_text):
            return True

    if "marked_as_ads" in post and post["marked_as_ads"] == "1":
        return True

    return False 

# Функция проверающая не закреплен ли пост
def is_pinned_post(post):
    return "is_pinned" in post and post["is_pinned"] == 1

# Применяет все вышеперечиленные функции + console.log
def moderation(post, blacklist_file):
    if contains_blacklisted_words(post, blacklist_file):
        print(f"Post ID {post['id']} contains blacklisted words. Skipping...")
        return False
    elif is_pinned_post(post):
        print(f"Post ID {post['id']} is pinned. Skipping...")
        return False
    else:
        return True
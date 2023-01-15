import json
from json import JSONDecodeError
from config import BOOKMARKS_PATH, POST_PATH


class PostDao:

    def __init__(self, path):
        self.path = path

    def __repr__(self):
        return f"Путь: {self.path}"

    def load_posts(self):
        try:
            with open(self.path, encoding='utf-8') as file:
                data = json.load(file)
                return data
        except JSONDecodeError:
            return

    def get_all_posts(self):
        return self.load_posts()

    def get_posts_by_user(self, user_name):
        posts = self.get_all_posts()
        post_by_name = []
        try:
            for post in posts:
                if user_name == post['poster_name']:
                    post_by_name.append(post)
                if post['content'] is None:
                    return []
            return post_by_name
        except ValueError:
            return 'Такого пользователя нет'

    def search_for_posts(self, query):
        posts = self.get_all_posts()
        lst_posts = []
        for post in posts:
            if query.lower() in post['content'].lower():
                lst_posts.append(post)
        return lst_posts

    def get_post_by_pk(self, pk):
        posts = self.get_all_posts()
        try:
            for post in posts:
                if pk == post['pk']:
                    return post
            return
        except ValueError:
            return "Такого пользователя нет"

    def add_post_to_bookmarks(self, post):
        with open(BOOKMARKS_PATH, encoding='utf-8') as file:
            data = json.load(file)
        data.append(post)
        with open(BOOKMARKS_PATH, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)

    def get_all_bookmarks(self):
        with open(BOOKMARKS_PATH, encoding='utf-8') as file:
            data = json.load(file)
        return data

    def delete_bookmark(self, post):
        with open(BOOKMARKS_PATH, encoding='utf-8') as file:
            data = json.load(file)
        data.remove(post)
        with open(BOOKMARKS_PATH, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)

#     def get_tags(self, tag_name):
#         data = self.get_all_posts()
#         tags = []
#         for post in data:
#             for word in post['content']:
#                 if word.startswith('#'):
#                     tags.append(word)
#                     print(tags)
#         for tag in tags:
#             if tag == tag_name:
#                 return tag
#
# a = PostDao('../../data/posts.json')
# print(a.get_tags("еда"))




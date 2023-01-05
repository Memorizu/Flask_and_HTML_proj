import json


class PostDao:

    def __init__(self, path):
        self.path = path

    def load_posts(self):
        with open("./data/posts.json", encoding='utf-8') as file:
            return json.load(file)

    def get_all_posts(self):
        return self.load_posts()

    def get_posts_by_user(self, poster_name):
        posts = self.get_all_posts()
        try:
            for post in posts:
                if post['poster_name'] == poster_name:
                    return post
                if post['content'] is None:
                    return []
        except ValueError:
            return 'Такого пользователя нет'

    def search_for_posts(self, query):
        posts = self.get_all_posts()
        for post in posts:
            if query.lower() in post['content'].lower():
                return post

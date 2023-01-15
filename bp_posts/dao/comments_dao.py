from bp_posts.dao.posts_dao import PostDao
import json
from config import COMMENTS_PATH, POST_PATH


class CommentsDao:

    def __init__(self, path):
        self.path = path

    def load_comments(self):
        with open(COMMENTS_PATH, encoding='utf-8') as file:
            return json.load(file)

    def get_all_comments(self):
        return self.load_comments()

    def get_comments_by_post_id(self, post_pk):
        """
        return comments by post pk
        :param post_pk: int
        :return: list of comments
        """
        post_dao = PostDao(POST_PATH)
        post = post_dao.get_post_by_pk(post_pk)
        try:
            comments = []
            for comment in self.get_all_comments():
                if comment["post_id"] == post['pk']:
                    comments.append(comment)
            return comments
        except ValueError:
            return "Такого поста нет"


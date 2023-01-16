from flask import Blueprint, jsonify
from bp_posts.views import PostDao
from config import POST_PATH
import logging


api_logger = logging.getLogger()
console_logger = logging.getLogger()

api_file_handler = logging.FileHandler("./logs/api.log")
console_handler = logging.StreamHandler()

formatter = logging.Formatter("%(asctime)s : [%(levelname)s] : %(message)s")

api_file_handler.setFormatter(formatter)

api_logger.addHandler(api_file_handler)
console_logger.setLevel(logging.DEBUG)
console_logger.addHandler(console_handler)

api_blueprint = Blueprint('api_blueprint', __name__)


@api_blueprint.get('/api/posts')
def get_posts():
    post_dao = PostDao(POST_PATH)
    data = post_dao.get_all_posts()
    return jsonify(data)


@api_blueprint.get('/api/posts/<int:post_id>')
def get_post_by_post_id(post_id):
    post_dao = PostDao(POST_PATH)
    data = post_dao.get_post_by_pk(post_id)
    return jsonify(data)

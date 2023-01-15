from flask import Blueprint, jsonify
from bp_posts.views import PostDao
from config import POST_PATH


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

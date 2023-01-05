from flask import Blueprint, render_template

from bp_posts.posts_dao import PostDao

post_blueprint = Blueprint('post_blueprint', __name__)
posts_path = '../data/posts.json'


@post_blueprint.get('/')
def index_page():
    posts_dao = PostDao(posts_path)
    posts = posts_dao.get_all_posts()
    return render_template('index.html', posts=posts)




from flask import Blueprint, render_template, request
from config import POST_PATH, COMMENTS_PATH
from bp_posts.posts_dao import PostDao
from bp_posts.comments_dao import CommentsDao

post_blueprint = Blueprint('post_blueprint', __name__)


@post_blueprint.get('/')
def index_page():
    posts_dao = PostDao(POST_PATH)
    posts = posts_dao.get_all_posts()
    return render_template('index.html', posts=posts)


@post_blueprint.get('/posts/<int:pk>')
def get_post(pk):
    post_dao = PostDao(POST_PATH)
    post = post_dao.get_post_by_pk(pk)
    name = post['poster_name']
    content = post_dao.get_posts_by_user(name)
    comment_dao = CommentsDao(COMMENTS_PATH)
    comments = comment_dao.get_comments_by_post_id(pk)
    len_comments = len(comments)
    return render_template('post.html', post=post, content=content, comments=comments, len_comments=len_comments)


@post_blueprint.get('/search')
def search_post():
    post_dao = PostDao(POST_PATH)
    query = request.args['s']
    result = post_dao.search_for_posts(query)
    return render_template('search.html', result=result, query=query)


@post_blueprint.get('/users/<username>')
def get_user_name(username):
    post_dao_name = PostDao(POST_PATH)
    posts = post_dao_name.get_posts_by_user(username)
    return render_template('user-feed.html', posts=posts)

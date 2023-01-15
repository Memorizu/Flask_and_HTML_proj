from flask import Blueprint, render_template, request, redirect
from config import POST_PATH, COMMENTS_PATH
from bp_posts.dao.posts_dao import PostDao
from bp_posts.dao.comments_dao import CommentsDao

post_blueprint = Blueprint('post_blueprint', __name__)


@post_blueprint.get('/')
def index_page():
    posts_dao = PostDao(POST_PATH)
    posts = posts_dao.get_all_posts()
    bookmarks = len(posts_dao.get_all_bookmarks())
    return render_template('index.html', posts=posts, bookmarks=bookmarks)


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
    len_result = len(result)
    return render_template('search.html', result=result, query=query, len_result=len_result)


@post_blueprint.get('/users/<username>')
def get_user_name(username):
    post_dao_name = PostDao(POST_PATH)
    posts = post_dao_name.get_posts_by_user(username)
    return render_template('user-feed.html', posts=posts, username=username)


@post_blueprint.get('/bookmarks/add/<int:post_pk>')
def add_bookmark(post_pk):
    post_dao_bookmark = PostDao(POST_PATH)
    post = post_dao_bookmark.get_post_by_pk(post_pk)
    post_dao_bookmark.add_post_to_bookmarks(post)
    return redirect("/", code=302)


@post_blueprint.get('/bookmarks')
def bookmarks_page():
    post_dao_all_bookmarks = PostDao(POST_PATH)
    bookmarks = post_dao_all_bookmarks.get_all_bookmarks()
    return render_template('bookmarks.html', bookmarks=bookmarks)


@post_blueprint.get('/bookmarks/remove/<int:post_id>')
def remove_bookmark(post_id):
    post_remove = PostDao(POST_PATH)
    post = post_remove.get_post_by_pk(post_id)
    post_remove.delete_bookmark(post)
    return redirect("/", code=302)


@post_blueprint.get('/tag/<tag_name>')
def tag_page(tag_name):
    post_tags = PostDao(POST_PATH)
    tags = post_tags.get_tags()

    return render_template('tag.html')

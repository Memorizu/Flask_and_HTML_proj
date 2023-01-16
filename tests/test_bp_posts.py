import pytest

from bp_posts.dao.posts_dao import PostDao
from bp_posts.dao.comments_dao import CommentsDao


@pytest.fixture
def post_number_1():
    return [{
        "poster_name": "leo",
        "poster_avatar": "https://randus.org/avatars/w/c1819dbdffffff18.png",
        "pic": "https://images.unsplash.com/photo-1525351326368-efbb5cb6814d?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=580&q=80",
        "content": "Ага, опять еда! Квадратная тарелка в квадратном кадре. А на тарелке, наверное, пирог! Мне было так жаль, что я не могу ее съесть. Я боялась, что они заметят, и если я не съем это, то, значит, они все подумают, что я плохая девочка... Но потом мне вспомнилось, как они на меня смотрели. Когда я была маленькой, на кухне всегда были родители, бабушка, дедушка, дядя Борис... Все вместе. И всегда одна я, потому что все остальные приходили туда лишь изредка. Мне казалось, если бы все ходили на работу, как и я, в этот свой офис, было бы совсем неинтересно.",
        "views_count": 376,
        "likes_count": 154,
        "pk": 1
    }]


@pytest.fixture
def comments_1():
    return [{
        "post_id": 1,
        "commenter_name": "leo",
        "comment": "Интересно. А где это?",
        "pk": 4
    }]


def test_get_post_by_pk(post_number_1):
    post_dao = PostDao("./data/posts.json")
    post = post_dao.get_post_by_pk(1)
    assert post == post_number_1


def test_get_posts_all():
    post_dao = PostDao("./data/posts.json")
    len_posts = len(post_dao.get_all_posts())
    assert len_posts == 8


def test_get_posts_by_user(post_number_1):
    post_dao = PostDao("./data/posts.json")
    user_post = post_dao.get_posts_by_user('leo')
    assert user_post == post_number_1


def test_get_comments_by_post_id(comments_1):
    comments_dao = CommentsDao("./data/comments.json")
    comment = comments_dao.get_comments_by_post_id(1)
    assert comment == comments_1


def test_search_for_posts(post_number_1):
    post_dao = PostDao("./data/posts.json")
    search_posts = post_dao.search_for_posts('еда')
    assert search_posts == post_number_1

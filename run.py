from flask import Flask

from bp_posts.views import post_blueprint


app = Flask(__name__)


app.register_blueprint(post_blueprint, template_folder='templates')

if __name__ == '__main__':
    app.run(debug=True)





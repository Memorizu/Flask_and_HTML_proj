from flask import Flask
from bp_posts.views import post_blueprint

app = Flask(__name__)

app.register_blueprint(post_blueprint)

app.run(debug=True, port=5001)





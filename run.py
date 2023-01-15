from flask import Flask
import logging
from bp_posts.views import post_blueprint
from bp_API.views import api_blueprint

app = Flask(__name__)

console_logger = logging.getLogger('console_logger')
console_logger.setLevel(logging.DEBUG)
console_handler = logging.StreamHandler()
console_logger.addHandler(console_handler)
formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
file_logger = logging.getLogger('file_logger')
file_logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('./logs/api.log')
file_logger.addHandler(file_handler)
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

app.config['JSON_AS_ASCII'] = False

app.register_blueprint(post_blueprint, template_folder='templates')
app.register_blueprint(api_blueprint)


if __name__ == '__main__':
    app.run(debug=True)

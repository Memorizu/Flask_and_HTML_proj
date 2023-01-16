from flask import Flask, render_template
from bp_posts.views import post_blueprint
from bp_API.views import api_blueprint

app = Flask(__name__)


app.config['JSON_AS_ASCII'] = False


app.register_blueprint(post_blueprint, template_folder='templates')
app.register_blueprint(api_blueprint)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def page_500_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(debug=True)

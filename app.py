from flask import Flask, render_template
from werkzeug.serving import run_simple

from flask_webpack import Webpack


webpack = Webpack()


def create_app():
    """
    Create a Flask application using the app factory pattern.

    :return: Flask app
    """
    app = Flask(__name__)

    settings = {
        'DEBUG': True,
        'WEBPACK_MANIFEST_PATH': './build/manifest.json'
    }

    app.config.update(settings)

    webpack.init_app(app)

    return app


app = create_app()


@app.route('/')
def index():
    return render_template('index.jinja2')

# Please use a proper wsgi server such as gunicorn, I am only using this to keep
# the demo app as simple as possible.
if __name__ == '__main__':
    run_simple('localhost', 5000, app, use_reloader=True, use_debugger=True)

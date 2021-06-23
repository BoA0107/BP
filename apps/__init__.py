from flask import *
from apps.show.view import bp_show


def create_app():
    app = Flask(__name__,template_folder='../templates')
    app.register_blueprint(bp_show)

    print(app.url_map)
    return app

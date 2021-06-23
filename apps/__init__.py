from flask import *
from apps.show.view import bp_show
from apps.index.view import bp_index
from apps.home.view import bp_home


def create_app():
    app = Flask(__name__,template_folder='../templates')
    app.register_blueprint(bp_show)
    app.register_blueprint(bp_index)
    app.register_blueprint(bp_home)

    print(app.url_map)
    return app

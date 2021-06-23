from flask import *

bp_index= Blueprint('index', __name__)


@bp_index.route('/index')
def index():
    return render_template('index.html')

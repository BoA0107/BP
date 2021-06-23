from flask import *

bp_show= Blueprint('show', __name__)


@bp_show.route('/')
def show():
    return render_template('show.html')

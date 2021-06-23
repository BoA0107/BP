from flask import *

bp_home= Blueprint('home', __name__)


@bp_home.route('/home')
def home():
    return render_template('home.html')

from func.func_home import *
from func.func_BCA import *

app = Flask(__name__)


@app.route('/')
def show():
    return render_template('show.html')


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/home')
def home():
    return render_template("home.html", plan_info=plan_info, links=links_dct, career_level=career_level)


@app.route('/BCA')
def BCA():
    return render_template('BCA.html',UAT_BC=UAT_BC)


@app.route('/SQL')
def SQL():
    return render_template('SQL.html')


@app.route('/deploy')
def deploy():
    return render_template('deploy.html')


if __name__ == "__main__":
    app.run(port=7777, debug=True)

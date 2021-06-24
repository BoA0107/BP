from flask import *
from read_doc import *

F_home = r'doc/home.xlsx'
F_BCA = r'doc/BCA.xlsx'
F_SQL = r'doc/SQL.xlsx'

F_S_links = r'links'
F_S_deploy_plan = r'deploy_plan'
F_S_level_info = r'level_info'


app = Flask(__name__)


@app.route('/')
def show():
    return render_template('show.html')


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/home')
def home():
    # plan_info
    plan_info = read_doc(filename=F_home, sheetname=F_S_deploy_plan, max_line=16)

    # links
    links = read_doc(filename=F_home, sheetname=F_S_links)
    links_dct = make_dct(links)

    # career_level
    career_level = read_doc(filename=F_home, sheetname=F_S_level_info)

    return render_template("home.html", plan_info=plan_info, links=links_dct, career_level=career_level)


@app.route('/BCA')
def BCA():
    return render_template('BCA.html')


@app.route('/SQL')
def SQL():
    return render_template('SQL.html')


@app.route('/deploy')
def deploy():
    return render_template('deploy.html')


if __name__ == "__main__":
    app.run(port=7777, debug=True)

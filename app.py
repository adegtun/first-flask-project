from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.update(
    SECRECT_KEY='topsecret',
    SQLALCHEMY_DATABASE_URI='postgresql://postgres:tope123@localhost/catalog_db',
    SQLALCHEMY_TRACK_MODIFICATIONS=False
)
db = SQLAlchemy(app)

@app.route("/")
def Index():
    user_agent = request.headers.get('User-Agent')
    return "Your browser is {}".format(user_agent)

@app.route("/user/<string:name>")
def User(name):
    return "Hello, dear {}!". format(name)

@app.route("/news/")
def GetNewFunction():
    val = request.args.get('greeting')
    return "The greeting is {}".format(val)

@app.route("/watch")
def movies():
    movie_list = ['Pilgrim progress', 'War room', 'Agbara nla']
    return render_template('movies.html', movies=movie_list, name='Harry')

@app.route("/table")
def movies_plus():
    movie_dict = {'Pilgrim progress':3.14, 'War room':2.14, 'Agbara nla':5.5}
    return render_template('table_data.html', movies=movie_dict, name='Sally')

@app.route("/macros")
def jinja_macros():
    movie_dict = {'Pilgrim progress':3.14, 
    'War room':2.14,
    'Coming to America': 1.63,
    'Hard target': 5.22, 
    'Agbara nla':1.57}
    return render_template('using_macros.html', movies=movie_dict, name='Sally')


class Publication(db.Model):
    __tablename__='publication'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return 'The id is {}, Name is {}'.format(self.id, self.name)

if __name__=='__main__':
    db.create_all()
    app.run(debug=True)
from flask import Flask
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config.from_json("config.json")
db = MongoEngine(app)


class Codex(db.Document):
    name = db.StringField(required=True, unique=True)


@app.route('/')
def hello():
    return 'hello'


@app.route('/s')
def save():
    m = Codex(name='janice').save()
    return m.name

from flask import Flask
from flask_mongoengine import MongoEngine

app = Flask(__name__)
db = MongoEngine(app)
app.config.from_json("config.json")


@app.route('/')
def hello():
    return 'hello'

from flask import Flask, render_template, request, redirect, url_for
from flask_mongoengine import MongoEngine
import datetime

app = Flask(__name__, template_folder='templates')
app.config.from_json("config.json")
db = MongoEngine(app)


class Codex(db.Document):
    content = db.StringField(required=True)
    added_on = db.DateTimeField(required=True)
    source = db.StringField(required=True)
    source_type = db.StringField(required=True)


@app.route('/')
def get_all_documents():
    all_documents = Codex.objects
    return render_template('index.html', documents=all_documents)


@app.route('/new', methods=['POST'])
def new_document():
    content = request.form['content']
    source = request.form['source']
    source_type = request.form['source_type']
    c = Codex(content=content, added_on=datetime.datetime.now(), source=source, source_type=source_type).save()
    return redirect(url_for('get_all_documents'))

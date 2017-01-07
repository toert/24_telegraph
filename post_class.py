from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(80))
    author = db.Column(db.String(80))
    post_text = db.Column(db.Text)

    def __init__(self, title, author, post_text):
        self.title = title
        self.author = author
        self.post_text = post_text

    def __repr__(self):
        return 'title={}, author={}, post_text={}, id={}'\
            .format(self.title, self.author, self.post_text, self.id)
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from model import db, Posts
from helpers import get_forms_content, add_post_in_db


app = Flask(__name__)
app.config.from_object('config')
db.init_app(app)


@app.route('/', methods=['GET'])
def render_form():
    return render_template('form.html')


@app.route('/', methods=['POST'])
def make_a_post():
    header, sign, body = get_forms_content()
    unique_id = add_post_in_db(header, sign, body)
    return redirect(unique_id, 301)


@app.route('/<call_id>', methods=['GET'])
def show_article(call_id):
    post_info = Posts.query.filter_by(id=call_id).first()
    return render_template('article.html', info=(post_info.title, post_info.author , post_info.post_text))


if __name__ == "__main__":
    app.run()


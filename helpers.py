from flask import request
from model import Posts, db

def get_forms_content():
    header = request.form['header']
    sign = request.form['signature']
    body = request.form['body']
    return header, sign, body


def add_post_in_db(header, sign, body):
    new_post = Posts(header, sign, body)
    db.session.add(new_post)
    db.session.commit()
    return new_post.id



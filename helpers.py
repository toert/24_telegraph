from flask import request
from model import Posts, db
from flask_sqlalchemy import SQLAlchemy
from math import log, ceil


def get_forms_content():
    header = request.form['header']
    sign = request.form['signature']
    body = request.form['body']
    return header, sign, body


def add_post_in_db(header, sign, body):
    new_post = Posts(header, sign, body)
    db.session.add(new_post)
    db.session.commit()
    new_post = Posts.query.filter_by(id=new_post.id).first() # returns yourself
    new_id_log = new_post.init_id_log()
    db.session.commit()
    return new_id_log



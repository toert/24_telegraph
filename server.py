from flask import Flask, render_template, request, redirect
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



@app.route('/', methods=['GET'])
def render_form():
    return render_template('form.html')


@app.route('/', methods=['POST'])
def make_a_post():
    header, sign, body = get_forms_content()
    unique_id = add_post_in_db(header, sign, body)
    return redirect(unique_id, 301)


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


@app.route('/<call_id>', methods=['GET'])
def show_article(call_id):
    post_info = Posts.query.filter_by(id=call_id).first()
    return render_template('article.html', info=(post_info.title, post_info.author , post_info.post_text))


if __name__ == "__main__":
    app.run(host='0.0.0.0')


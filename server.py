from flask import Flask, render_template, request
from post_class import Posts, app, db



@app.route('/', methods=['GET'])
def render_form():
    return render_template('form.html')


@app.route('/', methods=['POST'])
def make_a_post():
    header, sign, body = get_forms_content()
    print(header, sign, body)
    unique_id = add_post_in_db(header, sign, body)
    # TODO доделать
    return 'Success'


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
    print(post_info)
    # print(post_info)
    # return render_template('article.html', text=(poset, output_text))
    return post_info


if __name__ == "__main__":
    app.run()
    show_article(1)

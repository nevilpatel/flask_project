from datetime import datetime
from logging import DEBUG

from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.logger.setLevel(DEBUG)
app.config['SECRET_KEY'] = '>yM\xf9Y%\xec\xc7\x13\xdc\xfb\x85\xc0\xb8\x90\xaf\xe2S\xfc\x13)4\xaa\xe3'
bookmarks = []


def store_bookmark(url):
    bookmarks.append(dict(
        url=url,
        user='nevil',
        date=datetime.utcnow()
    ))


def new_bookmarks(num):
    return sorted(bookmarks, key=lambda bm: bm['date'], reverse=True)[:num]


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', newbookmarks=new_bookmarks(5))


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        url = request.form['url']
        store_bookmark(url)
        flash('Stored Bookmark: {} '.format(url))
        return redirect(url_for('index'))
    return render_template('add.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(debug=True)

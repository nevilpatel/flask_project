from datetime import datetime
from logging import DEBUG

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.logger.setLevel(DEBUG)

bookmarks = []


def store_bookmark(url):
    bookmarks.append(dict(
        url=url,
        user='nevil',
        date=datetime.utcnow()
    ))


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title="New Title", text="This is the new Text.")


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        url = request.form['url']
        store_bookmark(url)
        app.logger.debug('stored url ' + url)
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

import os

from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(app.instance_path, 'database', 'annapurna.db')
app.config['SECRET_KEY'] = 'test'

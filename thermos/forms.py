from flask_wtf import Form
from flask_wtf.html5 import URLField
from wtforms.fields import StringField
from wtforms.validators import DataRequired, url


class BookmarkForm(Form):
    url = URLField('url', validators=[DataRequired, url])
    description = StringField('description')

import json

from flask_sqlalchemy import SQLAlchemy

from settings import app

db = SQLAlchemy(app)


class Catalog(db.Model):
    __tablename__ = "catalog"
    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer)
    name = db.Column(db.String(80), nullable=False)
    vendor = db.Column(db.String(40), nullable=False)
    category = db.Column(db.String(20), nullable=False)

    def json(self):
        return {
            "item_id": self.item_id,
            "name": self.name,
            "vendor": self.vendor,
            "category": self.category
        }

    @staticmethod
    def add_item(_item_id, _name, _vendor, _category):
        new_item = Catalog(name=_name, vendor=_vendor, item_id=_item_id, category=_category)
        db.session.add(new_item)
        db.session.commit()
        app.logger.info('Added item {0}'.format(_name))

    @staticmethod
    def get_catalog():
        # convert each row to json otherwise it will return query objects
        app.logger.info('Getting Catalog')
        return [Catalog.json(item) for item in Catalog.query.all()]

    def get_item(_item_id):
        item = Catalog.query.filter_by(item_id=_item_id).first()
        if item:
            return [Catalog.json(item)]
        else:
            return []

    def delete_item(_item_id):
        is_successful = Catalog.query.filter_by(item_id=_item_id).delete()
        db.session.commit()
        return bool(is_successful)

    def update_name(_item_id, _name):
        item = Catalog.query.filter_by(item_id=_item_id).first()
        item.name = _name
        db.session.commit()

    def update_vendor(_item_id, _vendor):
        item = Catalog.query.filter_by(item_id=_item_id).first()
        item.vendor = _vendor
        db.session.commit()

    def update_category(_item_id, _category):
        item = Catalog.query.filter_by(item_id=_item_id).first()
        item.category = _category
        db.session.commit()

    def replace_item(_item_id, _name, _vendor, _category):
        item = Catalog.query.filter_by(item_id=_item_id).first()
        item.name = _name
        item.vendor = _vendor
        item.category = _category
        db.session.commit()

    def __repr__(self):
        item_object = {
            "item_id": self.item_id,
            "name": self.name,
            "vendor": self.vendor,
            "category": self.category
        }
        return json.dumps(item_object)

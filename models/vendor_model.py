from flask_sqlalchemy import SQLAlchemy

from settings import app

db: SQLAlchemy = SQLAlchemy(app)


class Vendor(db.Model):
    __table__name = 'vendor'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    ranking = db.Column(db.Integer, nullable=False)

    def json(self):
        return {
            "id": self.id,
            "name": self.name,
            "ranking": self.ranking
        }

    @staticmethod
    def get_vendors():
        app.logger.info('Getting all Vendors ')
        return [Vendor.json(item) for item in Vendor.query.all()]

    @staticmethod
    def get_vendor(_id):
        app.logger.info('Getting Vendor: {} '.format(_id))
        vendor = Vendor.query.filter_by(id=_id).first()
        if vendor:
            return [Vendor.json(vendor)]
        else:
            return []

    @staticmethod
    def add_vendor(_id, _name):
        new_vendor: Vendor = Vendor(id=_id, name=_name, ranking=5)
        db.session.add(new_vendor)
        db.session.commit()

    @staticmethod
    def remove_vendor(_id):
        is_successful = Vendor.query.filter_by(id=_id).first().delete()
        db.session.commit()
        return is_successful

    @staticmethod
    def update_name(_id, _name):
        item = Vendor.query.filter_by(id=_id).first()
        item.name = _name

    @staticmethod
    def update_ranking(_id, _ranking):
        item = Vendor.query.filter_by(id=_id).first()
        item.ranking = _ranking

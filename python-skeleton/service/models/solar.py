from research import db


class SolarPanel(db.Model):
    """This class represents the various makes and models of solar panels
       It corresponds to the SolarPanel table"""

    __tablename__ = 'solarpanels'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(
        db.DateTime, default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp()
    )
    efficiency_status = db.Column(db.Integer)

    def __init__(self, name, efficiency_status):
        self.name = name
        self.efficiency_status = efficiency_status

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return SolarPanel.query.all()

    @staticmethod
    def get_by_name(name):
        try:
            return SolarPanel.query.filter_by(name=name).first()
        except KeyError:
            return None

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return "<SolarPanel: {}>".format(self.name)
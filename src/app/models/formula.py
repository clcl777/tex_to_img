from app.database import db


class Formula(db.Model):
    __tablename__ = "formula"
    id = db.Column(db.Integer, primary_key=True)

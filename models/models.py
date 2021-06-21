import datetime as dt

from api.app import db


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    url = db.Column(db.String(255), unique=True)
    created_at = db.Column(db.DateTime, default=dt.datetime.utcnow)


class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer)
    comment = db.Column(db.Text, default="")
    created_at = db.Column(db.DateTime, default=dt.datetime.utcnow)

    course_id = db.Column(db.Integer, db.ForeignKey("course.id"), nullable=False)
    course = db.relationship("Course", backref=db.backref("reviews", lazy=True))

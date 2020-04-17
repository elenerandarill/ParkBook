from routes import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.password}')"


class PkgSpace(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, unique=True, nullable=False)
    booker = db.Column(db.String(100), default='none')
    date_booked = db.Column(db.String(10), default='none')

    def __repr__(self):
        return f"PkgSpace('{self.number}','{self.booker}','{self.date_booked}')"

from PbApp import pb_db


class User(pb_db.Model):
    id = pb_db.Column(pb_db.Integer, primary_key=True)
    username = pb_db.Column(pb_db.String(30), unique=True, nullable=False)
    email = pb_db.Column(pb_db.String(120), unique=True, nullable=False)
    password = pb_db.Column(pb_db.String(80), nullable=False)

    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.password}')"


class PkgSpace(pb_db.Model):
    id = pb_db.Column(pb_db.Integer, primary_key=True)
    number = pb_db.Column(pb_db.Integer, unique=True, nullable=False)
    booker = pb_db.Column(pb_db.String(100), default='none')
    date_booked = pb_db.Column(pb_db.String(10), default='none')

    def __repr__(self):
        return f"PkgSpace('{self.number}','{self.booker}','{self.date_booked}')"

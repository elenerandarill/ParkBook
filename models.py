from PbApp import pb_db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# UserMixin trzeba bylo dopisac zeby mozna bylo logowac uzytkownikow !!!
class User(pb_db.Model, UserMixin):
    id = pb_db.Column(pb_db.Integer, primary_key=True)
    username = pb_db.Column(pb_db.String(30), unique=True, nullable=False)
    email = pb_db.Column(pb_db.String(120), unique=True, nullable=False)
    password = pb_db.Column(pb_db.String(80), nullable=False)
    # Potrzebne do połączenia kolumn z obu klas.
    all_spaces = pb_db.relationship('PkgSpace', back_populates='owner')

    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.password}')"


class PkgSpace(pb_db.Model):
    id = pb_db.Column(pb_db.Integer, primary_key=True)
    number = pb_db.Column(pb_db.Integer, unique=True, nullable=False)
    booker = pb_db.Column(pb_db.String(100), default='none')
    # Potrzebne do połączenia kolumn z obu klas.
    # user_id z PkgSpace, a user.id z User.
    user_id = pb_db.Column(pb_db.ForeignKey('user.id'), nullable=False)
    owner = pb_db.relationship('User', back_populates='all_spaces')

    def __repr__(self):
        return f"PkgSpace('{self.number}','{self.booker}')"

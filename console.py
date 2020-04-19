from models import User, PkgSpace
from PbApp import pb_db

"""creating first users for db"""
# pb_db.create_all()
#
# user01 = User(username='user01', email='user01@wp.pl', password='user01')
# pb_db.session.add(user01)
# user02 = User(username='user02', email='user02@wp.pl', password='user02')
# pb_db.session.add(user02)
# pb_db.session.commit()
#
print(User.query.all())

"""creating parking spaces for db"""
#
# pkg_space01 = PkgSpace(number=12, booker='none', date_booked='none')
# pkg_space02 = PkgSpace(number=17, booker='none', date_booked='none')
# pb_db.session.add(pkg_space01)
# pb_db.session.add(pkg_space02)
# pb_db.session.commit()
#
print(PkgSpace.query.all())

""" """

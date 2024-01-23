from enum import unique
from ssl import _create_unverified_context
from song_recc import db,app,login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(id):
    return Login.query.get(int(id))



class Login(db.Model, UserMixin):
    id=db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80), nullable=False)
    usertype = db.Column(db.String(80), nullable=False)
    name = db.Column(db.String(200))
    contact = db.Column(db.String(200))

with app.app_context():
    # Create the tables
    db.create_all()







    
  

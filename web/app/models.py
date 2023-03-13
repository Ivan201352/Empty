
import sqlalchemy as sa
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin



from app import db, app

class Lift(db.Model, UserMixin):  
    __tablename__ = 'lifts'

    id = db.Column(db.Integer, primary_key=True)    
    address = db.Column(db.String(40), nullable=False)
    type = db.Column(db.String(250), nullable=False)

class Incedent(db.Model, UserMixin):
    __tablename__ = 'incedents'

    id = db.Column(db.Integer, primary_key=True)    
    address = db.Column(db.String(40), nullable=False)
    type = db.Column(db.String(250), nullable=False)
    key = db.Column(db.String(40), nullable=False)




    



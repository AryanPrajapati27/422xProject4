from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'
    
class Boat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    year_built = db.Column(db.Integer)
    make_model = db.Column(db.String(100))
    color = db.Column(db.String(50))
    type = db.Column(db.String(50))
    condition = db.Column(db.String(50))
    price = db.Column(db.Float)
    description = db.Column(db.String(200))
    city = db.Column(db.String(50))
    phone_number = db.Column(db.String(20))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('entries', lazy=True))

    def __repr__(self):
        return f'<Entry {self.make_model}>'


def init_app(app):
    db.init_app(app)

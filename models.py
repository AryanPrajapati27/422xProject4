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
    user = db.relationship('User', backref=db.backref('boats', lazy=True))

    def __repr__(self):
        return f'<Entry {self.make_model}>'
    
class Cars_Trucks(db.Model):
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
    user = db.relationship('User', backref=db.backref('cars_trucks', lazy=True))

    def __repr__(self):
        return f'<Entry {self.make_model}>'

class Motorcycles(db.Model):
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
    user = db.relationship('User', backref=db.backref('motorcycles', lazy=True))

    def __repr__(self):
        return f'<Entry {self.make_model}>'

class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    year_released = db.Column(db.Integer)
    title = db.Column(db.String(100))
    author = db.Column(db.String(100))
    pages = db.Column(db.Integer)
    condition = db.Column(db.String(50))
    price = db.Column(db.Float)
    description = db.Column(db.String(200))
    city = db.Column(db.String(50))
    phone_number = db.Column(db.String(20))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('books', lazy=True))

    def __repr__(self):
        return f'<Entry {self.title}>'
    
class Furniture(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    year_made = db.Column(db.Integer)
    name = db.Column(db.String(100))
    color = db.Column(db.String(50))
    condition = db.Column(db.String(50))
    price = db.Column(db.Float)
    description = db.Column(db.String(200))
    city = db.Column(db.String(50))
    phone_number = db.Column(db.String(20))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('furniture', lazy=True))

    def __repr__(self):
        return f'<Entry {self.name}>'



def init_app(app):
    db.init_app(app)

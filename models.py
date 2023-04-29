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

class Apartments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    bedrooms = db.Column(db.Integer)
    bathrooms = db.Column(db.Integer)
    square_footage = db.Column(db.Integer)
    monthly_rent = db.Column(db.Integer)
    description = db.Column(db.String(200))
    amenities = db.Column(db.String(200))
    city = db.Column(db.String(50))
    phone_number = db.Column(db.String(20))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('apartments', lazy=True))

    def __repr__(self):
        return f'<Entry {self.title}>'

class Condos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    bedrooms = db.Column(db.Integer)
    bathrooms = db.Column(db.Integer)
    square_footage = db.Column(db.Integer)
    price = db.Column(db.Integer)
    hoa_fees = db.Column(db.Integer)
    description = db.Column(db.String(200))
    amenities = db.Column(db.String(200))
    city = db.Column(db.String(50))
    phone_number = db.Column(db.String(20))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('condos', lazy=True))

    def __repr__(self):
        return f'<Entry {self.title}>'

class Houses(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    bedrooms = db.Column(db.Integer)
    bathrooms = db.Column(db.Integer)
    square_footage = db.Column(db.Integer)
    lot_size = db.Column(db.Integer)
    price = db.Column(db.Integer)
    description = db.Column(db.String(200))
    city = db.Column(db.String(50))
    phone_number = db.Column(db.String(20))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('houses', lazy=True))

    def __repr__(self):
        return f'<Entry {self.title}>'
    
class Roomates(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    rooms = db.Column(db.Integer)
    preferences = db.Column(db.String(200))
    bathrooms = db.Column(db.Integer)
    shared_spaces = db.Column(db.String(200))
    monthly_rate = db.Column(db.Integer)
    description = db.Column(db.String(200))
    city = db.Column(db.String(50))
    phone_number = db.Column(db.String(20))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('roomates', lazy=True))

    def __repr__(self):
        return f'<Entry {self.title}>'

class Vacation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    bedrooms = db.Column(db.Integer)
    bathrooms = db.Column(db.Integer)
    amenities = db.Column(db.String(200))
    nightly_rate = db.Column(db.Integer)
    minimum_stay = db.Column(db.Integer)
    description = db.Column(db.String(200))
    city = db.Column(db.String(50))
    phone_number = db.Column(db.String(20))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('vacation', lazy=True))

    def __repr__(self):
        return f'<Entry {self.title}>'

def init_app(app):
    db.init_app(app)

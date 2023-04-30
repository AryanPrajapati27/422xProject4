from flask import Flask, session, flash, render_template, request, redirect, url_for
from models import *
from werkzeug.security import check_password_hash, generate_password_hash
import sys
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'your_secret_key_here'

init_app(app)
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    if 'username' in session:
        return render_template('home.html', username=session["username"])
    else:
        return render_template('home.html')

@app.route('/for_sale/cars_trucks')
def cars_trucks():
    entries = Cars_Trucks.query.all()
    if 'username' not in session:
        return render_template('cars_trucks.html', entries=entries)
    return render_template('cars_trucks.html', username=session["username"], entries=entries)

@app.route('/for_sale/motorcycles')
def motorcycles():
    entries = Motorcycles.query.all()
    if 'username' not in session:
        return render_template('motorcycles.html', entries=entries)
    return render_template('motorcycles.html', username=session["username"], entries=entries)

@app.route('/for_sale/boats')
def boats():
    entries = Boat.query.all()
    if 'username' not in session:
        return render_template('boats.html', entries=entries)
    return render_template('boats.html', username=session["username"], entries=entries)

@app.route('/for_sale/books')
def books():
    entries = Books.query.all()
    if 'username' not in session:
        return render_template('books.html', entries=entries)
    return render_template('books.html', username=session["username"], entries=entries)

@app.route('/for_sale/furniture')
def furniture():
    entries = Furniture.query.all()
    if 'username' not in session:
        return render_template('furniture.html', entries=entries)
    return render_template('furniture.html', username=session["username"], entries=entries)
#####
@app.route('/housing/apartments')
def apartments():
    entries = Apartments.query.all()
    if 'username' not in session:
        return render_template('apartments.html', entries=entries)
    return render_template('apartments.html', username=session["username"], entries=entries)

@app.route('/housing/houses')
def houses():
    entries = Houses.query.all()
    if 'username' not in session:
        return render_template('houses.html', entries=entries)
    return render_template('houses.html', username=session["username"], entries=entries)

@app.route('/housing/condos')
def condos():
    entries = Condos.query.all()
    if 'username' not in session:
        return render_template('condos.html', entries=entries)
    return render_template('condos.html', username=session["username"], entries=entries)

@app.route('/housing/roomates')
def roomates():
    entries = Roomates.query.all()
    if 'username' not in session:
        return render_template('roomates.html', entries=entries)
    return render_template('roomates.html', username=session["username"], entries=entries)

@app.route('/housing/vacation')
def vacation():
    entries = Vacation.query.all()
    if 'username' not in session:
        return render_template('vacation.html', entries=entries)

    return render_template('vacation.html', username=session["username"], entries=entries)

@app.route('/more_info/<string:type>/<int:entry_id>')
def more_info(entry_id, type):
    obj = getattr(sys.modules[__name__], type)
    entry = obj.query.filter_by(id=entry_id).first()
    if 'username' not in session:
        return render_template('more_info.html', entry=entry)
    return render_template('more_info.html', username=session["username"], entry=entry)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

@app.route('/create_boat', methods=['GET', 'POST']) 
def create_boat():
    if request.method == 'POST':
        year_built = request.form['year_built']
        make_model = request.form['make_model']
        color = request.form['color']
        boat_type = request.form['type']
        condition = request.form['condition']
        price = request.form['price']
        description = request.form['description']
        city = request.form['city']
        phone_number = request.form['phone_number']
        if 'username' not in session:
            return redirect(url_for('login'))
        user = User.query.filter_by(username=session['username']).first()
        entry = Boat(year_built=year_built, make_model=make_model, color=color, type=boat_type,
                     condition=condition, price=price, description=description, city=city,
                     phone_number=phone_number, user=user)
        db.session.add(entry)
        db.session.commit()
        flash('New entry was successfully created.')
        return redirect(url_for('home'))

    return render_template('createEntry.html')

@app.route('/create_book', methods=['GET', 'POST']) 
def create_book():
    if request.method == 'POST':
        year_released = request.form['year_released']
        title = request.form['title']
        author = request.form['author']
        pages = request.form['pages']
        condition = request.form['condition']
        price = request.form['price']
        description = request.form['description']
        city = request.form['city']
        phone_number = request.form['phone_number']
        if 'username' not in session:
            return redirect(url_for('login'))
        user = User.query.filter_by(username=session['username']).first()
        entry = Books(year_released=year_released, title=title, author=author, pages=pages,
                     condition=condition, price=price, description=description, city=city,
                     phone_number=phone_number, user=user)
        db.session.add(entry)
        db.session.commit()
        flash('New entry was successfully created.')
        return redirect(url_for('home'))

    return render_template('createEntry.html')

@app.route('/create_furniture', methods=['GET', 'POST']) 
def create_furniture():
    if request.method == 'POST':
        year_made = request.form['year_made']
        name = request.form['name']
        color = request.form['color']
        condition = request.form['condition']
        price = request.form['price']
        description = request.form['description']
        city = request.form['city']
        phone_number = request.form['phone_number']
        if 'username' not in session:
            return redirect(url_for('login'))
        user = User.query.filter_by(username=session['username']).first()
        entry = Furniture(year_made=year_made, name=name, color=color,
                     condition=condition, price=price, description=description, city=city,
                     phone_number=phone_number, user=user)
        db.session.add(entry)
        db.session.commit()
        flash('New entry was successfully created.')
        return redirect(url_for('home'))

    return render_template('createEntry.html')

@app.route('/create_motorcycles', methods=['GET', 'POST']) 
def create_motorcycles():
    if request.method == 'POST':
        year_built = request.form['year_built']
        make_model = request.form['make_model']
        color = request.form['color']
        boat_type = request.form['type']
        condition = request.form['condition']
        price = request.form['price']
        description = request.form['description']
        city = request.form['city']
        phone_number = request.form['phone_number']
        if 'username' not in session:
            return redirect(url_for('login'))
        user = User.query.filter_by(username=session['username']).first()
        entry = Motorcycles(year_built=year_built, make_model=make_model, color=color, type=boat_type,
                     condition=condition, price=price, description=description, city=city,
                     phone_number=phone_number, user=user)
        db.session.add(entry)
        db.session.commit()
        flash('New entry was successfully created.')
        return redirect(url_for('home'))

    return render_template('createEntry.html')

@app.route('/create_cars_trucks', methods=['GET', 'POST']) 
def create_cars_trucks():
    if request.method == 'POST':
        year_built = request.form['year_built']
        make_model = request.form['make_model']
        color = request.form['color']
        boat_type = request.form['type']
        condition = request.form['condition']
        price = request.form['price']
        description = request.form['description']
        city = request.form['city']
        phone_number = request.form['phone_number']
        if 'username' not in session:
            return redirect(url_for('login'))
        user = User.query.filter_by(username=session['username']).first()
        entry = Cars_Trucks(year_built=year_built, make_model=make_model, color=color, type=boat_type,
                     condition=condition, price=price, description=description, city=city,
                     phone_number=phone_number, user=user)
        db.session.add(entry)
        db.session.commit()
        flash('New entry was successfully created.')
        return redirect(url_for('home'))

    return render_template('createEntry.html')

@app.route('/create_apartment', methods=['GET', 'POST'])
def create_apartment():
    if request.method == 'POST':
        title = request.form['title']
        bedrooms = request.form['bedrooms']
        bathrooms = request.form['bathrooms']
        square_footage = request.form['square_footage']
        monthly_rent = request.form['monthly_rent']
        description = request.form['description']
        amenities = request.form['amenities']
        city = request.form['city']
        phone_number = request.form['phone_number']
        if 'username' not in session:
            return redirect(url_for('login'))
        user = User.query.filter_by(username=session['username']).first()
        entry = Apartments(title=title, bedrooms=bedrooms, bathrooms=bathrooms,
                    square_footage=square_footage, monthly_rent=monthly_rent,
                    description=description, amenities=amenities, city=city,
                    phone_number=phone_number, user=user)
        db.session.add(entry)
        db.session.commit()
        flash('New entry was successfully created.')
        return redirect(url_for('home'))

    return render_template('createEntry.html')

@app.route('/create_condo', methods=['GET', 'POST'])
def create_condo():
    if request.method == 'POST':
        title = request.form['title']
        bedrooms = request.form['bedrooms']
        bathrooms = request.form['bathrooms']
        square_footage = request.form['square_footage']
        price = request.form['price']
        hoa_fees = request.form['hoa_fees']
        description = request.form['description']
        amenities = request.form['amenities']
        city = request.form['city']
        phone_number = request.form['phone_number']
        if 'username' not in session:
            return redirect(url_for('login'))
        user = User.query.filter_by(username=session['username']).first()
        entry = Condos(title=title, bedrooms=bedrooms, bathrooms=bathrooms,
                       square_footage=square_footage, price=price, hoa_fees=hoa_fees,
                       description=description, amenities=amenities, city=city,
                       phone_number=phone_number, user=user)
        db.session.add(entry)
        db.session.commit()
        flash('New entry was successfully created.')
        return redirect(url_for('home'))

    return render_template('create_condo.html')

@app.route('/create_house', methods=['GET', 'POST'])
def create_house():
    if request.method == 'POST':
        title = request.form['title']
        bedrooms = request.form['bedrooms']
        bathrooms = request.form['bathrooms']
        square_footage = request.form['square_footage']
        lot_size = request.form['lot_size']
        price = request.form['price']
        description = request.form['description']
        city = request.form['city']
        phone_number = request.form['phone_number']
        if 'username' not in session:
            return redirect(url_for('login'))
        user = User.query.filter_by(username=session['username']).first()
        entry = Houses(title=title, bedrooms=bedrooms, bathrooms=bathrooms,
                       square_footage=square_footage, lot_size=lot_size, price=price,
                       description=description, city=city, phone_number=phone_number,
                       user=user)
        db.session.add(entry)
        db.session.commit()
        flash('New entry was successfully created.')
        return redirect(url_for('home'))

    return render_template('create_house.html')

@app.route('/create_roomate', methods=['GET', 'POST'])
def create_roomate():
    if request.method == 'POST':
        title = request.form['title']
        rooms = request.form['rooms']
        preferences = request.form['preferences']
        bathrooms = request.form['bathrooms']
        shared_spaces = request.form['shared_spaces']
        monthly_rate = request.form['monthly_rate']
        description = request.form['description']
        city = request.form['city']
        phone_number = request.form['phone_number']
        if 'username' not in session:
            return redirect(url_for('login'))
        user = User.query.filter_by(username=session['username']).first()
        entry = Roomates(title=title, rooms=rooms, preferences=preferences,
                       bathrooms=bathrooms, shared_spaces=shared_spaces, monthly_rate=monthly_rate,
                       description=description, city=city, phone_number=phone_number, user=user)
        db.session.add(entry)
        db.session.commit()
        flash('New entry was successfully created.')
        return redirect(url_for('home'))

    return render_template('create_roomate.html')

@app.route('/create_vacation', methods=['GET', 'POST'])
def create_vacation():
    if request.method == 'POST':
        title = request.form['title']
        bedrooms = request.form['bedrooms']
        bathrooms = request.form['bathrooms']
        amenities = request.form['amenities']
        nightly_rate = request.form['nightly_rate']
        minimum_stay = request.form['minimum_stay']
        description = request.form['description']
        city = request.form['city']
        phone_number = request.form['phone_number']
        if 'username' not in session:
            return redirect(url_for('login'))
        user = User.query.filter_by(username=session['username']).first()
        entry = Vacation(title=title, bedrooms=bedrooms, bathrooms=bathrooms,
                         amenities=amenities, nightly_rate=nightly_rate, minimum_stay=minimum_stay,
                         description=description, city=city, phone_number=phone_number, user=user)
        db.session.add(entry)
        db.session.commit()
        flash('New entry was successfully created.')
        return redirect(url_for('home'))

    return render_template('create_vacation.html')

@app.route('/create_entry', methods=['GET', 'POST']) 
def create_entry():
    return render_template('createEntry.html', username=session["username"])

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            session['username'] = username
            return redirect(url_for('home'))
        else:
            return render_template('login.html', error='Invalid username or password')
    else:
        return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if not username or not password:
            error = 'Both username and password are required.'
        elif User.query.filter_by(username=username).first() is not None:
            error = f'The username "{username}" is already taken.'
        else:
            user = User(username=username, password=generate_password_hash(password))
            db.session.add(user)
            db.session.commit()
            flash(f'Account created for {username}! Please login.')
            return redirect(url_for('login'))
    return render_template('register.html', error=error)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

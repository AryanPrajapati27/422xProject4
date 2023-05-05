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

@app.route('/jobs/babysitter')
def babysitter():
    entries = Babysitter.query.all()
    if 'username' not in session:
        return render_template('babysitter.html', entries=entries)

    return render_template('babysitter.html', username=session["username"], entries=entries)
@app.route('/jobs/tutor')
def tutor():
    entries = Tutor.query.all()
    if 'username' not in session:
        return render_template('tutor.html', entries=entries)

    return render_template('tutor.html', username=session["username"], entries=entries)
@app.route('/jobs/moving')
def moving():
    entries = Moving.query.all()
    if 'username' not in session:
        return render_template('moving.html', entries=entries)

    return render_template('moving.html', username=session["username"], entries=entries)
@app.route('/jobs/webdesign')
def webdesign():
    entries = Webdesign.query.all()
    if 'username' not in session:
        return render_template('webdesign.html', entries=entries)

    return render_template('webdesign.html', username=session["username"], entries=entries)
@app.route('/jobs/foodservice')
def foodservice():
    entries = Foodservice.query.all()
    if 'username' not in session:
        return render_template('foodservice.html', entries=entries)

    return render_template('foodservice.html', username=session["username"], entries=entries)
@app.route('/services/homeservice')
def homeservice():
    entries = Homeservice.query.all()
    if 'username' not in session:
        return render_template('homeservice.html', entries=entries)

    return render_template('homeservice.html', username=session["username"], entries=entries)

@app.route('/services/transportservice')
def transportservice():
    entries = Transportservice.query.all()
    if 'username' not in session:
        return render_template('transportservice.html', entries=entries)

    return render_template('transportservice.html', username=session["username"], entries=entries)

@app.route('/services/hygieneservice')
def hygieneservice():
    entries = Hygieneservice.query.all()
    if 'username' not in session:
        return render_template('hygieneservice.html', entries=entries)

    return render_template('hygieneservice.html', username=session["username"], entries=entries)

@app.route('/services/eventservice')
def eventservice():
    entries = Eventservice.query.all()
    if 'username' not in session:
        return render_template('eventservice.html', entries=entries)

    return render_template('eventservice.html', username=session["username"], entries=entries)

@app.route('/services/techservice')
def techservice():
    entries = Techservice.query.all()
    if 'username' not in session:
        return render_template('techservice.html', entries=entries)

    return render_template('techservice.html', username=session["username"], entries=entries)
####
@app.route('/community/event')
def event():
    entries = Event.query.all()
    if 'username' not in session:
        return render_template('event.html', entries=entries)

    return render_template('event.html', username=session["username"], entries=entries)

@app.route('/community/group')
def group():
    entries = Group.query.all()
    if 'username' not in session:
        return render_template('group.html', entries=entries)

    return render_template('group.html', username=session["username"], entries=entries)

@app.route('/community/lostfound')
def lostfound():
    entries = LostFound.query.all()
    if 'username' not in session:
        return render_template('lostfound.html', entries=entries)

    return render_template('lostfound.html', username=session["username"], entries=entries)

@app.route('/community/volunteer')
def volunteer():
    entries = Volunteer.query.all()
    if 'username' not in session:
        return render_template('volunteer.html', entries=entries)

    return render_template('volunteer.html', username=session["username"], entries=entries)

@app.route('/community/general')
def general():
    entries = General.query.all()
    if 'username' not in session:
        return render_template('general.html', entries=entries)

    return render_template('general.html', username=session["username"], entries=entries)

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
@app.route('/create_babysitter', methods=['GET', 'POST'])
def create_babysitter():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        pay = request.form['pay']
        serviceTerm = request.form['serviceterm']
        city = request.form['city']
        state = request.form['state']
        phone_number = request.form['phone_number']
        if 'username' not in session:
            return redirect(url_for('login'))
        user = User.query.filter_by(username=session['username']).first()
        entry = Babysitter(title=title, description=description, pay=pay,
                         serviceTerm=serviceTerm, city=city, state=state,
                         phone_number=phone_number, user=user)
        db.session.add(entry)
        db.session.commit()
        flash('New entry was successfully created.')
        return redirect(url_for('home'))

    return render_template('create_babysitter.html')
@app.route('/create_tutor', methods=['GET', 'POST'])
def create_tutor():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        pay = request.form['pay']
        serviceTerm = request.form['serviceterm']
        city = request.form['city']
        state = request.form['state']
        phone_number = request.form['phone_number']
        if 'username' not in session:
            return redirect(url_for('login'))
        user = User.query.filter_by(username=session['username']).first()
        entry = Tutor(title=title, description=description, pay=pay,
                         serviceTerm=serviceTerm, city=city, state=state,
                         phone_number=phone_number, user=user)
        db.session.add(entry)
        db.session.commit()
        flash('New entry was successfully created.')
        return redirect(url_for('home'))

    return render_template('create_tutor.html')

@app.route('/create_moving', methods=['GET', 'POST'])
def create_moving():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        pay = request.form['pay']
        date = request.form['date']
        city = request.form['city']
        state = request.form['state']
        phone_number = request.form['phone_number']
        if 'username' not in session:
            return redirect(url_for('login'))
        user = User.query.filter_by(username=session['username']).first()
        entry = Moving(title=title, description=description, pay=pay,
                         date=date, city=city, state=state,
                         phone_number=phone_number, user=user)
        db.session.add(entry)
        db.session.commit()
        flash('New entry was successfully created.')
        return redirect(url_for('home'))

    return render_template('create_moving.html')

@app.route('/create_webdesign', methods=['GET', 'POST'])
def create_webdesign():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        pay = request.form['pay']
        serviceterm = request.form['serviceterm']
        languages = request.form['languages']
        requirments = request.form['requirments']
        phone_number = request.form['phone_number']
        if 'username' not in session:
            return redirect(url_for('login'))
        user = User.query.filter_by(username=session['username']).first()
        entry = Webdesign(title=title, description=description, pay=pay,
                         serviceterm=serviceterm, languages=languages, requirments=requirments,
                         phone_number=phone_number, user=user)
        db.session.add(entry)
        db.session.commit()
        flash('New entry was successfully created.')
        return redirect(url_for('home'))

    return render_template('create_webdesign.html')

@app.route('/create_foodservice', methods=['GET', 'POST'])
def create_foodservice():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        pay = request.form['pay']
        serviceterm = request.form['serviceterm']
        city = request.form['city']
        state = request.form['state']
        phone_number = request.form['phone_number']
        if 'username' not in session:
            return redirect(url_for('login'))
        user = User.query.filter_by(username=session['username']).first()
        entry = Foodservice(title=title, description=description, pay=pay,
                         serviceterm=serviceterm, city=city, state=state,
                         phone_number=phone_number, user=user)
        db.session.add(entry)
        db.session.commit()
        flash('New entry was successfully created.')
        return redirect(url_for('home'))

    return render_template('create_foodservice.html')
@app.route('/create_entry', methods=['GET', 'POST']) 
def create_entry():
    return render_template('createEntry.html', username=session["username"])

@app.route('/create_homeservice', methods =['GET','POST'])
def create_homeservice():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        price = request.form['price']
        availability = request.form['availability']
        service_location =request.form['service_location']
        phone_number = request.form['phone_number']
        email = request.form['email']
        if 'username' not in session:
            return redirect(url_for('login'))
        user = User.query.filter_by(username=session['username']).first()
        entry = Homeservice(title=title,description=description,price=price,
                        availability=availability,service_location=service_location,
                        phone_number=phone_number,email=email,user=user)
        db.session.add(entry)
        db.session.commit()
        flash('New entry was successfully created.')
        return redirect(url_for('home'))
    return render_template('create_homeservice.html')

@app.route('/create_transportservice', methods =['GET','POST'])
def create_transportservice():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        price_per_mile = request.form['price_per_mile']
        availability = request.form['availability']
        service_coverage_area = request.form['service_coverage_area']
        pick_up_location = request.form['pick_up_location']
        drop_off_location = request.form['drop_off_location']
        payment_methods = request.form['payment_methods']
        phone_number = request.form['phone_number']
        email = request.form['email']
        if 'username' not in session:
            return redirect(url_for('login'))
        user = User.query.filter_by(username=session['username']).first()
        entry = Transportservice(title=title,description=description,price_per_mile=price_per_mile,
                        availability=availability,service_coverage_area=service_coverage_area,
                        pick_up_location=pick_up_location,drop_off_location=drop_off_location,
                        payment_methods=payment_methods,phone_number=phone_number,email=email,user=user)
        db.session.add(entry)
        db.session.commit()
        flash('New entry was successfully created.')
        return redirect(url_for('home'))
    return render_template('create_transportservice.html')

@app.route('/create_hygieneservice', methods =['GET','POST'])
def create_hygieneservice():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        price = request.form['price']
        duration =  request.form['duration']
        appointment_availability =  request.form['appointment_availability']
        service_location =  request.form['service_location']
        phone_number =  request.form['phone_number']
        email =  request.form['email']
        if 'username' not in session:
            return redirect(url_for('login'))
        user = User.query.filter_by(username=session['username']).first()
        entry = Hygieneservice(title=title,description=description,price=price,duration=duration,
                        appointment_availability=appointment_availability,service_location=service_location,
                        phone_number=phone_number,email=email,user=user)
        db.session.add(entry)
        db.session.commit()
        flash('New entry was successfully created.')
        return redirect(url_for('home'))
    return render_template('create_hygieneservice.html')


@app.route('/create_eventservice', methods =['GET','POST'])
def create_eventservice():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        budget = request.form['budget']
        availability = request.form['availability']
        event_date = request.form['event_date']
        guest_count = request.form['guest_count']
        event_location = request.form['event_location']
        phone_number = request.form['phone_number']
        email = request.form['email']
        if 'username' not in session:
            return redirect(url_for('login'))
        user = User.query.filter_by(username=session['username']).first()
        entry = Eventservice(title=title,description=description,budget=budget,availability=availability,
                        event_date=event_date,guest_count=guest_count,event_location=event_location,
                        phone_number=phone_number,email=email,user=user)
        db.session.add(entry)
        db.session.commit()
        flash('New entry was successfully created.')
        return redirect(url_for('home'))
    return render_template('create_eventservice.html')


@app.route('/create_techservice', methods =['GET','POST'])
def create_techservice():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        price = request.form['price']
        availability = request.form['availability']
        service_location = request.form['service_location']
        skills_and_expertise = request.form['skills_and_expertise']
        certifications = request.form['certifications']
        phone_number = request.form['phone_number']
        email = request.form['email']
        if 'username' not in session:
            return redirect(url_for('login'))
        user = User.query.filter_by(username=session['username']).first()    
        entry = Techservice(title=title,description=description,price=price,availability=availability,
                        service_location=service_location,skills_and_expertise=skills_and_expertise,
                        certifications=certifications,phone_number=phone_number,email=email,user=user)
        db.session.add(entry)
        db.session.commit()
        flash('New entry was successfully created.')
        return redirect(url_for('home'))
    return render_template('create_techservice.html')

@app.route('/create_event', methods=['GET', 'POST'])
def create_event():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        date = request.form['date']
        time = request.form['time']
        location = request.form['location']
        organizer_name = request.form['organizer_name']
        organizer_contact = request.form['organizer_contact']
        phone_number = request.form['phone_number']
        price = request.form['price']
        capacity = request.form['capacity']
        if 'username' not in session:
            return redirect(url_for('login'))
        user = User.query.filter_by(username=session['username']).first()
        entry = Event(title=title, description=description, date=date, time=time, location=location,
                      organizer_name=organizer_name, organizer_contact=organizer_contact, phone_number=phone_number,
                      price=price, capacity=capacity, user=user)
        db.session.add(entry)
        db.session.commit()
        flash('New event was successfully created.')
        return redirect(url_for('home'))

    return render_template('create_event.html')

@app.route('/create_group', methods=['GET', 'POST'])
def create_group():
    if request.method == 'POST':
        title = request.form['title']
        group_type = request.form['group_type']
        description = request.form['description']
        meeting_time = request.form['meeting_time']
        meeting_location = request.form['meeting_location']
        contact_info = request.form['contact_info']
        size = request.form['size']
        membership_fee = request.form['membership_fee']
        membership_requirements = request.form['membership_requirements']
        phone_number = request.form['phone_number']
        if 'username' not in session:
            return redirect(url_for('login'))
        user = User.query.filter_by(username=session['username']).first()
        entry = Group(title=title, group_type=group_type, description=description,
                      meeting_time=meeting_time, meeting_location=meeting_location,
                      contact_info=contact_info, size=size, membership_fee=membership_fee,
                      membership_requirements=membership_requirements, phone_number=phone_number, user=user)
        db.session.add(entry)
        db.session.commit()
        flash('New entry was successfully created.')
        return redirect(url_for('home'))
    return render_template('create_group.html')

@app.route('/create_lostfound', methods=['GET', 'POST'])
def create_lostfound():
    if request.method == 'POST':
        title = request.form['title']
        item_type = request.form['item_type']
        description = request.form['description']
        location = request.form['location']
        date_lost_found = request.form['date_lost_found']
        contact_info = request.form['contact_info']
        image_url = request.form['image_url']
        status = request.form['status']
        phone_number = request.form['phone_number']
        if 'username' not in session:
            return redirect(url_for('login'))
        user = User.query.filter_by(username=session['username']).first()
        entry = LostFound(title=title, item_type=item_type, description=description, location=location,
                          date_lost_found=date_lost_found, contact_info=contact_info, image_url=image_url,
                          status=status, phone_number=phone_number, user=user)
        db.session.add(entry)
        db.session.commit()
        flash('New entry was successfully created.')
        return redirect(url_for('home'))
    return render_template('create_lostfound.html')

@app.route('/create_volunteer', methods=['GET', 'POST'])
def create_volunteer():
    if request.method == 'POST':
        title = request.form['title']
        email = request.form['email']
        phone_number = request.form['phone_number']
        location = request.form['location']
        skills = request.form['skills']
        interests = request.form['interests']
        availability = request.form['availability']
        experience = request.form['experience']
        if 'username' not in session:
            return redirect(url_for('login'))
        user = User.query.filter_by(username=session['username']).first()
        entry = Volunteer(title=title, email=email, phone_number=phone_number, location=location, 
                          skills=skills, interests=interests, availability=availability, experience=experience,
                          user=user)
        db.session.add(entry)
        db.session.commit()
        flash('New entry was successfully created.')
        return redirect(url_for('home'))
    return render_template('create_volunteer.html')

@app.route('/create_general', methods=['GET', 'POST'])
def create_general():
    if request.method == 'POST':
        title = request.form['title']
        category = request.form['category']
        description = request.form['description']
        location = request.form['location']
        price = request.form['price']
        contact_info = request.form['contact_info']
        image_url = request.form['image_url']
        phone_number = request.form['phone_number']
        tags = request.form['tags']
        if 'username' not in session:
            return redirect(url_for('login'))
        user = User.query.filter_by(username=session['username']).first()    
        entry = General(title=title, category=category, description=description, location=location, price=price,
                        contact_info=contact_info, image_url=image_url, phone_number=phone_number, tags=tags, user=user)
        db.session.add(entry)
        db.session.commit()
        flash('New entry was successfully created.')
        return redirect(url_for('home'))
    return render_template('create_general.html')

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

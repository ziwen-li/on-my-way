from flask import Flask, render_template, request, redirect, url_for
from models import db, TravelOffer, DeliveryRequest
from config import DevelopmentConfig

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

db.init_app(app)


@app.before_request
def create_tables():
    db.create_all()


@app.route('/')
def index():
    requests_ = DeliveryRequest.query.order_by(DeliveryRequest.created_at.desc()).all()
    offers = TravelOffer.query.order_by(TravelOffer.created_at.desc()).all()
    return render_template('index.html', offers=offers, requests=requests_)


# ---------- Travel Offers ----------

@app.route('/offers')
def offers_list():
    offers = TravelOffer.query.order_by(TravelOffer.created_at.desc()).all()
    return render_template('offers_list.html', offers=offers)


@app.route('/offers/new', methods=['GET', 'POST'])
def offer_new():
    if request.method == 'POST':
        offer = TravelOffer(
            from_country=request.form['from_country'],
            from_city=request.form.get('from_city'),
            to_country=request.form['to_country'],
            to_city=request.form.get('to_city'),
            travel_date=request.form['travel_date'],
            available_weight=request.form['available_weight'],
            item_type=request.form['item_type'],
            reward=request.form['reward'],
            contact=request.form['contact']
        )
        db.session.add(offer)
        db.session.commit()
        return redirect(url_for('offers_list'))

    return render_template('offer_new.html')


# ---------- Delivery Requests ----------

@app.route('/requests')
def requests_list():
    requests_ = DeliveryRequest.query.order_by(DeliveryRequest.created_at.desc()).all()
    return render_template('requests_list.html', requests=requests_)


@app.route('/requests/new', methods=['GET', 'POST'])
def request_new():
    if request.method == 'POST':
        req = DeliveryRequest(
            from_country=request.form['from_country'],
            to_country=request.form['to_country'],
            item_description=request.form['item_description'],
            weight=request.form['weight'],
            desired_date=request.form['desired_date'],
            budget=request.form['budget'],
            contact=request.form['contact']
        )
        db.session.add(req)
        db.session.commit()
        return redirect(url_for('requests_list'))

    return render_template('request_new.html')


if __name__ == '__main__':
    app.run(debug=True)

from flask import Blueprint, render_template
from flask_login import login_required, current_user


views = Blueprint('views', __name__)


@views.route('/')
def index():
    return render_template('index.html')

@views.route('/checkout')
def checkout():
    return render_template('checkout.html')

@views.route('/cart')
def cart():
    return render_template('cart.html')

@views.route('/admin')
@login_required
def admin():
    return 'ok'
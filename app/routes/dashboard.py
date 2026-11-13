from flask import Blueprint, render_template
from flask_login import login_required, current_user
from app.models import Membership, Booking

bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')

@bp.route('/')
@login_required
def index():
    memberships = Membership.query.filter_by(user_id=current_user.id).all()
    bookings = Booking.query.filter_by(user_id=current_user.id).all()
    return render_template('dashboard.html',
                           memberships=memberships,
                           bookings=bookings)
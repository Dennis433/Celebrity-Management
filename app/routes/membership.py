from flask import Blueprint, render_template
from app.models import MembershipCard

bp = Blueprint('membership', __name__, url_prefix='/membership')

@bp.route('/')
def index():
    cards = MembershipCard.query.filter_by(is_active=True).all()
    return render_template('membership.html', cards=cards)
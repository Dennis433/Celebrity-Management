from flask import Blueprint, render_template
from app.models import Experience

bp = Blueprint('experiences', __name__, url_prefix='/experiences')

@bp.route('/')
def index():
    experiences = Experience.query.filter_by(is_active=True).all()
    return render_template('experiences.html', experiences=experiences)
from flask import Blueprint, render_template, request
from app.models import Celebrity

bp = Blueprint('celebrities', __name__, url_prefix='/celebrities')

@bp.route('/')
def index():
    search = request.args.get('search', '')
    category = request.args.get('category', '')

    query = Celebrity.query.filter_by(is_active=True)

    if search:
        query = query.filter(Celebrity.name.ilike(f'%{search}%'))

    if category:
        query = query.filter_by(category=category)

    celebrities = query.order_by(Celebrity.name).all()

    categories = [
        'Musicians and Singers',
        'Actors and Actresses',
        'Athletes and Sports',
        'Television and Entertainment',
        'WWE Superstars'
    ]

    return render_template('celebrities.html',
                           celebrities=celebrities,
                           categories=categories,
                           search=search,
                           selected_category=category)

@bp.route('/<int:celeb_id>')
def detail(celeb_id):
    celeb = Celebrity.query.get_or_404(celeb_id)
    related = Celebrity.query.filter_by(
        category=celeb.category,
        is_active=True
    ).filter(Celebrity.id != celeb_id).limit(4).all()
    return render_template('celebrity_detail.html',
                           celeb=celeb,
                           related=related)
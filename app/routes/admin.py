from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app import db
from app.models import User, MembershipCard, Membership, Experience, Booking, Celebrity
from functools import wraps
import os
import cloudinary
import cloudinary.uploader
from werkzeug.utils import secure_filename

bp = Blueprint('admin', __name__, url_prefix='/admin')

ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'webp'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or not current_user.is_admin:
            flash('Access denied. Admins only.', 'danger')
            return redirect(url_for('main.index'))
        return f(*args, **kwargs)
    return decorated_function

def upload_to_cloudinary(file, folder='celebrities'):
    """Upload file to Cloudinary and return URL"""
    try:
        result = cloudinary.uploader.upload(
            file,
            folder=f'ocm/{folder}',
            transformation=[
                {'width': 400, 'height': 400, 'crop': 'fill', 'gravity': 'face'},
                {'quality': 'auto', 'fetch_format': 'auto'}
            ]
        )
        return result.get('secure_url')
    except Exception as e:
        print(f'Cloudinary upload error: {e}')
        return None

@bp.route('/')
@login_required
@admin_required
def dashboard():
    total_users = User.query.count()
    total_memberships = Membership.query.count()
    total_experiences = Experience.query.count()
    total_bookings = Booking.query.count()
    total_celebrities = Celebrity.query.count()
    recent_users = User.query.order_by(User.created_at.desc()).limit(5).all()
    recent_bookings = Booking.query.order_by(Booking.booked_at.desc()).limit(5).all()
    return render_template('admin/dashboard.html',
                           total_users=total_users,
                           total_memberships=total_memberships,
                           total_experiences=total_experiences,
                           total_bookings=total_bookings,
                           total_celebrities=total_celebrities,
                           recent_users=recent_users,
                           recent_bookings=recent_bookings)

@bp.route('/users')
@login_required
@admin_required
def users():
    all_users = User.query.order_by(User.created_at.desc()).all()
    return render_template('admin/users.html', users=all_users)

@bp.route('/users/toggle-admin/<int:user_id>')
@login_required
@admin_required
def toggle_admin(user_id):
    user = User.query.get_or_404(user_id)
    if user.id == current_user.id:
        flash('You cannot change your own admin status.', 'warning')
    else:
        user.is_admin = not user.is_admin
        db.session.commit()
        flash(f'{"Admin granted to" if user.is_admin else "Admin removed from"} {user.username}.', 'success')
    return redirect(url_for('admin.users'))

@bp.route('/experiences')
@login_required
@admin_required
def experiences():
    all_experiences = Experience.query.order_by(Experience.date.desc()).all()
    return render_template('admin/experiences.html', experiences=all_experiences)

@bp.route('/experiences/add', methods=['GET', 'POST'])
@login_required
@admin_required
def add_experience():
    if request.method == 'POST':
        from datetime import datetime
        exp = Experience(
            title=request.form.get('title'),
            description=request.form.get('description'),
            price=float(request.form.get('price')),
            location=request.form.get('location'),
            capacity=int(request.form.get('capacity')),
            date=datetime.strptime(request.form.get('date'), '%Y-%m-%dT%H:%M') if request.form.get('date') else None,
            is_active=True
        )
        db.session.add(exp)
        db.session.commit()
        flash('Experience added successfully.', 'success')
        return redirect(url_for('admin.experiences'))
    return render_template('admin/experiences.html', add_mode=True,
                           experiences=Experience.query.all())

@bp.route('/experiences/delete/<int:exp_id>')
@login_required
@admin_required
def delete_experience(exp_id):
    exp = Experience.query.get_or_404(exp_id)
    db.session.delete(exp)
    db.session.commit()
    flash('Experience deleted.', 'success')
    return redirect(url_for('admin.experiences'))

@bp.route('/memberships')
@login_required
@admin_required
def memberships():
    all_memberships = Membership.query.order_by(Membership.purchased_at.desc()).all()
    return render_template('admin/memberships.html', memberships=all_memberships)

@bp.route('/celebrities')
@login_required
@admin_required
def celebrities():
    search = request.args.get('search', '')
    category = request.args.get('category', '')
    query = Celebrity.query
    if search:
        query = query.filter(Celebrity.name.ilike(f'%{search}%'))
    if category:
        query = query.filter_by(category=category)
    all_celebrities = query.order_by(Celebrity.name).all()
    categories = [
        'Musicians and Singers',
        'Actors and Actresses',
        'Athletes and Sports',
        'Television and Entertainment',
        'WWE Superstars'
    ]
    return render_template('admin/celebrities.html',
                           celebrities=all_celebrities,
                           categories=categories,
                           search=search,
                           selected_category=category)

@bp.route('/celebrities/upload-image/<int:celeb_id>', methods=['POST'])
@login_required
@admin_required
def upload_celebrity_image(celeb_id):
    celeb = Celebrity.query.get_or_404(celeb_id)
    if 'image' not in request.files:
        flash('No file selected.', 'danger')
        return redirect(url_for('admin.celebrities'))
    file = request.files['image']
    if file.filename == '':
        flash('No file selected.', 'danger')
        return redirect(url_for('admin.celebrities'))
    if file and allowed_file(file.filename):
        # Try Cloudinary first
        cloudinary_url = upload_to_cloudinary(file, folder='celebrities')
        if cloudinary_url:
            celeb.image = cloudinary_url
            db.session.commit()
            flash(f'Image uploaded to cloud for {celeb.name}.', 'success')
        else:
            # Fallback to local storage
            ext = file.filename.rsplit('.', 1)[1].lower()
            slug = celeb.name.lower().replace(' ', '-').replace('.', '').replace("'", '')
            filename = f'{slug}.{ext}'
            save_path = os.path.join('app', 'static', 'images', 'celebrities', filename)
            os.makedirs(os.path.dirname(save_path), exist_ok=True)
            file.seek(0)
            file.save(save_path)
            celeb.image = f'images/celebrities/{filename}'
            db.session.commit()
            flash(f'Image saved locally for {celeb.name}.', 'success')
    else:
        flash('Invalid file type. Use jpg, jpeg, png or webp.', 'danger')
    return redirect(url_for('admin.celebrities'))

@bp.route('/celebrities/delete-image/<int:celeb_id>')
@login_required
@admin_required
def delete_celebrity_image(celeb_id):
    celeb = Celebrity.query.get_or_404(celeb_id)
    if celeb.image:
        # Only delete local files, not Cloudinary URLs
        if not celeb.image.startswith('http'):
            file_path = os.path.join('app', 'static', celeb.image)
            if os.path.exists(file_path):
                os.remove(file_path)
        celeb.image = None
        db.session.commit()
        flash(f'Image removed for {celeb.name}.', 'success')
    return redirect(url_for('admin.celebrities'))

@bp.route('/celebrities/edit/<int:celeb_id>', methods=['GET', 'POST'])
@login_required
@admin_required
def edit_celebrity(celeb_id):
    celeb = Celebrity.query.get_or_404(celeb_id)
    if request.method == 'POST':
        celeb.bio = request.form.get('bio')
        celeb.net_worth = request.form.get('net_worth')
        celeb.nationality = request.form.get('nationality')
        celeb.born = request.form.get('born')
        celeb.known_for = request.form.get('known_for')
        db.session.commit()

        # Handle image upload
        if 'image' in request.files:
            file = request.files['image']
            if file and file.filename != '' and allowed_file(file.filename):
                cloudinary_url = upload_to_cloudinary(file, folder='celebrities')
                if cloudinary_url:
                    celeb.image = cloudinary_url
                    db.session.commit()

        flash(f'Profile updated for {celeb.name}.', 'success')
        return redirect(url_for('admin.celebrities'))
    return render_template('admin/edit_celebrity.html', celeb=celeb)
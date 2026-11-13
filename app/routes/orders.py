from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user
from app import db
from app.models import BookingRequest
import urllib.parse

bp = Blueprint('orders', __name__, url_prefix='/orders')

PACKAGES = {
    'membership_silver': {
        'name': 'Silver Membership Card',
        'price': '$300.00',
        'type': 'Membership Card',
        'description': 'Official membership card with fan club newsletter and member discounts.',
        'perks': ['Official membership card', 'Fan club newsletter', 'Member discounts']
    },
    'membership_gold': {
        'name': 'Gold Membership Card',
        'price': '$375.00',
        'type': 'Membership Card',
        'description': 'Priority event access, early merch drops and exclusive content.',
        'perks': ['Everything in Silver', 'Priority event access', 'Early merch drops', 'Exclusive content']
    },
    'membership_platinum': {
        'name': 'Platinum Membership Card',
        'price': '$500.00',
        'type': 'Membership Card',
        'description': 'VIP event invitations, meet & greet priority and signed merchandise.',
        'perks': ['Everything in Gold', 'VIP event invitations', 'Meet & greet priority', 'Signed merchandise', 'Direct management updates']
    },
    'meetgreet_standard': {
        'name': 'Standard Meet & Greet',
        'price': '$199.99',
        'type': 'Meet & Greet',
        'description': 'A personal one-on-one meeting with photos and autographs.',
        'perks': ['One-on-one meeting', 'Professional photos', 'Autographs', 'Official certificate']
    },
    'meetgreet_vip': {
        'name': 'VIP Meet & Greet',
        'price': '$349.99',
        'type': 'Meet & Greet',
        'description': 'Extended backstage meet and greet with exclusive access.',
        'perks': ['Extended meeting time', 'Backstage access', 'Professional photos', 'Autographs', 'Gift package']
    },
    'meetgreet_private': {
        'name': 'Private Meet & Greet Session',
        'price': '$999.99',
        'type': 'Meet & Greet',
        'description': 'Fully private session with the celebrity.',
        'perks': ['Private session', 'Unlimited photos', 'Video message', 'Signed merchandise', 'Gift package', 'Certificate of authenticity']
    },
    'vacation_weekend': {
        'name': 'Celebrity Weekend Getaway',
        'price': '$2,499.99',
        'type': 'Vacation Package',
        'description': 'An exclusive weekend vacation experience with the celebrity.',
        'perks': ['2-night luxury stay', 'Private dinner', 'Exclusive activities', 'Professional photoshoot', 'Gift package']
    },
    'vacation_vip': {
        'name': 'VIP Vacation Experience',
        'price': '$4,999.99',
        'type': 'Vacation Package',
        'description': 'A fully immersive VIP vacation alongside the celebrity.',
        'perks': ['5-night luxury stay', 'Private jet experience', 'Multiple dinners', 'Exclusive events', 'Professional photoshoot', 'Signed memorabilia']
    },
}

@bp.route('/book/<package_key>', methods=['GET', 'POST'])
def book(package_key):
    package = PACKAGES.get(package_key)
    if not package:
        flash('Invalid package selected.', 'danger')
        return redirect(url_for('membership.index'))

    celebrity_name = request.args.get('celebrity', '')

    if request.method == 'POST':
        full_name = request.form.get('full_name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        celeb = request.form.get('celebrity_name', celebrity_name)

        booking = BookingRequest(
            full_name=full_name,
            email=email,
            phone=phone,
            request_type=package['type'],
            package=package['name'],
            price=package['price'],
            celebrity_name=celeb,
            message=message,
            user_id=current_user.id if current_user.is_authenticated else None
        )
        db.session.add(booking)
        db.session.commit()

        subject = f'Booking Request — {package["name"]} | OCM'
        body = f"""Hello Official Celebrity Management Team,

I would like to request the following booking:

━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BOOKING DETAILS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Package:         {package['name']}
Type:            {package['type']}
Price:           {package['price']}
Celebrity:       {celeb if celeb else 'Not specified'}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CUSTOMER DETAILS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Full Name:       {full_name}
Email:           {email}
Phone:           {phone if phone else 'Not provided'}
Booking Ref:     #OCM-{booking.id:05d}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━
MESSAGE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{message if message else 'No additional message.'}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Please reply with payment instructions.

Thank you,
{full_name}
"""
        mailto = f"mailto:officialcelebritymanagement85@gmail.com?subject={urllib.parse.quote(subject)}&body={urllib.parse.quote(body)}"

        return render_template('orders/success.html',
                               booking=booking,
                               package=package,
                               mailto=mailto)

    return render_template('orders/book.html',
                           package=package,
                           package_key=package_key,
                           celebrity_name=celebrity_name)
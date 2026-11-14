from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
from flask_migrate import Migrate
import cloudinary
from config import Config

db = SQLAlchemy()
login_manager = LoginManager()
mail = Mail()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    migrate.init_app(app, db)

    # Configure Cloudinary
    cloudinary.config(
        cloud_name=app.config.get('CLOUDINARY_CLOUD_NAME'),
        api_key=app.config.get('CLOUDINARY_API_KEY'),
        api_secret=app.config.get('CLOUDINARY_API_SECRET'),
        secure=True
    )

    login_manager.login_view = 'auth.login'
    login_manager.login_message_category = 'info'

    with app.app_context():
        # Import models
        from app.models import (User, MembershipCard, Membership,
                                Experience, Booking, Merchandise,
                                Order, OrderItem, Celebrity, BookingRequest)

        # Import and register blueprints
        from app.routes import main, auth, dashboard, membership
        from app.routes import experiences, admin, celebrities, orders
        app.register_blueprint(main.bp)
        app.register_blueprint(auth.bp)
        app.register_blueprint(dashboard.bp)
        app.register_blueprint(membership.bp)
        app.register_blueprint(experiences.bp)
        app.register_blueprint(admin.bp)
        app.register_blueprint(celebrities.bp)
        app.register_blueprint(orders.bp)

        # Auto migrate database
        from flask_migrate import upgrade
        try:
            upgrade()
            print('Database migrated successfully!')
        except Exception as e:
            print(f'Migration note: {e}')

        # Auto create tables if they dont exist
        db.create_all()
        print('Database tables verified!')

    return app
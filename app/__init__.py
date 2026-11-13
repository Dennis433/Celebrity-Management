from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
from flask_migrate import Migrate
from config import Config

db = SQLAlchemy()
login_manager = LoginManager()
mail = Mail()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    migrate.init_app(app, db)

    login_manager.login_view = 'auth.login'
    login_manager.login_message_category = 'info'

    with app.app_context():
        from app.models import User, MembershipCard, Membership
        from app.models import Experience, Booking, Merchandise, Order, OrderItem
        from app.models import Celebrity, BookingRequest
        from app.routes import main, auth, dashboard, membership, experiences, admin, celebrities
        from app.routes import orders
        app.register_blueprint(main.bp)
        app.register_blueprint(auth.bp)
        app.register_blueprint(dashboard.bp)
        app.register_blueprint(membership.bp)
        app.register_blueprint(experiences.bp)
        app.register_blueprint(admin.bp)
        app.register_blueprint(celebrities.bp)
        app.register_blueprint(orders.bp)

    return app
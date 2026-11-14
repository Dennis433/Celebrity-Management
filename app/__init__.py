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

    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    migrate.init_app(app, db)

    cloudinary.config(
        cloud_name=app.config.get('CLOUDINARY_CLOUD_NAME'),
        api_key=app.config.get('CLOUDINARY_API_KEY'),
        api_secret=app.config.get('CLOUDINARY_API_SECRET'),
        secure=True
    )

    login_manager.login_view = 'auth.login'
    login_manager.login_message_category = 'info'

    with app.app_context():
        from app.models import (User, MembershipCard, Membership,
                                Experience, Booking, Merchandise,
                                Order, OrderItem, Celebrity, BookingRequest)

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

        # Auto migrate
        try:
            from flask_migrate import upgrade
            upgrade()
            print('Database migrated!')
        except Exception as e:
            print(f'Migration note: {e}')

        # Auto create tables
        db.create_all()

        # Auto seed on first run
        try:
            auto_seed()
        except Exception as e:
            print(f'Seed note: {e}')

    return app


def auto_seed():
    from app.models import Celebrity, User
    from werkzeug.security import generate_password_hash
    from datetime import datetime

    # Create admin if not exists
    admin = User.query.filter_by(
        email='officialcelebritymanagement85@gmail.com'
    ).first()
    if not admin:
        admin = User(
            username='ocm_admin',
            full_name='Official Celebrity Management',
            email='officialcelebritymanagement85@gmail.com',
            password_hash=generate_password_hash('DeeZee55001199'),
            is_admin=True,
            created_at=datetime.utcnow()
        )
        db.session.add(admin)
        db.session.commit()
        print('Admin created!')
    else:
        if not admin.is_admin:
            admin.is_admin = True
            admin.password_hash = generate_password_hash('DeeZee55001199')
            db.session.commit()
        print('Admin exists!')

    # Seed celebrities if empty
    if Celebrity.query.count() == 0:
        celebrities_data = [
            # Musicians and Singers
            ('Calum Scott', 'Musicians and Singers', 'British', 'October 12, 1988', '$4 Million', 'Dancing On My Own, You Are The Reason'),
            ('Ed Sheeran', 'Musicians and Singers', 'British', 'February 17, 1991', '$200 Million', 'Shape of You, Perfect, Thinking Out Loud'),
            ('Taylor Swift', 'Musicians and Singers', 'American', 'December 13, 1989', '$1.1 Billion', 'Shake It Off, Blank Space, Anti-Hero'),
            ('Justin Bieber', 'Musicians and Singers', 'Canadian', 'March 1, 1994', '$300 Million', 'Baby, Sorry, Love Yourself'),
            ('Adele', 'Musicians and Singers', 'British', 'May 5, 1988', '$220 Million', 'Hello, Rolling in the Deep, Someone Like You'),
            ('Rihanna', 'Musicians and Singers', 'Barbadian', 'February 20, 1988', '$1.4 Billion', 'Umbrella, Diamonds, We Found Love'),
            ('Beyoncé', 'Musicians and Singers', 'American', 'September 4, 1981', '$500 Million', 'Crazy in Love, Halo, Lemonade'),
            ('Drake', 'Musicians and Singers', 'Canadian', 'October 24, 1986', '$250 Million', 'God\'s Plan, Hotline Bling, One Dance'),
            ('Bruno Mars', 'Musicians and Singers', 'American', 'October 8, 1985', '$175 Million', 'Just the Way You Are, Uptown Funk'),
            ('The Weeknd', 'Musicians and Singers', 'Canadian', 'February 16, 1990', '$300 Million', 'Blinding Lights, Starboy, Can\'t Feel My Face'),
            ('Shawn Mendes', 'Musicians and Singers', 'Canadian', 'August 8, 1998', '$40 Million', 'Treat You Better, Stitches'),
            ('Sam Smith', 'Musicians and Singers', 'British', 'May 19, 1992', '$25 Million', 'Stay With Me, Writing\'s on the Wall'),
            ('Lewis Capaldi', 'Musicians and Singers', 'Scottish', 'October 7, 1996', '$10 Million', 'Someone You Loved, Before You Go'),
            ('Charlie Puth', 'Musicians and Singers', 'American', 'December 2, 1991', '$25 Million', 'See You Again, Attention'),
            ('Dua Lipa', 'Musicians and Singers', 'British-Albanian', 'August 22, 1995', '$35 Million', 'Levitating, Don\'t Start Now, New Rules'),
            ('Ariana Grande', 'Musicians and Singers', 'American', 'June 26, 1993', '$200 Million', 'Thank U Next, 7 Rings, Problem'),
            ('Selena Gomez', 'Musicians and Singers', 'American', 'July 22, 1992', '$800 Million', 'Lose You to Love Me, Come & Get It'),
            ('Miley Cyrus', 'Musicians and Singers', 'American', 'November 23, 1992', '$160 Million', 'Wrecking Ball, Flowers, The Climb'),
            ('Lady Gaga', 'Musicians and Singers', 'American', 'March 28, 1986', '$320 Million', 'Poker Face, Bad Romance, Shallow'),
            ('Katy Perry', 'Musicians and Singers', 'American', 'October 25, 1984', '$330 Million', 'Roar, Firework, I Kissed a Girl'),
            ('Chris Brown', 'Musicians and Singers', 'American', 'May 5, 1989', '$50 Million', 'With You, Forever, Look at Me Now'),
            ('Post Malone', 'Musicians and Singers', 'American', 'July 4, 1995', '$45 Million', 'Rockstar, Sunflower, Circles'),
            ('Harry Styles', 'Musicians and Singers', 'British', 'February 1, 1994', '$100 Million', 'Watermelon Sugar, As It Was, Adore You'),
            ('Billie Eilish', 'Musicians and Singers', 'American', 'December 18, 2001', '$25 Million', 'Bad Guy, Happier Than Ever, Ocean Eyes'),
            ('Sia', 'Musicians and Singers', 'Australian', 'December 18, 1975', '$30 Million', 'Chandelier, Cheap Thrills, Titanium'),
            ('Celine Dion', 'Musicians and Singers', 'Canadian', 'March 30, 1968', '$800 Million', 'My Heart Will Go On, The Power of Love'),
            ('Michael Bublé', 'Musicians and Singers', 'Canadian', 'September 9, 1975', '$80 Million', 'Haven\'t Met You Yet, Feeling Good'),
            ('Elton John', 'Musicians and Singers', 'British', 'March 25, 1947', '$550 Million', 'Rocket Man, Tiny Dancer, Your Song'),
            ('Shakira', 'Musicians and Singers', 'Colombian', 'February 2, 1977', '$300 Million', 'Hips Don\'t Lie, Waka Waka, She Wolf'),
            ('Pitbull', 'Musicians and Singers', 'American', 'January 15, 1981', '$100 Million', 'Give Me Everything, Timber, International Love'),

            # Actors and Actresses
            ('Dwayne Johnson', 'Actors and Actresses', 'American', 'May 2, 1972', '$800 Million', 'The Rock, Fast & Furious, Jumanji'),
            ('Kevin Hart', 'Actors and Actresses', 'American', 'July 6, 1979', '$200 Million', 'Ride Along, Central Intelligence, stand-up comedy'),
            ('Will Smith', 'Actors and Actresses', 'American', 'September 25, 1968', '$350 Million', 'Fresh Prince, Men in Black, Ali'),
            ('Leonardo DiCaprio', 'Actors and Actresses', 'American', 'November 11, 1974', '$300 Million', 'Titanic, The Wolf of Wall Street, Inception'),
            ('Tom Cruise', 'Actors and Actresses', 'American', 'July 3, 1962', '$600 Million', 'Mission Impossible, Top Gun, Jerry Maguire'),
            ('Brad Pitt', 'Actors and Actresses', 'American', 'December 18, 1963', '$400 Million', 'Fight Club, Se7en, Troy'),
            ('Angelina Jolie', 'Actors and Actresses', 'American', 'June 4, 1975', '$120 Million', 'Lara Croft, Maleficent, Girl Interrupted'),
            ('Jennifer Aniston', 'Actors and Actresses', 'American', 'February 11, 1969', '$320 Million', 'Friends, The Morning Show, Marley & Me'),
            ('Johnny Depp', 'Actors and Actresses', 'American', 'June 9, 1963', '$150 Million', 'Pirates of the Caribbean, Edward Scissorhands'),
            ('Robert Downey Jr.', 'Actors and Actresses', 'American', 'April 4, 1965', '$300 Million', 'Iron Man, Avengers, Sherlock Holmes'),
            ('Chris Hemsworth', 'Actors and Actresses', 'Australian', 'August 11, 1983', '$130 Million', 'Thor, Avengers, Extraction'),
            ('Chris Evans', 'Actors and Actresses', 'American', 'June 13, 1981', '$80 Million', 'Captain America, Avengers, Knives Out'),
            ('Scarlett Johansson', 'Actors and Actresses', 'American', 'November 22, 1984', '$165 Million', 'Black Widow, Lost in Translation, Marriage Story'),
            ('Zendaya', 'Actors and Actresses', 'American', 'September 1, 1996', '$20 Million', 'Euphoria, Spider-Man, The Greatest Showman'),
            ('Tom Holland', 'Actors and Actresses', 'British', 'June 1, 1996', '$25 Million', 'Spider-Man MCU trilogy, Avengers, Cherry'),
            ('Ryan Reynolds', 'Actors and Actresses', 'Canadian', 'October 23, 1976', '$350 Million', 'Deadpool, Free Guy, The Proposal'),
            ('Ryan Gosling', 'Actors and Actresses', 'Canadian', 'November 12, 1980', '$70 Million', 'The Notebook, La La Land, Drive, Barbie'),
            ('Sandra Bullock', 'Actors and Actresses', 'American', 'July 26, 1964', '$250 Million', 'Speed, Miss Congeniality, The Blind Side'),
            ('Julia Roberts', 'Actors and Actresses', 'American', 'October 28, 1967', '$250 Million', 'Pretty Woman, Erin Brockovich, Ocean\'s Eleven'),
            ('Jason Statham', 'Actors and Actresses', 'British', 'July 26, 1967', '$90 Million', 'The Transporter, Crank, Fast & Furious'),
            ('Keanu Reeves', 'Actors and Actresses', 'Canadian', 'September 2, 1964', '$380 Million', 'The Matrix, John Wick, Speed'),
            ('Morgan Freeman', 'Actors and Actresses', 'American', 'June 1, 1937', '$250 Million', 'The Shawshank Redemption, Se7en, Million Dollar Baby'),
            ('Gal Gadot', 'Actors and Actresses', 'Israeli', 'April 30, 1985', '$30 Million', 'Wonder Woman, Fast & Furious, Red Notice'),
            ('Anne Hathaway', 'Actors and Actresses', 'American', 'November 12, 1982', '$60 Million', 'The Princess Diaries, The Devil Wears Prada, Les Misérables'),
            ('Margot Robbie', 'Actors and Actresses', 'Australian', 'July 2, 1990', '$26 Million', 'The Wolf of Wall Street, Suicide Squad, Barbie'),
            ('Will Ferrell', 'Actors and Actresses', 'American', 'July 16, 1967', '$160 Million', 'Elf, Anchorman, Step Brothers'),
            ('Vin Diesel', 'Actors and Actresses', 'American', 'July 18, 1967', '$225 Million', 'Fast & Furious franchise, Guardians of the Galaxy'),
            ('Hugh Jackman', 'Actors and Actresses', 'Australian', 'October 12, 1968', '$180 Million', 'Logan, X-Men franchise, The Greatest Showman'),
            ('Emma Watson', 'Actors and Actresses', 'British', 'April 15, 1990', '$85 Million', 'Harry Potter franchise, Beauty and the Beast'),
            ('Nicole Kidman', 'Actors and Actresses', 'Australian-American', 'June 20, 1967', '$250 Million', 'Moulin Rouge, The Hours, Big Little Lies'),

            # Athletes and Sports
            ('Cristiano Ronaldo', 'Athletes and Sports', 'Portuguese', 'February 5, 1985', '$500 Million', 'Five Ballon d\'Or titles, Real Madrid, Al Nassr'),
            ('Lionel Messi', 'Athletes and Sports', 'Argentine', 'June 24, 1987', '$600 Million', 'Eight Ballon d\'Or titles, FC Barcelona, Inter Miami'),
            ('LeBron James', 'Athletes and Sports', 'American', 'December 30, 1984', '$1 Billion', 'Four NBA Championships, Lakers, Heat, Cavaliers'),
            ('Stephen Curry', 'Athletes and Sports', 'American', 'March 14, 1988', '$160 Million', 'Four NBA Championships, Golden State Warriors'),
            ('Serena Williams', 'Athletes and Sports', 'American', 'September 26, 1981', '$250 Million', '23 Grand Slam singles titles'),
            ('Venus Williams', 'Athletes and Sports', 'American', 'June 17, 1980', '$95 Million', 'Seven Grand Slam singles titles, Wimbledon champion'),
            ('Lewis Hamilton', 'Athletes and Sports', 'British', 'January 7, 1985', '$285 Million', 'Seven Formula 1 World Championships'),
            ('Max Verstappen', 'Athletes and Sports', 'Dutch-Belgian', 'September 30, 1997', '$60 Million', 'Four Formula 1 World Championships'),
            ('Kylian Mbappé', 'Athletes and Sports', 'French', 'December 20, 1998', '$150 Million', 'Real Madrid, PSG, France national team'),
            ('Neymar Jr.', 'Athletes and Sports', 'Brazilian', 'February 5, 1992', '$200 Million', 'Barcelona, PSG, Brazil national team'),
            ('David Beckham', 'Athletes and Sports', 'British', 'May 2, 1975', '$450 Million', 'Manchester United, Real Madrid, LA Galaxy'),
            ('Mike Tyson', 'Athletes and Sports', 'American', 'June 30, 1966', '$10 Million', 'Youngest heavyweight champion, Iron Mike'),
            ('Floyd Mayweather Jr.', 'Athletes and Sports', 'American', 'February 24, 1977', '$450 Million', 'Undefeated record 50-0, five-division champion'),
            ('Conor McGregor', 'Athletes and Sports', 'Irish', 'July 14, 1988', '$200 Million', 'UFC Double Champion, Floyd Mayweather bout'),
            ('Rafael Nadal', 'Athletes and Sports', 'Spanish', 'June 3, 1986', '$220 Million', '22 Grand Slam titles, King of Clay'),
            ('Novak Djokovic', 'Athletes and Sports', 'Serbian', 'May 22, 1987', '$220 Million', '24 Grand Slam titles, most weeks at world number one'),
            ('Roger Federer', 'Athletes and Sports', 'Swiss', 'August 8, 1981', '$550 Million', '20 Grand Slam titles, most elegant player'),
            ('Tiger Woods', 'Athletes and Sports', 'American', 'December 30, 1975', '$1.1 Billion', '15 Major championships, transforming golf'),
            ('Usain Bolt', 'Athletes and Sports', 'Jamaican', 'August 21, 1986', '$90 Million', 'World\'s fastest man, 100m and 200m world records'),
            ("Shaquille O'Neal", 'Athletes and Sports', 'American', 'March 6, 1972', '$400 Million', 'Four NBA Championships, dominant center'),

            # Television and Entertainment
            ('Oprah Winfrey', 'Television and Entertainment', 'American', 'January 29, 1954', '$2.5 Billion', 'The Oprah Winfrey Show, OWN Network'),
            ('Ellen DeGeneres', 'Television and Entertainment', 'American', 'January 26, 1958', '$500 Million', 'The Ellen DeGeneres Show, Finding Nemo'),
            ('Kim Kardashian', 'Television and Entertainment', 'American', 'October 21, 1980', '$1.7 Billion', 'Keeping Up with the Kardashians, SKIMS'),
            ('Kylie Jenner', 'Television and Entertainment', 'American', 'August 10, 1997', '$700 Million', 'Kylie Cosmetics, youngest self-made billionaire'),
            ('Kendall Jenner', 'Television and Entertainment', 'American', 'November 3, 1995', '$60 Million', 'Supermodel, Keeping Up with the Kardashians'),
            ('Gordon Ramsay', 'Television and Entertainment', 'British', 'November 8, 1966', '$220 Million', 'Hell\'s Kitchen, MasterChef, Kitchen Nightmares'),
            ('Simon Cowell', 'Television and Entertainment', 'British', 'October 7, 1959', '$600 Million', 'American Idol, The X Factor, Britain\'s Got Talent'),
            ('MrBeast', 'Television and Entertainment', 'American', 'May 7, 1998', '$500 Million', 'YouTube philanthropy, Feastables, MrBeast Burger'),
            ('Jimmy Fallon', 'Television and Entertainment', 'American', 'September 19, 1974', '$60 Million', 'The Tonight Show, Saturday Night Live'),
            ('Trevor Noah', 'Television and Entertainment', 'South African', 'February 20, 1984', '$100 Million', 'The Daily Show, stand-up comedy, Born a Crime'),
            ('Snoop Dogg', 'Television and Entertainment', 'American', 'October 20, 1971', '$160 Million', 'Doggystyle, Drop It Like It\'s Hot'),
            ('Ice Cube', 'Television and Entertainment', 'American', 'June 15, 1969', '$160 Million', 'N.W.A., Friday franchise, Boyz n the Hood'),
            ('50 Cent', 'Television and Entertainment', 'American', 'July 6, 1975', '$40 Million', 'Get Rich or Die Tryin\', In Da Club, Power TV'),
            ('Martha Stewart', 'Television and Entertainment', 'American', 'August 3, 1941', '$400 Million', 'Martha Stewart Living, home and lifestyle brand'),
            ('David Letterman', 'Television and Entertainment', 'American', 'April 12, 1947', '$400 Million', 'Late Night with David Letterman, Late Show'),
            ('Gwyneth Paltrow', 'Television and Entertainment', 'American', 'September 27, 1972', '$200 Million', 'Shakespeare in Love, Iron Man, Goop'),
            ('Steve Harvey', 'Television and Entertainment', 'American', 'January 17, 1957', '$200 Million', 'Family Feud, The Steve Harvey Morning Show'),
            ('Jamie Foxx', 'Television and Entertainment', 'American', 'December 13, 1967', '$170 Million', 'Ray, Django Unchained, Ali'),
            ('Nick Cannon', 'Television and Entertainment', 'American', 'October 8, 1980', '$20 Million', 'Wild \'N Out, America\'s Got Talent, The Masked Singer'),
            ('Paris Hilton', 'Television and Entertainment', 'American', 'February 17, 1981', '$300 Million', 'The Simple Life, heiress, entrepreneur'),

            # WWE Superstars
            ('Roman Reigns', 'WWE Superstars', 'American', 'May 25, 1985', '$12 Million', 'Universal Champion, The Tribal Chief'),
            ('John Cena', 'WWE Superstars', 'American', 'April 23, 1977', '$60 Million', 'You Can\'t See Me, 16-time World Champion'),
            ('Randy Orton', 'WWE Superstars', 'American', 'April 1, 1980', '$11 Million', 'The Viper, RKO, 14-time World Champion'),
            ('Cody Rhodes', 'WWE Superstars', 'American', 'June 30, 1985', '$10 Million', 'WWE Undisputed Champion, The American Nightmare'),
            ('Seth Rollins', 'WWE Superstars', 'American', 'May 28, 1986', '$9 Million', 'The Visionary, World Heavyweight Champion'),
            ('Drew McIntyre', 'WWE Superstars', 'Scottish', 'June 6, 1985', '$5 Million', 'WWE Champion, The Scottish Warrior'),
            ('CM Punk', 'WWE Superstars', 'American', 'October 26, 1978', '$12 Million', 'Pipe Bomb promo, WWE Champion, straight-edge'),
            ('Jey Uso', 'WWE Superstars', 'American', 'August 22, 1985', '$3 Million', 'Yeet!, WWE Tag Team Champion, The Bloodline'),
            ('Jimmy Uso', 'WWE Superstars', 'American', 'August 22, 1985', '$3 Million', 'WWE Tag Team Champion, The Bloodline'),
            ('The Undertaker', 'WWE Superstars', 'American', 'March 24, 1965', '$17 Million', 'The Deadman, WrestleMania streak 21-1'),
            ('Triple H', 'WWE Superstars', 'American', 'July 27, 1969', '$50 Million', 'The Game, 14-time World Champion, D-Generation X'),
            ('Shawn Michaels', 'WWE Superstars', 'American', 'July 22, 1965', '$17 Million', 'Mr. WrestleMania, Heartbreak Kid, Sweet Chin Music'),
            ('Brock Lesnar', 'WWE Superstars', 'American', 'July 12, 1977', '$25 Million', 'The Beast Incarnate, UFC Heavyweight Champion'),
            ('AJ Styles', 'WWE Superstars', 'American', 'June 2, 1977', '$6 Million', 'The Phenomenal One, WWE Champion'),
            ('Rey Mysterio', 'WWE Superstars', 'American', 'December 11, 1974', '$10 Million', 'The Master of the 619, luchador mask'),
            ('Dominik Mysterio', 'WWE Superstars', 'American', 'April 5, 2001', '$2 Million', 'Dirty Dom, NXT North American Champion'),
            ('LA Knight', 'WWE Superstars', 'American', 'October 2, 1983', '$2 Million', 'Yeah!, The Megastar, United States Champion'),
            ('Gunther', 'WWE Superstars', 'Austrian', 'April 1, 1988', '$2 Million', 'Intercontinental Champion record reign, Ring General'),
            ('Damian Priest', 'WWE Superstars', 'American', 'November 25, 1982', '$2 Million', 'World Heavyweight Champion, The Judgment Day'),
            ('Finn Bálor', 'WWE Superstars', 'Irish', 'July 25, 1981', '$3 Million', 'First Universal Champion, The Demon'),
            ('Bianca Belair', 'WWE Superstars', 'American', 'April 9, 1989', '$3 Million', 'The EST of WWE, Raw Women\'s Champion'),
            ('Rhea Ripley', 'WWE Superstars', 'Australian', 'October 8, 1996', '$2 Million', 'Mami, World Women\'s Champion, The Judgment Day'),
            ('Becky Lynch', 'WWE Superstars', 'Irish', 'January 30, 1987', '$6 Million', 'The Man, SmackDown Women\'s Champion'),
            ('Charlotte Flair', 'WWE Superstars', 'American', 'April 5, 1986', '$2 Million', 'The Queen, 14-time Women\'s Champion'),
            ('Liv Morgan', 'WWE Superstars', 'American', 'June 8, 1994', '$2 Million', 'SmackDown Women\'s Champion, Obsession character'),
            ('Bayley', 'WWE Superstars', 'American', 'June 15, 1989', '$2 Million', 'The Role Model, SmackDown Women\'s Champion'),
            ('Alexa Bliss', 'WWE Superstars', 'American', 'August 9, 1991', '$3 Million', 'Five Feet of Fury, Raw Women\'s Champion'),
            ('Iyo Sky', 'WWE Superstars', 'Japanese', 'March 26, 1990', '$1 Million', 'WWE Women\'s Champion, Damage CTRL'),
            ('Asuka', 'WWE Superstars', 'Japanese', 'September 26, 1981', '$2 Million', 'The Empress of Tomorrow, undefeated streak'),
            ('Nia Jax', 'WWE Superstars', 'American', 'May 29, 1984', '$2 Million', 'The Irresistible Force, Raw Women\'s Champion'),
        ]

        for name, category, nationality, born, net_worth, known_for in celebrities_data:
            c = Celebrity(
                name=name,
                category=category,
                nationality=nationality,
                born=born,
                net_worth=net_worth,
                known_for=known_for
            )
            db.session.add(c)

        db.session.commit()
        print(f'Seeded {len(celebrities_data)} celebrities!')
    else:
        print(f'Celebrities already seeded: {Celebrity.query.count()}')
from app import create_app, db
from app.models import Celebrity

app = create_app()

def make_slug(name):
    slug = name.lower()
    replacements = {
        ' ': '-', '.': '', 'é': 'e', 'á': 'a', 'ú': 'u',
        'ó': 'o', 'í': 'i', "'": '', 'ü': 'u', 'ñ': 'n',
        'ã': 'a', 'à': 'a', 'â': 'a', 'ô': 'o', 'è': 'e',
        'ê': 'e', 'î': 'i', 'û': 'u', 'ç': 'c'
    }
    for char, replacement in replacements.items():
        slug = slug.replace(char, replacement)
    return slug

celebrities = [
    ('Calum Scott', 'Musicians and Singers', 'calum-scott'),
    ('Ed Sheeran', 'Musicians and Singers', 'ed-sheeran'),
    ('Taylor Swift', 'Musicians and Singers', 'taylor-swift'),
    ('Justin Bieber', 'Musicians and Singers', 'justin-bieber'),
    ('Adele', 'Musicians and Singers', 'adele'),
    ('Rihanna', 'Musicians and Singers', 'rihanna'),
    ('Beyoncé', 'Musicians and Singers', 'beyonce'),
    ('Drake', 'Musicians and Singers', 'drake'),
    ('Bruno Mars', 'Musicians and Singers', 'bruno-mars'),
    ('The Weeknd', 'Musicians and Singers', 'the-weeknd'),
    ('Shawn Mendes', 'Musicians and Singers', 'shawn-mendes'),
    ('Sam Smith', 'Musicians and Singers', 'sam-smith'),
    ('Lewis Capaldi', 'Musicians and Singers', 'lewis-capaldi'),
    ('Charlie Puth', 'Musicians and Singers', 'charlie-puth'),
    ('Dua Lipa', 'Musicians and Singers', 'dua-lipa'),
    ('Ariana Grande', 'Musicians and Singers', 'ariana-grande'),
    ('Selena Gomez', 'Musicians and Singers', 'selena-gomez'),
    ('Miley Cyrus', 'Musicians and Singers', 'miley-cyrus'),
    ('Lady Gaga', 'Musicians and Singers', 'lady-gaga'),
    ('Katy Perry', 'Musicians and Singers', 'katy-perry'),
    ('Chris Brown', 'Musicians and Singers', 'chris-brown'),
    ('Post Malone', 'Musicians and Singers', 'post-malone'),
    ('Harry Styles', 'Musicians and Singers', 'harry-styles'),
    ('Billie Eilish', 'Musicians and Singers', 'billie-eilish'),
    ('Sia', 'Musicians and Singers', 'sia'),
    ('Celine Dion', 'Musicians and Singers', 'celine-dion'),
    ('Michael Bublé', 'Musicians and Singers', 'michael-buble'),
    ('Elton John', 'Musicians and Singers', 'elton-john'),
    ('Shakira', 'Musicians and Singers', 'shakira'),
    ('Pitbull', 'Musicians and Singers', 'pitbull'),
    ('Dwayne Johnson', 'Actors and Actresses', 'dwayne-johnson'),
    ('Kevin Hart', 'Actors and Actresses', 'kevin-hart'),
    ('Will Smith', 'Actors and Actresses', 'will-smith'),
    ('Leonardo DiCaprio', 'Actors and Actresses', 'leonardo-dicaprio'),
    ('Tom Cruise', 'Actors and Actresses', 'tom-cruise'),
    ('Brad Pitt', 'Actors and Actresses', 'brad-pitt'),
    ('Angelina Jolie', 'Actors and Actresses', 'angelina-jolie'),
    ('Jennifer Aniston', 'Actors and Actresses', 'jennifer-aniston'),
    ('Johnny Depp', 'Actors and Actresses', 'johnny-depp'),
    ('Robert Downey Jr.', 'Actors and Actresses', 'robert-downey-jr'),
    ('Chris Hemsworth', 'Actors and Actresses', 'chris-hemsworth'),
    ('Chris Evans', 'Actors and Actresses', 'chris-evans'),
    ('Scarlett Johansson', 'Actors and Actresses', 'scarlett-johansson'),
    ('Zendaya', 'Actors and Actresses', 'zendaya'),
    ('Tom Holland', 'Actors and Actresses', 'tom-holland'),
    ('Ryan Reynolds', 'Actors and Actresses', 'ryan-reynolds'),
    ('Ryan Gosling', 'Actors and Actresses', 'ryan-gosling'),
    ('Sandra Bullock', 'Actors and Actresses', 'sandra-bullock'),
    ('Julia Roberts', 'Actors and Actresses', 'julia-roberts'),
    ('Jason Statham', 'Actors and Actresses', 'jason-statham'),
    ('Keanu Reeves', 'Actors and Actresses', 'keanu-reeves'),
    ('Morgan Freeman', 'Actors and Actresses', 'morgan-freeman'),
    ('Gal Gadot', 'Actors and Actresses', 'gal-gadot'),
    ('Anne Hathaway', 'Actors and Actresses', 'anne-hathaway'),
    ('Margot Robbie', 'Actors and Actresses', 'margot-robbie'),
    ('Will Ferrell', 'Actors and Actresses', 'will-ferrell'),
    ('Vin Diesel', 'Actors and Actresses', 'vin-diesel'),
    ('Hugh Jackman', 'Actors and Actresses', 'hugh-jackman'),
    ('Emma Watson', 'Actors and Actresses', 'emma-watson'),
    ('Nicole Kidman', 'Actors and Actresses', 'nicole-kidman'),
    ('Cristiano Ronaldo', 'Athletes and Sports', 'cristiano-ronaldo'),
    ('Lionel Messi', 'Athletes and Sports', 'lionel-messi'),
    ('LeBron James', 'Athletes and Sports', 'lebron-james'),
    ('Stephen Curry', 'Athletes and Sports', 'stephen-curry'),
    ('Serena Williams', 'Athletes and Sports', 'serena-williams'),
    ('Venus Williams', 'Athletes and Sports', 'venus-williams'),
    ('Lewis Hamilton', 'Athletes and Sports', 'lewis-hamilton'),
    ('Max Verstappen', 'Athletes and Sports', 'max-verstappen'),
    ('Kylian Mbappé', 'Athletes and Sports', 'kylian-mbappe'),
    ('Neymar Jr.', 'Athletes and Sports', 'neymar-jr'),
    ('David Beckham', 'Athletes and Sports', 'david-beckham'),
    ('Mike Tyson', 'Athletes and Sports', 'mike-tyson'),
    ('Floyd Mayweather Jr.', 'Athletes and Sports', 'floyd-mayweather-jr'),
    ('Conor McGregor', 'Athletes and Sports', 'conor-mcgregor'),
    ('Rafael Nadal', 'Athletes and Sports', 'rafael-nadal'),
    ('Novak Djokovic', 'Athletes and Sports', 'novak-djokovic'),
    ('Roger Federer', 'Athletes and Sports', 'roger-federer'),
    ('Tiger Woods', 'Athletes and Sports', 'tiger-woods'),
    ('Usain Bolt', 'Athletes and Sports', 'usain-bolt'),
    ("Shaquille O'Neal", 'Athletes and Sports', 'shaquille-oneal'),
    ('Oprah Winfrey', 'Television and Entertainment', 'oprah-winfrey'),
    ('Ellen DeGeneres', 'Television and Entertainment', 'ellen-degeneres'),
    ('Kim Kardashian', 'Television and Entertainment', 'kim-kardashian'),
    ('Kylie Jenner', 'Television and Entertainment', 'kylie-jenner'),
    ('Kendall Jenner', 'Television and Entertainment', 'kendall-jenner'),
    ('Gordon Ramsay', 'Television and Entertainment', 'gordon-ramsay'),
    ('Simon Cowell', 'Television and Entertainment', 'simon-cowell'),
    ('MrBeast', 'Television and Entertainment', 'mrbeast'),
    ('Jimmy Fallon', 'Television and Entertainment', 'jimmy-fallon'),
    ('Trevor Noah', 'Television and Entertainment', 'trevor-noah'),
    ('Snoop Dogg', 'Television and Entertainment', 'snoop-dogg'),
    ('Ice Cube', 'Television and Entertainment', 'ice-cube'),
    ('50 Cent', 'Television and Entertainment', '50-cent'),
    ('Martha Stewart', 'Television and Entertainment', 'martha-stewart'),
    ('David Letterman', 'Television and Entertainment', 'david-letterman'),
    ('Gwyneth Paltrow', 'Television and Entertainment', 'gwyneth-paltrow'),
    ('Steve Harvey', 'Television and Entertainment', 'steve-harvey'),
    ('Jamie Foxx', 'Television and Entertainment', 'jamie-foxx'),
    ('Nick Cannon', 'Television and Entertainment', 'nick-cannon'),
    ('Paris Hilton', 'Television and Entertainment', 'paris-hilton'),
    ('Roman Reigns', 'WWE Superstars', 'roman-reigns'),
    ('John Cena', 'WWE Superstars', 'john-cena'),
    ('Randy Orton', 'WWE Superstars', 'randy-orton'),
    ('Cody Rhodes', 'WWE Superstars', 'cody-rhodes'),
    ('Seth Rollins', 'WWE Superstars', 'seth-rollins'),
    ('Drew McIntyre', 'WWE Superstars', 'drew-mcintyre'),
    ('CM Punk', 'WWE Superstars', 'cm-punk'),
    ('Jey Uso', 'WWE Superstars', 'jey-uso'),
    ('Jimmy Uso', 'WWE Superstars', 'jimmy-uso'),
    ('The Undertaker', 'WWE Superstars', 'the-undertaker'),
    ('Triple H', 'WWE Superstars', 'triple-h'),
    ('Shawn Michaels', 'WWE Superstars', 'shawn-michaels'),
    ('Brock Lesnar', 'WWE Superstars', 'brock-lesnar'),
    ('AJ Styles', 'WWE Superstars', 'aj-styles'),
    ('Rey Mysterio', 'WWE Superstars', 'rey-mysterio'),
    ('Dominik Mysterio', 'WWE Superstars', 'dominik-mysterio'),
    ('LA Knight', 'WWE Superstars', 'la-knight'),
    ('Gunther', 'WWE Superstars', 'gunther-wwe'),
    ('Damian Priest', 'WWE Superstars', 'damian-priest'),
    ('Finn Bálor', 'WWE Superstars', 'finn-balor'),
    ('Bianca Belair', 'WWE Superstars', 'bianca-belair'),
    ('Rhea Ripley', 'WWE Superstars', 'rhea-ripley'),
    ('Becky Lynch', 'WWE Superstars', 'becky-lynch'),
    ('Charlotte Flair', 'WWE Superstars', 'charlotte-flair'),
    ('Liv Morgan', 'WWE Superstars', 'liv-morgan'),
    ('Bayley', 'WWE Superstars', 'bayley-wwe'),
    ('Alexa Bliss', 'WWE Superstars', 'alexa-bliss'),
    ('Iyo Sky', 'WWE Superstars', 'iyo-sky'),
    ('Asuka', 'WWE Superstars', 'asuka-wwe'),
    ('Nia Jax', 'WWE Superstars', 'nia-jax'),
]

with app.app_context():
    db.create_all()
    Celebrity = __import__('app.models', fromlist=['Celebrity']).Celebrity
    existing = Celebrity.query.count()
    if existing == 0:
        for name, category, slug in celebrities:
            c = Celebrity(
                name=name,
                category=category,
                image=f'images/celebrities/{slug}.jpg'
            )
            db.session.add(c)
        db.session.commit()
        print(f'Seeded {len(celebrities)} celebrities!')
    else:
        # Update existing with image paths
        for name, category, slug in celebrities:
            c = Celebrity.query.filter_by(name=name).first()
            if c:
                c.image = f'images/celebrities/{slug}.jpg'
        db.session.commit()
        print('Updated celebrity images!')
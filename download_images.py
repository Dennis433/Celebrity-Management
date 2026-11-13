import os
import requests
import time

# Create directory
os.makedirs('app/static/images/celebrities', exist_ok=True)

HEADERS = {
    'User-Agent': 'CelebrityManagementApp/1.0 (educational project; contact@example.com)'
}

celebrities = [
    ('Calum Scott', 'calum-scott'),
    ('Ed Sheeran', 'ed-sheeran'),
    ('Taylor Swift', 'taylor-swift'),
    ('Justin Bieber', 'justin-bieber'),
    ('Adele', 'adele'),
    ('Rihanna', 'rihanna'),
    ('Beyonce', 'beyonce'),
    ('Drake', 'drake'),
    ('Bruno Mars', 'bruno-mars'),
    ('The Weeknd', 'the-weeknd'),
    ('Shawn Mendes', 'shawn-mendes'),
    ('Sam Smith', 'sam-smith'),
    ('Lewis Capaldi', 'lewis-capaldi'),
    ('Charlie Puth', 'charlie-puth'),
    ('Dua Lipa', 'dua-lipa'),
    ('Ariana Grande', 'ariana-grande'),
    ('Selena Gomez', 'selena-gomez'),
    ('Miley Cyrus', 'miley-cyrus'),
    ('Lady Gaga', 'lady-gaga'),
    ('Katy Perry', 'katy-perry'),
    ('Chris Brown', 'chris-brown'),
    ('Post Malone', 'post-malone'),
    ('Harry Styles', 'harry-styles'),
    ('Billie Eilish', 'billie-eilish'),
    ('Sia', 'sia'),
    ('Celine Dion', 'celine-dion'),
    ('Michael Buble', 'michael-buble'),
    ('Elton John', 'elton-john'),
    ('Shakira', 'shakira'),
    ('Pitbull', 'pitbull'),
    ('Dwayne Johnson', 'dwayne-johnson'),
    ('Kevin Hart', 'kevin-hart'),
    ('Will Smith', 'will-smith'),
    ('Leonardo DiCaprio', 'leonardo-dicaprio'),
    ('Tom Cruise', 'tom-cruise'),
    ('Brad Pitt', 'brad-pitt'),
    ('Angelina Jolie', 'angelina-jolie'),
    ('Jennifer Aniston', 'jennifer-aniston'),
    ('Johnny Depp', 'johnny-depp'),
    ('Robert Downey Jr', 'robert-downey-jr'),
    ('Chris Hemsworth', 'chris-hemsworth'),
    ('Chris Evans', 'chris-evans'),
    ('Scarlett Johansson', 'scarlett-johansson'),
    ('Zendaya', 'zendaya'),
    ('Tom Holland', 'tom-holland'),
    ('Ryan Reynolds', 'ryan-reynolds'),
    ('Ryan Gosling', 'ryan-gosling'),
    ('Sandra Bullock', 'sandra-bullock'),
    ('Julia Roberts', 'julia-roberts'),
    ('Jason Statham', 'jason-statham'),
    ('Keanu Reeves', 'keanu-reeves'),
    ('Morgan Freeman', 'morgan-freeman'),
    ('Gal Gadot', 'gal-gadot'),
    ('Anne Hathaway', 'anne-hathaway'),
    ('Margot Robbie', 'margot-robbie'),
    ('Will Ferrell', 'will-ferrell'),
    ('Vin Diesel', 'vin-diesel'),
    ('Hugh Jackman', 'hugh-jackman'),
    ('Emma Watson', 'emma-watson'),
    ('Nicole Kidman', 'nicole-kidman'),
    ('Cristiano Ronaldo', 'cristiano-ronaldo'),
    ('Lionel Messi', 'lionel-messi'),
    ('LeBron James', 'lebron-james'),
    ('Stephen Curry', 'stephen-curry'),
    ('Serena Williams', 'serena-williams'),
    ('Venus Williams', 'venus-williams'),
    ('Lewis Hamilton', 'lewis-hamilton'),
    ('Max Verstappen', 'max-verstappen'),
    ('Kylian Mbappe', 'kylian-mbappe'),
    ('Neymar Jr', 'neymar-jr'),
    ('David Beckham', 'david-beckham'),
    ('Mike Tyson', 'mike-tyson'),
    ('Floyd Mayweather Jr', 'floyd-mayweather-jr'),
    ('Conor McGregor', 'conor-mcgregor'),
    ('Rafael Nadal', 'rafael-nadal'),
    ('Novak Djokovic', 'novak-djokovic'),
    ('Roger Federer', 'roger-federer'),
    ('Tiger Woods', 'tiger-woods'),
    ('Usain Bolt', 'usain-bolt'),
    ('Shaquille ONeal', 'shaquille-oneal'),
    ('Oprah Winfrey', 'oprah-winfrey'),
    ('Ellen DeGeneres', 'ellen-degeneres'),
    ('Kim Kardashian', 'kim-kardashian'),
    ('Kylie Jenner', 'kylie-jenner'),
    ('Kendall Jenner', 'kendall-jenner'),
    ('Gordon Ramsay', 'gordon-ramsay'),
    ('Simon Cowell', 'simon-cowell'),
    ('MrBeast', 'mrbeast'),
    ('Jimmy Fallon', 'jimmy-fallon'),
    ('Trevor Noah', 'trevor-noah'),
    ('Snoop Dogg', 'snoop-dogg'),
    ('Ice Cube', 'ice-cube'),
    ('50 Cent', '50-cent'),
    ('Martha Stewart', 'martha-stewart'),
    ('David Letterman', 'david-letterman'),
    ('Gwyneth Paltrow', 'gwyneth-paltrow'),
    ('Steve Harvey', 'steve-harvey'),
    ('Jamie Foxx', 'jamie-foxx'),
    ('Nick Cannon', 'nick-cannon'),
    ('Paris Hilton', 'paris-hilton'),
    ('Roman Reigns', 'roman-reigns'),
    ('John Cena', 'john-cena'),
    ('Randy Orton', 'randy-orton'),
    ('Cody Rhodes', 'cody-rhodes'),
    ('Seth Rollins', 'seth-rollins'),
    ('Drew McIntyre', 'drew-mcintyre'),
    ('CM Punk', 'cm-punk'),
    ('Jey Uso', 'jey-uso'),
    ('Jimmy Uso', 'jimmy-uso'),
    ('The Undertaker', 'the-undertaker'),
    ('Triple H', 'triple-h'),
    ('Shawn Michaels', 'shawn-michaels'),
    ('Brock Lesnar', 'brock-lesnar'),
    ('AJ Styles', 'aj-styles'),
    ('Rey Mysterio', 'rey-mysterio'),
    ('Dominik Mysterio', 'dominik-mysterio'),
    ('LA Knight', 'la-knight'),
    ('Gunther', 'gunther-wwe'),
    ('Damian Priest', 'damian-priest'),
    ('Finn Balor', 'finn-balor'),
    ('Bianca Belair', 'bianca-belair'),
    ('Rhea Ripley', 'rhea-ripley'),
    ('Becky Lynch', 'becky-lynch'),
    ('Charlotte Flair', 'charlotte-flair'),
    ('Liv Morgan', 'liv-morgan'),
    ('Bayley', 'bayley-wwe'),
    ('Alexa Bliss', 'alexa-bliss'),
    ('Iyo Sky', 'iyo-sky'),
    ('Asuka', 'asuka-wwe'),
    ('Nia Jax', 'nia-jax'),
]

def get_wikipedia_image(name, slug):
    save_path = f'app/static/images/celebrities/{slug}.jpg'
    if os.path.exists(save_path):
        print(f'Already exists: {slug}.jpg')
        return True

    try:
        # Get page image from Wikipedia API
        search_url = 'https://en.wikipedia.org/w/api.php'
        params = {
            'action': 'query',
            'titles': name,
            'prop': 'pageimages',
            'format': 'json',
            'pithumbsize': 400,
        }
        resp = requests.get(search_url, params=params, headers=HEADERS, timeout=10)
        data = resp.json()

        pages = data.get('query', {}).get('pages', {})
        for page_id, page in pages.items():
            thumbnail = page.get('thumbnail', {})
            img_url = thumbnail.get('source', '')
            if img_url:
                img_resp = requests.get(img_url, headers=HEADERS, timeout=10)
                if img_resp.status_code == 200:
                    with open(save_path, 'wb') as f:
                        f.write(img_resp.content)
                    print(f'Downloaded: {slug}.jpg')
                    return True

        print(f'No image found for: {name}')
        return False

    except Exception as e:
        print(f'Error for {name}: {e}')
        return False

if __name__ == '__main__':
    success = 0
    failed = 0
    for name, slug in celebrities:
        result = get_wikipedia_image(name, slug)
        if result:
            success += 1
        else:
            failed += 1
        time.sleep(0.5)  # Be polite to Wikipedia API

    print(f'\nDone! {success} downloaded, {failed} failed.')
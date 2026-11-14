import os
import requests
import time
import cloudinary
import cloudinary.uploader
from app import create_app, db
from app.models import Celebrity
from dotenv import load_dotenv

load_dotenv()

# Configure Cloudinary
cloudinary.config(
    cloud_name=os.environ.get('CLOUDINARY_CLOUD_NAME'),
    api_key=os.environ.get('CLOUDINARY_API_KEY'),
    api_secret=os.environ.get('CLOUDINARY_API_SECRET'),
    secure=True
)

app = create_app()

HEADERS = {
    'User-Agent': 'OfficialCelebrityManagement/1.0 (educational; contact@ocm.com)'
}

# Manual image URLs for celebrities that Wikipedia might miss
MANUAL_IMAGES = {
    'Calum Scott': 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Calum_Scott_2019.jpg/440px-Calum_Scott_2019.jpg',
    'Ed Sheeran': 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Ed_Sheeran_-_Multiply_tour%2C_Rockefeller_Park%2C_NYC_-_2014-07-14_%28cropped%29.jpg/440px-Ed_Sheeran_-_Multiply_tour%2C_Rockefeller_Park%2C_NYC_-_2014-07-14_%28cropped%29.jpg',
    'Taylor Swift': 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/191125_Taylor_Swift_at_the_2019_American_Music_Awards_%28cropped%29.png/440px-191125_Taylor_Swift_at_the_2019_American_Music_Awards_%28cropped%29.png',
    'Justin Bieber': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Justin_Bieber_in_2015.jpg/440px-Justin_Bieber_in_2015.jpg',
    'Adele': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/Adele_at_the_2016_Brit_Awards_%28cropped%29.jpg/440px-Adele_at_the_2016_Brit_Awards_%28cropped%29.jpg',
    'Rihanna': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Rihanna_Fenty_2018.jpg/440px-Rihanna_Fenty_2018.jpg',
    'Beyoncé': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/17/Beyonc%C3%A9_at_The_Lion_King_European_Premiere_2019.png/440px-Beyonc%C3%A9_at_The_Lion_King_European_Premiere_2019.png',
    'Drake': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/Drake_July_2016.jpg/440px-Drake_July_2016.jpg',
    'Bruno Mars': 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/95/Bruno_Mars_Net_Worth.jpg/440px-Bruno_Mars_Net_Worth.jpg',
    'The Weeknd': 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/The_Weeknd_in_2020.png/440px-The_Weeknd_in_2020.png',
    'Shawn Mendes': 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Shawn_Mendes_2019_by_Glenn_Francis.jpg/440px-Shawn_Mendes_2019_by_Glenn_Francis.jpg',
    'Sam Smith': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/13/Sam_Smith_2018.jpg/440px-Sam_Smith_2018.jpg',
    'Lewis Capaldi': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/Lewis_Capaldi_2019_%28cropped%29.jpg/440px-Lewis_Capaldi_2019_%28cropped%29.jpg',
    'Charlie Puth': 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/7c/Charlie_Puth_2016.jpg/440px-Charlie_Puth_2016.jpg',
    'Dua Lipa': 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f4/Dua_Lipa_2021_%28cropped%29.jpg/440px-Dua_Lipa_2021_%28cropped%29.jpg',
    'Ariana Grande': 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b1/Ariana_Grande_2019_by_Glenn_Francis.jpg/440px-Ariana_Grande_2019_by_Glenn_Francis.jpg',
    'Selena Gomez': 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/7a/Selena_Gomez_in_2019.jpg/440px-Selena_Gomez_in_2019.jpg',
    'Miley Cyrus': 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f9/Miley_Cyrus_2019.jpg/440px-Miley_Cyrus_2019.jpg',
    'Lady Gaga': 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f9/Lady_Gaga_2016_%28cropped%29.jpg/440px-Lady_Gaga_2016_%28cropped%29.jpg',
    'Katy Perry': 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Katy_Perry_2017.jpg/440px-Katy_Perry_2017.jpg',
    'Chris Brown': 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/6e/Chris_Brown_2019.jpg/440px-Chris_Brown_2019.jpg',
    'Post Malone': 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f5/Post_Malone_2018_%28cropped%29.jpg/440px-Post_Malone_2018_%28cropped%29.jpg',
    'Harry Styles': 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Harry_Styles_2017.jpg/440px-Harry_Styles_2017.jpg',
    'Billie Eilish': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Billie_Eilish_2019_by_Glenn_Francis_%28cropped%29.jpg/440px-Billie_Eilish_2019_by_Glenn_Francis_%28cropped%29.jpg',
    'Sia': 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Sia_%28musician%29_2016.jpg/440px-Sia_%28musician%29_2016.jpg',
    'Celine Dion': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/55/C%C3%A9line_Dion_in_2019.jpg/440px-C%C3%A9line_Dion_in_2019.jpg',
    'Michael Bublé': 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/27/Michael_Bubl%C3%A9_2018.jpg/440px-Michael_Bubl%C3%A9_2018.jpg',
    'Elton John': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/55/Elton_John_2015.jpg/440px-Elton_John_2015.jpg',
    'Shakira': 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b9/Shakira_-_2010.jpg/440px-Shakira_-_2010.jpg',
    'Pitbull': 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Pitbull_2012_%28cropped%29.jpg/440px-Pitbull_2012_%28cropped%29.jpg',
    'Dwayne Johnson': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1f/Dwayne_Johnson_2014_%28cropped%29.jpg/440px-Dwayne_Johnson_2014_%28cropped%29.jpg',
    'Kevin Hart': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Kevin_Hart_2019_by_Glenn_Francis.jpg/440px-Kevin_Hart_2019_by_Glenn_Francis.jpg',
    'Will Smith': 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Will_Smith_2019_by_Glenn_Francis.jpg/440px-Will_Smith_2019_by_Glenn_Francis.jpg',
    'Leonardo DiCaprio': 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Leonardo_Dicaprio_Cannes_2019.jpg/440px-Leonardo_Dicaprio_Cannes_2019.jpg',
    'Tom Cruise': 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/33/Tom_Cruise_by_Gage_Skidmore_2.jpg/440px-Tom_Cruise_by_Gage_Skidmore_2.jpg',
    'Brad Pitt': 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Brad_Pitt_2019_by_Glenn_Francis.jpg/440px-Brad_Pitt_2019_by_Glenn_Francis.jpg',
    'Angelina Jolie': 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/ad/Angelina_Jolie_2_June_2014_%28cropped%29.jpg/440px-Angelina_Jolie_2_June_2014_%28cropped%29.jpg',
    'Jennifer Aniston': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Jennifer_Aniston_2019_by_Glenn_Francis.jpg/440px-Jennifer_Aniston_2019_by_Glenn_Francis.jpg',
    'Johnny Depp': 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Johnny_Depp_at_the_2012_Venice_Film_Festival.jpg/440px-Johnny_Depp_at_the_2012_Venice_Film_Festival.jpg',
    'Robert Downey Jr.': 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/94/Robert_Downey_Jr_2014_Comic_Con_%28cropped%29.jpg/440px-Robert_Downey_Jr_2014_Comic_Con_%28cropped%29.jpg',
    'Chris Hemsworth': 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e8/Chris_Hemsworth_by_Gage_Skidmore_2.jpg/440px-Chris_Hemsworth_by_Gage_Skidmore_2.jpg',
    'Chris Evans': 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Chris_Evans_2019_by_Glenn_Francis.jpg/440px-Chris_Evans_2019_by_Glenn_Francis.jpg',
    'Scarlett Johansson': 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/60/Scarlett_Johansson_2010.jpg/440px-Scarlett_Johansson_2010.jpg',
    'Zendaya': 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f9/Zendaya_2019_by_Glenn_Francis_%28cropped%29.jpg/440px-Zendaya_2019_by_Glenn_Francis_%28cropped%29.jpg',
    'Tom Holland': 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Tom_Holland_by_Gage_Skidmore.jpg/440px-Tom_Holland_by_Gage_Skidmore.jpg',
    'Ryan Reynolds': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/Ryan_Reynolds_2016.jpg/440px-Ryan_Reynolds_2016.jpg',
    'Ryan Gosling': 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/Ryan_Gosling_2018_%28cropped%29.jpg/440px-Ryan_Gosling_2018_%28cropped%29.jpg',
    'Sandra Bullock': 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/9d/Sandra_Bullock_2010.jpg/440px-Sandra_Bullock_2010.jpg',
    'Julia Roberts': 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/fd/Julia_Roberts_2018_by_Glenn_Francis.jpg/440px-Julia_Roberts_2018_by_Glenn_Francis.jpg',
    'Jason Statham': 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Jason_Statham_2015.jpg/440px-Jason_Statham_2015.jpg',
    'Keanu Reeves': 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/27/Keanu_Reeves_cropped.jpg/440px-Keanu_Reeves_cropped.jpg',
    'Morgan Freeman': 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f5/Morgan_Freeman_2018.jpg/440px-Morgan_Freeman_2018.jpg',
    'Gal Gadot': 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Gal_Gadot_%22Wonder_Woman%22_at_the_San_Diego_Comic-Con_%28cropped%29.jpg/440px-Gal_Gadot_%22Wonder_Woman%22_at_the_San_Diego_Comic-Con_%28cropped%29.jpg',
    'Anne Hathaway': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/51/Anne_Hathaway_2019_by_Glenn_Francis.jpg/440px-Anne_Hathaway_2019_by_Glenn_Francis.jpg',
    'Margot Robbie': 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/40/Margot_Robbie_2019.jpg/440px-Margot_Robbie_2019.jpg',
    'Will Ferrell': 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/fd/Will_Ferrell_2012.jpg/440px-Will_Ferrell_2012.jpg',
    'Vin Diesel': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/Vin_Diesel_2019_by_Glenn_Francis.jpg/440px-Vin_Diesel_2019_by_Glenn_Francis.jpg',
    'Hugh Jackman': 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/fd/Hugh_Jackman_2013.jpg/440px-Hugh_Jackman_2013.jpg',
    'Emma Watson': 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/7f/Emma_Watson_2013.jpg/440px-Emma_Watson_2013.jpg',
    'Nicole Kidman': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/13/Nicole_Kidman_Cannes_2017.jpg/440px-Nicole_Kidman_Cannes_2017.jpg',
    'Cristiano Ronaldo': 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Cristiano_Ronaldo_2018.jpg/440px-Cristiano_Ronaldo_2018.jpg',
    'Lionel Messi': 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b8/Messi_vs_Nigeria_2018.jpg/440px-Messi_vs_Nigeria_2018.jpg',
    'LeBron James': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/LeBron_James_crop1.jpg/440px-LeBron_James_crop1.jpg',
    'Stephen Curry': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Stephen_Curry_2015_%28cropped%29.jpg/440px-Stephen_Curry_2015_%28cropped%29.jpg',
    'Serena Williams': 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f7/Serena_Williams_2017_Australian_Open.jpg/440px-Serena_Williams_2017_Australian_Open.jpg',
    'Venus Williams': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Venus_Williams_2013_Wimbledon.jpg/440px-Venus_Williams_2013_Wimbledon.jpg',
    'Lewis Hamilton': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/18/Lewis_Hamilton_2016_Malaysia_2.jpg/440px-Lewis_Hamilton_2016_Malaysia_2.jpg',
    'Max Verstappen': 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/71/Max_Verstappen_in_2022.jpg/440px-Max_Verstappen_in_2022.jpg',
    'Kylian Mbappé': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/57/2019-07-17_SG_Dynamo_Dresden_v_Paris_Saint-Germain_F.C._by_Sandro_Halank%E2%80%93191_%28cropped%29.jpg/440px-2019-07-17_SG_Dynamo_Dresden_v_Paris_Saint-Germain_F.C._by_Sandro_Halank%E2%80%93191_%28cropped%29.jpg',
    'Neymar Jr.': 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/Brasile_Coreia_do_Sul_20130602_01.jpg/440px-Brasile_Coreia_do_Sul_20130602_01.jpg',
    'David Beckham': 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/2e/David_Beckham_2019.jpg/440px-David_Beckham_2019.jpg',
    'Mike Tyson': 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Mike_Tyson_2019_by_Glenn_Francis.jpg/440px-Mike_Tyson_2019_by_Glenn_Francis.jpg',
    'Floyd Mayweather Jr.': 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/95/Floyd_Mayweather_Jr._%28cropped%29.jpg/440px-Floyd_Mayweather_Jr._%28cropped%29.jpg',
    'Conor McGregor': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1f/Conor_McGregor_2019_%28cropped%29.jpg/440px-Conor_McGregor_2019_%28cropped%29.jpg',
    'Rafael Nadal': 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f9/Rafael_Nadal_2015_Roland_Garros.jpg/440px-Rafael_Nadal_2015_Roland_Garros.jpg',
    'Novak Djokovic': 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Novak_Djokovic_2019_Wimbledon_%28cropped%29.jpg/440px-Novak_Djokovic_2019_Wimbledon_%28cropped%29.jpg',
    'Roger Federer': 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/40/Roger_Federer_2017_Australian_Open.jpg/440px-Roger_Federer_2017_Australian_Open.jpg',
    'Tiger Woods': 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/9b/Tiger_Woods_2016.jpg/440px-Tiger_Woods_2016.jpg',
    'Usain Bolt': 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/Usain_Bolt_2012.jpg/440px-Usain_Bolt_2012.jpg',
    "Shaquille O'Neal": 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f9/Shaquille_O%27Neal_2016.jpg/440px-Shaquille_O%27Neal_2016.jpg',
    'Oprah Winfrey': 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/Oprah_in_2014.jpg/440px-Oprah_in_2014.jpg',
    'Ellen DeGeneres': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/Ellen_DeGeneres_2011.jpg/440px-Ellen_DeGeneres_2011.jpg',
    'Kim Kardashian': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/55/Kim_Kardashian_2019_by_Glenn_Francis.jpg/440px-Kim_Kardashian_2019_by_Glenn_Francis.jpg',
    'Kylie Jenner': 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f4/Kylie_Jenner_2019_by_Glenn_Francis.jpg/440px-Kylie_Jenner_2019_by_Glenn_Francis.jpg',
    'Kendall Jenner': 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/9d/Kendall_Jenner_2019_by_Glenn_Francis.jpg/440px-Kendall_Jenner_2019_by_Glenn_Francis.jpg',
    'Gordon Ramsay': 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/fb/Gordon_Ramsay.jpg/440px-Gordon_Ramsay.jpg',
    'Simon Cowell': 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/70/Simon_Cowell_2017.jpg/440px-Simon_Cowell_2017.jpg',
    'MrBeast': 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Jimmy_Donaldson_%28MrBeast%29.jpg/440px-Jimmy_Donaldson_%28MrBeast%29.jpg',
    'Jimmy Fallon': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/Jimmy_Fallon_2016.jpg/440px-Jimmy_Fallon_2016.jpg',
    'Trevor Noah': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/Trevor_Noah_2019_by_Glenn_Francis.jpg/440px-Trevor_Noah_2019_by_Glenn_Francis.jpg',
    'Snoop Dogg': 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Snoop_Dogg_2019_by_Glenn_Francis.jpg/440px-Snoop_Dogg_2019_by_Glenn_Francis.jpg',
    'Ice Cube': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Ice_Cube_2010.jpg/440px-Ice_Cube_2010.jpg',
    '50 Cent': 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f9/50_Cent_2012.jpg/440px-50_Cent_2012.jpg',
    'Martha Stewart': 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f5/Martha_Stewart_2011.jpg/440px-Martha_Stewart_2011.jpg',
    'David Letterman': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/David_Letterman_2016.jpg/440px-David_Letterman_2016.jpg',
    'Gwyneth Paltrow': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Gwyneth_Paltrow_2019.jpg/440px-Gwyneth_Paltrow_2019.jpg',
    'Steve Harvey': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/Steve_Harvey_2012.jpg/440px-Steve_Harvey_2012.jpg',
    'Jamie Foxx': 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f9/Jamie_Foxx_2019_by_Glenn_Francis.jpg/440px-Jamie_Foxx_2019_by_Glenn_Francis.jpg',
    'Nick Cannon': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Nick_Cannon_2019.jpg/440px-Nick_Cannon_2019.jpg',
    'Paris Hilton': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/Paris_Hilton_2018.jpg/440px-Paris_Hilton_2018.jpg',
    'Roman Reigns': 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f5/Roman_Reigns_2019.jpg/440px-Roman_Reigns_2019.jpg',
    'John Cena': 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/9b/John_Cena_2016.jpg/440px-John_Cena_2016.jpg',
    'Randy Orton': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/Randy_Orton_2016.jpg/440px-Randy_Orton_2016.jpg',
    'Cody Rhodes': 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f9/Cody_Rhodes_2022.jpg/440px-Cody_Rhodes_2022.jpg',
    'Seth Rollins': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/Seth_Rollins_2019.jpg/440px-Seth_Rollins_2019.jpg',
    'Drew McIntyre': 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f5/Drew_McIntyre_2019.jpg/440px-Drew_McIntyre_2019.jpg',
    'CM Punk': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/CM_Punk_2012.jpg/440px-CM_Punk_2012.jpg',
    'The Undertaker': 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f9/Undertaker_2013.jpg/440px-Undertaker_2013.jpg',
    'Triple H': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/Triple_H_2019.jpg/440px-Triple_H_2019.jpg',
    'Shawn Michaels': 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f5/Shawn_Michaels_2010.jpg/440px-Shawn_Michaels_2010.jpg',
    'Brock Lesnar': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/Brock_Lesnar_2019.jpg/440px-Brock_Lesnar_2019.jpg',
    'AJ Styles': 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f9/AJ_Styles_2016.jpg/440px-AJ_Styles_2016.jpg',
    'Rey Mysterio': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/Rey_Mysterio_2019.jpg/440px-Rey_Mysterio_2019.jpg',
    'Becky Lynch': 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f9/Becky_Lynch_2019.jpg/440px-Becky_Lynch_2019.jpg',
    'Charlotte Flair': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/Charlotte_Flair_2019.jpg/440px-Charlotte_Flair_2019.jpg',
    'Rhea Ripley': 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f5/Rhea_Ripley_2022.jpg/440px-Rhea_Ripley_2022.jpg',
    'Bianca Belair': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/Bianca_Belair_2021.jpg/440px-Bianca_Belair_2021.jpg',
}

def get_wikipedia_image(name):
    """Try to get image URL from Wikipedia API"""
    try:
        url = 'https://en.wikipedia.org/w/api.php'
        params = {
            'action': 'query',
            'titles': name,
            'prop': 'pageimages',
            'format': 'json',
            'pithumbsize': 500,
        }
        resp = requests.get(url, params=params, headers=HEADERS, timeout=10)
        data = resp.json()
        pages = data.get('query', {}).get('pages', {})
        for page_id, page in pages.items():
            thumbnail = page.get('thumbnail', {})
            img_url = thumbnail.get('source', '')
            if img_url:
                return img_url
    except Exception as e:
        print(f'  Wikipedia error for {name}: {e}')
    return None

def upload_url_to_cloudinary(image_url, name):
    """Upload image URL directly to Cloudinary"""
    try:
        slug = name.lower().replace(' ', '-').replace('.', '').replace("'", '').replace('é', 'e').replace('á', 'a').replace('ú', 'u')
        result = cloudinary.uploader.upload(
            image_url,
            public_id=f'ocm/celebrities/{slug}',
            overwrite=True,
            transformation=[
                {'width': 400, 'height': 400, 'crop': 'fill', 'gravity': 'face'},
                {'quality': 'auto', 'fetch_format': 'auto'}
            ]
        )
        return result.get('secure_url')
    except Exception as e:
        print(f'  Cloudinary upload error for {name}: {e}')
        return None

def upload_local_to_cloudinary(local_path, name):
    """Upload local file to Cloudinary"""
    try:
        slug = name.lower().replace(' ', '-').replace('.', '').replace("'", '').replace('é', 'e')
        result = cloudinary.uploader.upload(
            local_path,
            public_id=f'ocm/celebrities/{slug}',
            overwrite=True,
            transformation=[
                {'width': 400, 'height': 400, 'crop': 'fill', 'gravity': 'face'},
                {'quality': 'auto', 'fetch_format': 'auto'}
            ]
        )
        return result.get('secure_url')
    except Exception as e:
        print(f'  Cloudinary local upload error for {name}: {e}')
        return None

with app.app_context():
    celebrities = Celebrity.query.all()
    total = len(celebrities)
    success = 0
    failed = []

    print(f'\n🚀 Processing {total} celebrities...\n')

    for i, celeb in enumerate(celebrities, 1):
        print(f'[{i}/{total}] {celeb.name}', end=' ')

        # Skip if already has a Cloudinary URL
        if celeb.image and celeb.image.startswith('https://res.cloudinary.com'):
            print('✅ Already on Cloudinary')
            success += 1
            continue

        cloudinary_url = None

        # Step 1: Check if has local file
        if celeb.image and not celeb.image.startswith('http'):
            local_path = os.path.join('app', 'static', celeb.image)
            if os.path.exists(local_path):
                print('📁 Local file found, uploading to Cloudinary...', end=' ')
                cloudinary_url = upload_local_to_cloudinary(local_path, celeb.name)

        # Step 2: Try manual image URL
        if not cloudinary_url and celeb.name in MANUAL_IMAGES:
            print('🔗 Using manual URL...', end=' ')
            cloudinary_url = upload_url_to_cloudinary(MANUAL_IMAGES[celeb.name], celeb.name)

        # Step 3: Try Wikipedia API
        if not cloudinary_url:
            print('🌐 Trying Wikipedia...', end=' ')
            wiki_url = get_wikipedia_image(celeb.name)
            if wiki_url:
                cloudinary_url = upload_url_to_cloudinary(wiki_url, celeb.name)

        # Step 4: Try Wikipedia with alternate name
        if not cloudinary_url:
            alt_name = celeb.name.replace('Jr.', '').replace('Sr.', '').strip()
            if alt_name != celeb.name:
                wiki_url = get_wikipedia_image(alt_name)
                if wiki_url:
                    cloudinary_url = upload_url_to_cloudinary(wiki_url, celeb.name)

        if cloudinary_url:
            celeb.image = cloudinary_url
            db.session.commit()
            print(f'✅ Done')
            success += 1
        else:
            print(f'❌ Failed')
            failed.append(celeb.name)

        time.sleep(0.3)

    print(f'\n{"="*50}')
    print(f'✅ Successfully processed: {success}/{total}')

    if failed:
        print(f'\n❌ Failed ({len(failed)}):')
        for name in failed:
            print(f'  - {name}')
        print('\nFor failed celebrities, upload manually via:')
        print('http://127.0.0.1:5000/admin/celebrities')
    else:
        print('\n🎉 ALL celebrities have images!')
from app import create_app, db
from app.models import Celebrity

app = create_app()

data = {
    'Calum Scott': {
        'nationality': 'British',
        'born': 'October 12, 1988',
        'net_worth': '$4 Million',
        'known_for': 'Dancing On My Own, You Are The Reason',
        'bio': 'Calum Scott is a British singer and songwriter who rose to fame after appearing on Britain\'s Got Talent in 2015. His emotional cover of Robyn\'s Dancing On My Own became a worldwide hit, reaching number two on the UK Singles Chart.\n\nBorn in Hull, England, Calum developed his passion for music at a young age. After his Britain\'s Got Talent appearance, he signed with Capitol Records and released his debut album Only Human in 2018.\n\nKnown for his powerful falsetto voice and deeply emotional performances, Calum has toured the world and collaborated with artists across the globe. His single You Are The Reason became an international anthem of love and devotion.'
    },
    'Ed Sheeran': {
        'nationality': 'British',
        'born': 'February 17, 1991',
        'net_worth': '$200 Million',
        'known_for': 'Shape of You, Perfect, Thinking Out Loud',
        'bio': 'Ed Sheeran is one of the best-selling music artists of all time, with over 150 million records sold worldwide. Born in Halifax, West Yorkshire, England, he began playing guitar at age eleven and started performing at local venues as a teenager.\n\nHe moved to London at seventeen to pursue his music career, busking on the streets before being discovered. His debut album Plus (+) was released in 2011 and reached number one in the UK. He followed it with Multiply (x), Divide (÷) and Equals (=), each breaking records worldwide.\n\nEd has won multiple Grammy Awards, Brit Awards and Ivor Novello Awards. Known for his unique ability to blend pop, folk, hip hop and soul, he is considered one of the most versatile artists of his generation.'
    },
    'Taylor Swift': {
        'nationality': 'American',
        'born': 'December 13, 1989',
        'net_worth': '$1.1 Billion',
        'known_for': 'Shake It Off, Blank Space, Anti-Hero, Love Story',
        'bio': 'Taylor Swift is an American singer-songwriter and one of the most successful musicians in history. Born in West Reading, Pennsylvania, she moved to Nashville at fourteen to pursue a country music career.\n\nShe signed with Big Machine Records and released her self-titled debut album in 2006. Her second album Fearless won the Grammy Award for Album of the Year, making her the youngest artist to win that honor.\n\nOver the course of her career, Taylor has reinvented herself across multiple genres including country, pop and indie folk. Her Eras Tour became the highest-grossing concert tour of all time. She is also the first artist to have four albums debut at number one in the same year.'
    },
    'Justin Bieber': {
        'nationality': 'Canadian',
        'born': 'March 1, 1994',
        'net_worth': '$300 Million',
        'known_for': 'Baby, Sorry, Love Yourself, Peaches',
        'bio': 'Justin Bieber is a Canadian singer who was discovered at the age of thirteen by talent manager Scooter Braun after posting YouTube videos of himself singing. He was subsequently introduced to R&B artist Usher and signed to RBMG Records.\n\nBorn in London, Ontario, Canada, Justin released his debut EP My World in 2009, becoming the first artist to have seven songs from a debut record chart on the Billboard Hot 100. He went on to become one of the best-selling music artists of all time.\n\nDespite personal challenges throughout his career, Justin has maintained a massive global fanbase known as Beliebers. His album Justice released in 2021 debuted at number one in multiple countries.'
    },
    'Adele': {
        'nationality': 'British',
        'born': 'May 5, 1988',
        'net_worth': '$220 Million',
        'known_for': 'Hello, Rolling in the Deep, Someone Like You',
        'bio': 'Adele Laurie Blue Adkins, known professionally as Adele, is an English singer and songwriter. Born in Tottenham, London, she attended the BRIT School for Performing Arts and Technology where she honed her vocal talents.\n\nShe was discovered by XL Recordings after a friend posted her demo on Myspace. Her debut album 19, released in 2008, established her as a major artist. Her second album 21 became one of the best-selling albums of all time, winning six Grammy Awards.\n\nAdele is known for her powerful mezzo-soprano voice and deeply personal songwriting. Her album 25 broke the record for first-week album sales in both the US and UK. She returned with the critically acclaimed 30 in 2021.'
    },
    'Rihanna': {
        'nationality': 'Barbadian',
        'born': 'February 20, 1988',
        'net_worth': '$1.4 Billion',
        'known_for': 'Umbrella, Diamonds, We Found Love, Work',
        'bio': 'Robyn Rihanna Fenty, known professionally as Rihanna, is a Barbadian singer, actress and businesswoman. Born in Saint Michael, Barbados, she was discovered at age fifteen by American record producer Evan Rogers.\n\nShe signed with Def Jam Recordings in 2005 and released her debut album Music of the Sun. Her career skyrocketed with the release of Good Girl Gone Bad in 2007, featuring the global hit Umbrella.\n\nBeyond music, Rihanna has built a business empire. Her Fenty Beauty cosmetics line, launched in 2017, was valued at over one billion dollars within its first year. Her Savage X Fenty lingerie brand has also achieved massive commercial success, making her one of the wealthiest entertainers in the world.'
    },
    'Beyoncé': {
        'nationality': 'American',
        'born': 'September 4, 1981',
        'net_worth': '$500 Million',
        'known_for': 'Crazy in Love, Halo, Lemonade, Single Ladies',
        'bio': 'Beyoncé Giselle Knowles-Carter is an American singer, songwriter, actress and businesswoman. Born in Houston, Texas, she began performing in singing and dancing competitions as a child.\n\nShe rose to fame in the late 1990s as the lead singer of R&B girl group Destiny\'s Child, one of the best-selling girl groups of all time. Her solo debut album Dangerously in Love in 2003 established her as one of the premier artists of her generation.\n\nBeyoncé has won 32 Grammy Awards, the most of any artist in history. Known for her powerful voice, electrifying stage presence and boundary-pushing artistry, she is widely regarded as one of the greatest performers of all time. Her visual album Lemonade is considered one of the most important cultural works of the 21st century.'
    },
    'Drake': {
        'nationality': 'Canadian',
        'born': 'October 24, 1986',
        'net_worth': '$250 Million',
        'known_for': 'God\'s Plan, Hotline Bling, One Dance, Started From the Bottom',
        'bio': 'Aubrey Drake Graham, known professionally as Drake, is a Canadian rapper, singer, songwriter and actor. Born in Toronto, Ontario, he first gained recognition as an actor on the teen drama Degrassi: The Next Generation.\n\nHe launched his music career with the mixtape Room for Improvement in 2006 and quickly gained attention in the hip hop community. After signing with Young Money Entertainment, he released his debut studio album Thank Me Later in 2010.\n\nDrake has broken numerous records throughout his career, including the most Billboard Hot 100 entries of any artist in history. He has won four Grammy Awards and multiple Billboard Music Awards. His influence on the blend of rap and R&B has shaped the sound of modern popular music.'
    },
    'Bruno Mars': {
        'nationality': 'American',
        'born': 'October 8, 1985',
        'net_worth': '$175 Million',
        'known_for': 'Just the Way You Are, Uptown Funk, That\'s What I Like',
        'bio': 'Peter Gene Hernandez, known professionally as Bruno Mars, is an American singer, songwriter, record producer and dancer. Born in Honolulu, Hawaii, he grew up performing in a family band and developed an early love for music.\n\nHe moved to Los Angeles after high school to pursue a music career. After initial struggles, he broke through as a co-writer of several hit songs before launching his own career. His debut album Doo-Wops and Hooligans produced the hits Just the Way You Are and Grenade.\n\nBruno is known for his incredible versatility, effortlessly blending pop, funk, R&B, reggae and soul. His live performances are legendary for their energy and precision. He has won 15 Grammy Awards and sold over 130 million records worldwide.'
    },
    'The Weeknd': {
        'nationality': 'Canadian',
        'born': 'February 16, 1990',
        'net_worth': '$300 Million',
        'known_for': 'Blinding Lights, Starboy, Can\'t Feel My Face',
        'bio': 'Abel Makkonen Tesfaye, known professionally as The Weeknd, is a Canadian singer, songwriter and record producer. Born in Toronto to Ethiopian immigrant parents, he dropped out of high school at seventeen to pursue music.\n\nHe began his career by anonymously uploading songs to YouTube in 2010, quickly building a cult following with his dark, atmospheric R&B sound. His mixtape trilogy Trilogy was critically acclaimed and led to a deal with Republic Records.\n\nThe Weeknd has become one of the most streamed artists of all time. His album After Hours and its single Blinding Lights broke numerous streaming records. He delivered a critically praised Super Bowl halftime performance in 2021 and has expanded his brand into acting and philanthropy.'
    },
    'Dwayne Johnson': {
        'nationality': 'American',
        'born': 'May 2, 1972',
        'net_worth': '$800 Million',
        'known_for': 'The Rock, Fast & Furious franchise, Jumanji',
        'bio': 'Dwayne Douglas Johnson, also known by his ring name The Rock, is an American actor, businessman and former professional wrestler. Born in Hayward, California, he comes from a wrestling family — his father and grandfather were both professional wrestlers.\n\nAfter a brief career in Canadian football, he joined the WWF in 1996 and became one of the most popular and electrifying performers in wrestling history. He transitioned to acting in 2001 with The Mummy Returns and quickly became one of Hollywood\'s most bankable stars.\n\nDwayne has starred in some of the highest-grossing films of all time, including the Fast & Furious franchise, Jumanji and Black Adam. He is consistently ranked as one of the highest-paid actors in the world and was named Time magazine\'s 100 most influential people multiple times.'
    },
    'Cristiano Ronaldo': {
        'nationality': 'Portuguese',
        'born': 'February 5, 1985',
        'net_worth': '$500 Million',
        'known_for': 'Five Ballon d\'Or titles, Manchester United, Real Madrid, Juventus',
        'bio': 'Cristiano Ronaldo dos Santos Aveiro is a Portuguese professional footballer widely regarded as one of the greatest players of all time. Born in Funchal, Madeira, he joined the Sporting CP academy at age twelve after showing exceptional talent.\n\nManchester United signed him in 2003 at age eighteen. He went on to win three consecutive Premier League titles and the UEFA Champions League before joining Real Madrid for a then world record fee in 2009.\n\nAt Real Madrid, Ronaldo became the all-time leading scorer for the club and won four Champions League titles. He has won five Ballon d\'Or awards and holds the record for the most international goals in football history. Known for his extraordinary athleticism, goal-scoring ability and dedication to fitness, he is considered one of the sport\'s all-time greats.'
    },
    'Lionel Messi': {
        'nationality': 'Argentine',
        'born': 'June 24, 1987',
        'net_worth': '$600 Million',
        'known_for': 'Eight Ballon d\'Or titles, FC Barcelona, 2022 World Cup winner',
        'bio': 'Lionel Andrés Messi is an Argentine professional footballer widely considered the greatest player of all time. Born in Rosario, Argentina, he was diagnosed with a growth hormone deficiency at age ten. FC Barcelona agreed to pay for his treatment in exchange for joining their famous La Masia academy.\n\nMessi spent over twenty years at Barcelona, becoming their all-time leading scorer and winning ten La Liga titles, four UEFA Champions League titles and eight Ballon d\'Or awards — the most in history.\n\nIn 2021 he moved to Paris Saint-Germain and later Inter Miami in MLS. His greatest achievement came in 2022 when he led Argentina to the FIFA World Cup title in Qatar, fulfilling his lifelong dream and cementing his legacy as the undisputed greatest footballer of all time.'
    },
    'LeBron James': {
        'nationality': 'American',
        'born': 'December 30, 1984',
        'net_worth': '$1 Billion',
        'known_for': 'Four NBA Championships, Lakers, Heat, Cavaliers',
        'bio': 'LeBron Raymone James Sr. is an American professional basketball player for the Los Angeles Lakers in the NBA. Born in Akron, Ohio, he was a highly touted prospect from a young age and was selected first overall in the 2003 NBA Draft.\n\nKnown as King James, he has won four NBA championships with three different teams, four MVP awards and four Finals MVP awards. He surpassed Kareem Abdul-Jabbar\'s all-time NBA scoring record in 2023.\n\nBeyond basketball, LeBron is a successful businessman and philanthropist. He co-founded the production company SpringHill Entertainment and owns a stake in Fenway Sports Group. His I Promise School in Akron provides education and support to at-risk youth. He is widely considered one of the greatest athletes in history.'
    },
    'Oprah Winfrey': {
        'nationality': 'American',
        'born': 'January 29, 1954',
        'net_worth': '$2.5 Billion',
        'known_for': 'The Oprah Winfrey Show, OWN Network, media mogul',
        'bio': 'Oprah Gail Winfrey is an American talk show host, television producer, actress, author and philanthropist. Born in rural poverty in Kosciusko, Mississippi, she overcame a difficult childhood to become one of the most influential women in the world.\n\nShe began her media career in radio while in high school and co-anchored a local evening news program before moving to daytime talk. The Oprah Winfrey Show launched nationally in 1986 and became the highest-rated television program of its kind in history, running for 25 seasons.\n\nOprah became the first African American female billionaire through her media empire, which includes the OWN Network, Harpo Productions and O magazine. She is also known for her powerful book club, philanthropic work and her presidential Medal of Freedom.'
    },
    'Roman Reigns': {
        'nationality': 'American',
        'born': 'May 25, 1985',
        'net_worth': '$12 Million',
        'known_for': 'Universal Champion, The Tribal Chief, The Head of the Table',
        'bio': 'Leati Joseph Anoa\'i, known professionally as Roman Reigns, is an American professional wrestler and former American football player. Born in Pensacola, Florida, he comes from the legendary Anoa\'i wrestling dynasty.\n\nHe played college football at Georgia Tech and briefly played in the NFL before transitioning to professional wrestling. He signed with WWE in 2010 and trained at their developmental territory before debuting on the main roster as part of The Shield in 2012.\n\nRoman became one of WWE\'s most dominant champions, holding the Universal Championship and later the WWE Championship simultaneously as the Undisputed WWE Universal Champion. His character The Tribal Chief and Head of the Table is widely considered one of the greatest character evolutions in wrestling history.'
    },
    'John Cena': {
        'nationality': 'American',
        'born': 'April 23, 1977',
        'net_worth': '$60 Million',
        'known_for': 'You Can\'t See Me, 16-time World Champion, Hollywood career',
        'bio': 'John Felix Anthony Cena is an American professional wrestler, actor and television presenter. Born in West Newbury, Massachusetts, he studied exercise physiology at Springfield College before pursuing a career in bodybuilding and wrestling.\n\nHe signed with WWE in 2001 and became one of the company\'s most recognizable faces, winning a record-tying 16 world championships. Known for his Never Give Up motto and his tremendous work with the Make-A-Wish Foundation — having granted over 650 wishes — he became one of wrestling\'s most beloved figures.\n\nCena successfully transitioned into acting, starring in films such as The Marine, Trainwreck, Blockers and The Suicide Squad. He also hosted the reality show Are You Smarter Than a 5th Grader. He is one of the most decorated wrestlers and respected entertainers in the industry.'
    },
    'Kim Kardashian': {
        'nationality': 'American',
        'born': 'October 21, 1980',
        'net_worth': '$1.7 Billion',
        'known_for': 'Keeping Up with the Kardashians, SKIMS, KKW Beauty',
        'bio': 'Kimberly Noel Kardashian is an American media personality, socialite, businesswoman and model. Born in Los Angeles, California, she first gained public attention as a friend and stylist of Paris Hilton before becoming a television personality in her own right.\n\nKeeping Up with the Kardashians, which premiered in 2007, became one of the longest-running reality television series and turned the entire Kardashian family into global celebrities. Kim leveraged her fame into multiple successful business ventures.\n\nHer SKIMS shapewear company was valued at over 4 billion dollars, and her KKW Beauty line achieved massive commercial success. Kim has also pursued criminal justice reform, working to free wrongfully incarcerated individuals. She passed the baby bar exam in 2021 and is pursuing a law degree.'
    },
    'Conor McGregor': {
        'nationality': 'Irish',
        'born': 'July 14, 1988',
        'net_worth': '$200 Million',
        'known_for': 'UFC Double Champion, Floyd Mayweather bout, Proper Twelve whiskey',
        'bio': 'Conor Anthony McGregor is an Irish professional mixed martial artist, boxer and businessman. Born in Crumlin, Dublin, Ireland, he began training in boxing at age twelve before transitioning to MMA.\n\nHe became the first fighter in UFC history to hold championships in two weight divisions simultaneously, winning the featherweight title in 2015 and the lightweight title in 2016. His trash-talking persona and electrifying fighting style made him one of the sport\'s biggest draws.\n\nIn 2017, McGregor crossed over into boxing to face Floyd Mayweather Jr. in one of the highest-grossing combat sports events in history. Beyond fighting, he founded Proper No. Twelve Irish Whiskey, which he sold for a reported 600 million dollars, making him one of the wealthiest combat sports athletes in history.'
    },
}

with app.app_context():
    updated = 0
    for name, info in data.items():
        celeb = Celebrity.query.filter_by(name=name).first()
        if celeb:
            celeb.nationality = info.get('nationality')
            celeb.born = info.get('born')
            celeb.net_worth = info.get('net_worth')
            celeb.known_for = info.get('known_for')
            celeb.bio = info.get('bio')
            updated += 1
    db.session.commit()
    print(f'Updated {updated} celebrities with bio data!')
    print('Remaining celebrities can be edited through the admin panel at /admin/celebrities')
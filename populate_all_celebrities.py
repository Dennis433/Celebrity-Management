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
        'bio': 'Ed Sheeran is one of the best-selling music artists of all time, with over 150 million records sold worldwide. Born in Halifax, West Yorkshire, he began playing guitar at age eleven and started performing at local venues as a teenager.\n\nHe moved to London at seventeen to pursue his music career, busking on the streets before being discovered. His debut album Plus was released in 2011 and reached number one in the UK. He followed it with Multiply, Divide and Equals, each breaking records worldwide.\n\nEd has won multiple Grammy Awards, Brit Awards and Ivor Novello Awards. Known for his unique ability to blend pop, folk, hip hop and soul, he is considered one of the most versatile artists of his generation.'
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
        'bio': 'Justin Bieber is a Canadian singer who was discovered at the age of thirteen by talent manager Scooter Braun after posting YouTube videos of himself singing. He was subsequently introduced to R&B artist Usher and signed to RBMG Records.\n\nBorn in London, Ontario, Canada, Justin released his debut EP My World in 2009, becoming the first artist to have seven songs from a debut record chart on the Billboard Hot 100.\n\nDespite personal challenges throughout his career, Justin has maintained a massive global fanbase known as Beliebers. His album Justice released in 2021 debuted at number one in multiple countries.'
    },
    'Adele': {
        'nationality': 'British',
        'born': 'May 5, 1988',
        'net_worth': '$220 Million',
        'known_for': 'Hello, Rolling in the Deep, Someone Like You',
        'bio': 'Adele Laurie Blue Adkins, known professionally as Adele, is an English singer and songwriter. Born in Tottenham, London, she attended the BRIT School for Performing Arts and Technology where she honed her vocal talents.\n\nShe was discovered by XL Recordings after a friend posted her demo on Myspace. Her debut album 19 established her as a major artist. Her second album 21 became one of the best-selling albums of all time, winning six Grammy Awards.\n\nAdele is known for her powerful mezzo-soprano voice and deeply personal songwriting. Her album 25 broke the record for first-week album sales in both the US and UK. She returned with the critically acclaimed 30 in 2021.'
    },
    'Rihanna': {
        'nationality': 'Barbadian',
        'born': 'February 20, 1988',
        'net_worth': '$1.4 Billion',
        'known_for': 'Umbrella, Diamonds, We Found Love, Work',
        'bio': 'Robyn Rihanna Fenty is a Barbadian singer, actress and businesswoman. Born in Saint Michael, Barbados, she was discovered at age fifteen by American record producer Evan Rogers.\n\nShe signed with Def Jam Recordings in 2005 and released her debut album Music of the Sun. Her career skyrocketed with Good Girl Gone Bad in 2007, featuring the global hit Umbrella.\n\nBeyond music, Rihanna has built a business empire. Her Fenty Beauty cosmetics line was valued at over one billion dollars within its first year. Her Savage X Fenty lingerie brand has also achieved massive commercial success, making her one of the wealthiest entertainers in the world.'
    },
    'Beyoncé': {
        'nationality': 'American',
        'born': 'September 4, 1981',
        'net_worth': '$500 Million',
        'known_for': 'Crazy in Love, Halo, Lemonade, Single Ladies',
        'bio': 'Beyoncé Giselle Knowles-Carter is an American singer, songwriter, actress and businesswoman. Born in Houston, Texas, she began performing in singing and dancing competitions as a child.\n\nShe rose to fame in the late 1990s as the lead singer of Destiny\'s Child, one of the best-selling girl groups of all time. Her solo debut album Dangerously in Love in 2003 established her as one of the premier artists of her generation.\n\nBeyoncé has won 32 Grammy Awards, the most of any artist in history. Known for her powerful voice, electrifying stage presence and boundary-pushing artistry, she is widely regarded as one of the greatest performers of all time.'
    },
    'Drake': {
        'nationality': 'Canadian',
        'born': 'October 24, 1986',
        'net_worth': '$250 Million',
        'known_for': 'God\'s Plan, Hotline Bling, One Dance, Started From the Bottom',
        'bio': 'Aubrey Drake Graham, known professionally as Drake, is a Canadian rapper, singer, songwriter and actor. Born in Toronto, Ontario, he first gained recognition as an actor on the teen drama Degrassi: The Next Generation.\n\nHe launched his music career with the mixtape Room for Improvement in 2006 and quickly gained attention in the hip hop community. After signing with Young Money Entertainment, he released his debut studio album Thank Me Later in 2010.\n\nDrake has broken numerous records throughout his career, including the most Billboard Hot 100 entries of any artist in history. He has won four Grammy Awards and multiple Billboard Music Awards.'
    },
    'Bruno Mars': {
        'nationality': 'American',
        'born': 'October 8, 1985',
        'net_worth': '$175 Million',
        'known_for': 'Just the Way You Are, Uptown Funk, That\'s What I Like',
        'bio': 'Peter Gene Hernandez, known professionally as Bruno Mars, is an American singer, songwriter, record producer and dancer. Born in Honolulu, Hawaii, he grew up performing in a family band and developed an early love for music.\n\nHe moved to Los Angeles after high school to pursue a music career. His debut album Doo-Wops and Hooligans produced the hits Just the Way You Are and Grenade.\n\nBruno is known for his incredible versatility, effortlessly blending pop, funk, R&B, reggae and soul. His live performances are legendary for their energy and precision. He has won 15 Grammy Awards and sold over 130 million records worldwide.'
    },
    'The Weeknd': {
        'nationality': 'Canadian',
        'born': 'February 16, 1990',
        'net_worth': '$300 Million',
        'known_for': 'Blinding Lights, Starboy, Can\'t Feel My Face',
        'bio': 'Abel Makkonen Tesfaye, known professionally as The Weeknd, is a Canadian singer, songwriter and record producer. Born in Toronto to Ethiopian immigrant parents, he dropped out of high school at seventeen to pursue music.\n\nHe began his career by anonymously uploading songs to YouTube in 2010, quickly building a cult following with his dark, atmospheric R&B sound. His mixtape trilogy led to a deal with Republic Records.\n\nThe Weeknd has become one of the most streamed artists of all time. His album After Hours and its single Blinding Lights broke numerous streaming records. He delivered a critically praised Super Bowl halftime performance in 2021.'
    },
    'Shawn Mendes': {
        'nationality': 'Canadian',
        'born': 'August 8, 1998',
        'net_worth': '$40 Million',
        'known_for': 'Treat You Better, Stitches, There\'s Nothing Holdin\' Me Back',
        'bio': 'Shawn Peter Raul Mendes is a Canadian singer and songwriter who rose to fame through the social media platform Vine in 2013. Born in Toronto, Ontario, he began posting videos of himself performing covers of popular songs at age fifteen.\n\nHe was discovered by artist manager Andrew Gertler and signed to Island Records. His debut single Life of the Party became the highest-charting debut for any artist under eighteen on the Billboard Hot 100.\n\nShawn has released multiple platinum albums and has sold out arenas worldwide. He is known for his soulful voice, acoustic guitar skills and heartfelt songwriting. His collaborations with artists like Camila Cabello have produced global hits.'
    },
    'Sam Smith': {
        'nationality': 'British',
        'born': 'May 19, 1992',
        'net_worth': '$25 Million',
        'known_for': 'Stay With Me, Writing\'s on the Wall, Unholy',
        'bio': 'Sam Smith is a British singer and songwriter known for their powerful soulful voice and deeply emotional ballads. Born in London, they grew up in Great Chishill, Cambridgeshire, and began singing from a very young age.\n\nThey rose to international fame with their feature on Disclosure\'s single Latch in 2012 and subsequently released their debut album In the Lonely Hour in 2014, which included the global hit Stay With Me.\n\nSam won four Grammy Awards at the 2015 ceremony, including Best New Artist and Record of the Year. They also recorded the Bond theme Writing\'s on the Wall for Spectre, winning an Academy Award. Their 2022 collaboration Unholy with Kim Petras became a worldwide phenomenon.'
    },
    'Lewis Capaldi': {
        'nationality': 'Scottish',
        'born': 'October 7, 1996',
        'net_worth': '$10 Million',
        'known_for': 'Someone You Loved, Before You Go, Pointless',
        'bio': 'Lewis Marc Capaldi is a Scottish singer and songwriter known for his powerful emotional ballads and down-to-earth personality. Born in Whitburn, West Lothian, Scotland, he began performing at local venues at age nine.\n\nHe gained wider attention after posting videos on social media and signing with Vertigo Records. His debut single Bruises gained millions of streams and his follow-up Someone You Loved spent nine weeks at number one in the UK.\n\nLewis won the Brit Award for Song of the Year and was nominated for two Grammy Awards. Known for his self-deprecating humor and authenticity on social media, he has built a devoted global fanbase.'
    },
    'Charlie Puth': {
        'nationality': 'American',
        'born': 'December 2, 1991',
        'net_worth': '$25 Million',
        'known_for': 'See You Again, Attention, We Don\'t Talk Anymore',
        'bio': 'Charles Otto Puth Jr. is an American singer, songwriter and record producer known for his vocal range and musical talent. Born in Rumson, New Jersey, he studied at the Berklee College of Music before pursuing a career in the music industry.\n\nHe gained worldwide recognition with the song See You Again, recorded as a tribute to Paul Walker for the Furious 7 soundtrack. The song spent twelve consecutive weeks at number one on the Billboard Hot 100.\n\nCharlie has released multiple successful albums and is known for producing and writing all of his own music. His ability to identify musical notes without hearing them, known as perfect pitch, is a defining feature of his musical identity.'
    },
    'Dua Lipa': {
        'nationality': 'British-Albanian',
        'born': 'August 22, 1995',
        'net_worth': '$35 Million',
        'known_for': 'Levitating, Don\'t Start Now, New Rules',
        'bio': 'Dua Lipa is a British-Albanian singer and songwriter who has become one of the defining pop artists of her generation. Born in London to Albanian parents, she moved to Kosovo at age eleven before returning to London at fifteen to pursue a music career.\n\nShe signed with Warner Music Group and released her self-titled debut album in 2017. Her second album Future Nostalgia, released in 2020, was a critical and commercial triumph, winning her two Grammy Awards including Best Pop Vocal Album.\n\nDua is known for her unique deep voice, retro-inspired pop sound and bold fashion choices. She has become one of the most streamed female artists in the world and a prominent advocate for artists\' rights.'
    },
    'Ariana Grande': {
        'nationality': 'American',
        'born': 'June 26, 1993',
        'net_worth': '$200 Million',
        'known_for': 'Thank U, Next, 7 Rings, Problem, God is a Woman',
        'bio': 'Ariana Grande-Butera is an American singer, songwriter and actress known for her wide vocal range and distinctive high ponytail. Born in Boca Raton, Florida, she began her career in the Broadway musical 13 before gaining television fame on Victorious.\n\nHer debut album Yours Truly debuted at number one on the Billboard 200 in 2013. She went on to release a series of critically acclaimed and commercially successful albums including My Everything, Dangerous Woman and Thank U, Next.\n\nAriana has won a Grammy Award, two Billboard Music Awards and numerous other accolades. She is one of the most followed people on social media and one of the best-selling music artists of all time, having sold over 85 million records worldwide.'
    },
    'Selena Gomez': {
        'nationality': 'American',
        'born': 'July 22, 1992',
        'net_worth': '$800 Million',
        'known_for': 'Lose You to Love Me, Come & Get It, Wolves',
        'bio': 'Selena Marie Gomez is an American singer, actress, and businesswoman who first rose to fame as a child actress on Barney and Friends and later as the star of Disney Channel\'s Wizards of Waverly Place.\n\nShe transitioned into a successful music career, releasing multiple platinum albums and hit singles. Her personal struggles with lupus and mental health have made her an advocate for health awareness and authenticity.\n\nBeyond entertainment, Selena founded Rare Beauty, a cosmetics line that became a billion-dollar brand within years of its launch. She is also the executive producer of the Netflix series 13 Reasons Why and the documentary My Mind and Me.'
    },
    'Miley Cyrus': {
        'nationality': 'American',
        'born': 'November 23, 1992',
        'net_worth': '$160 Million',
        'known_for': 'Wrecking Ball, Flowers, The Climb, Party in the U.S.A.',
        'bio': 'Destiny Hope Cyrus, known professionally as Miley Cyrus, is an American singer, songwriter and actress. Born in Franklin, Tennessee, the daughter of country singer Billy Ray Cyrus, she grew up surrounded by music.\n\nShe gained worldwide fame playing the dual role of Miley Stewart and pop star Hannah Montana on the Disney Channel series. She transitioned to a more mature and controversial image with her 2013 album Bangerz.\n\nMiley is known for her constant artistic reinvention and powerful live performances. Her 2023 single Flowers became one of the fastest songs in history to reach one billion streams on Spotify and won her first Grammy Awards.'
    },
    'Lady Gaga': {
        'nationality': 'American',
        'born': 'March 28, 1986',
        'net_worth': '$320 Million',
        'known_for': 'Poker Face, Bad Romance, Shallow, Born This Way',
        'bio': 'Stefani Joanne Angelina Germanotta, known professionally as Lady Gaga, is an American singer, songwriter and actress. Born in Manhattan, New York City, she studied at the Tisch School of the Arts before pursuing her music career.\n\nHer debut album The Fame introduced the world to her provocative image and electropop sound with hits like Just Dance and Poker Face. She followed it with The Fame Monster which included the iconic Bad Romance.\n\nLady Gaga has won 13 Grammy Awards, an Academy Award, a BAFTA Award and a Golden Globe. She is known for her boundary-pushing artistry, elaborate stage shows and powerful advocacy for LGBTQ rights and mental health awareness.'
    },
    'Katy Perry': {
        'nationality': 'American',
        'born': 'October 25, 1984',
        'net_worth': '$330 Million',
        'known_for': 'Roar, Firework, I Kissed a Girl, California Gurls',
        'bio': 'Katheryn Elizabeth Hudson, known professionally as Katy Perry, is an American singer, songwriter and television personality. Born in Santa Barbara, California, she was raised in a religious household and initially began her career in gospel music.\n\nShe broke into mainstream pop with the controversial hit I Kissed a Girl in 2008. Her album Teenage Dream produced five number one singles on the Billboard Hot 100, making her the first female artist to achieve this feat.\n\nKaty has sold over 143 million records worldwide and is one of the best-selling music artists of all time. She served as a judge on American Idol and has been recognized for her colorful, theatrical performance style and catchy pop anthems.'
    },
    'Chris Brown': {
        'nationality': 'American',
        'born': 'May 5, 1989',
        'net_worth': '$50 Million',
        'known_for': 'With You, Forever, Look at Me Now, No Guidance',
        'bio': 'Christopher Maurice Brown is an American singer, songwriter, dancer and actor. Born in Tappahannock, Virginia, he began singing and dancing at a young age, citing Michael Jackson as his primary influence.\n\nHe was signed to Jive Records at age fifteen and released his self-titled debut album in 2005 at the age of sixteen, achieving instant commercial success. His single Run It debuted at number one on the Billboard Hot 100.\n\nChris is widely regarded as one of the most talented performers of his generation, known for his exceptional dancing ability and vocal range. Despite personal controversies, he has continued to release commercially successful music and maintain a dedicated global fanbase.'
    },
    'Post Malone': {
        'nationality': 'American',
        'born': 'July 4, 1995',
        'net_worth': '$45 Million',
        'known_for': 'Rockstar, Sunflower, Circles, White Iverson',
        'bio': 'Austin Richard Post, known professionally as Post Malone, is an American rapper, singer, songwriter and record producer. Born in Syracuse, New York, he grew up in Grapevine, Texas, and taught himself guitar by playing Guitar Hero.\n\nHe rose to fame in 2015 with the song White Iverson, which went viral on SoundCloud. His debut album Stoney was certified seven times platinum by the RIAA. His subsequent albums Hollywood\'s Bleeding and Beerbongs and Bentleys have both broken streaming records.\n\nPost Malone is known for his genre-blending approach that incorporates elements of hip hop, pop, country and rock. His face tattoos and laid-back persona have made him one of the most recognizable artists of his generation.'
    },
    'Harry Styles': {
        'nationality': 'British',
        'born': 'February 1, 1994',
        'net_worth': '$100 Million',
        'known_for': 'Watermelon Sugar, As It Was, Adore You',
        'bio': 'Harry Edward Styles is a British singer, songwriter and actor who first rose to fame as a member of the boy band One Direction. Born in Redditch, Worcestershire, he auditioned for The X Factor as a solo artist in 2010 before being grouped with four other contestants.\n\nOne Direction became one of the best-selling boy bands of all time before going on hiatus in 2016. Harry launched his solo career with his self-titled debut album in 2017, which showcased a more mature, rock-influenced sound.\n\nHis second album Fine Line debuted at number one in the US and produced the Grammy-winning hit Watermelon Sugar. His third album Harry\'s House won Album of the Year at the Grammy Awards. He is also known for his acting roles in Dunkirk and Don\'t Worry Darling.'
    },
    'Billie Eilish': {
        'nationality': 'American',
        'born': 'December 18, 2001',
        'net_worth': '$25 Million',
        'known_for': 'Bad Guy, Happier Than Ever, Ocean Eyes, No Time to Die',
        'bio': 'Billie Eilish Pirate Baird O\'Connell is an American singer and songwriter who became a global pop phenomenon as a teenager. Born in Los Angeles, California, she was homeschooled and grew up in a musical family.\n\nShe uploaded the song Ocean Eyes to SoundCloud at age thirteen, and it went viral almost immediately. Her debut EP Don\'t Smile at Me was released in 2017 and became the first EP by a solo artist born in the 2000s to chart on the Billboard 200.\n\nAt age eighteen, Billie became the youngest artist to win all four main Grammy categories — Best New Artist, Album of the Year, Song of the Year and Record of the Year — for her debut album When We All Fall Asleep, Where Do We Go? She also recorded the Bond theme No Time to Die.'
    },
    'Sia': {
        'nationality': 'Australian',
        'born': 'December 18, 1975',
        'net_worth': '$30 Million',
        'known_for': 'Chandelier, Cheap Thrills, Titanium, Elastic Heart',
        'bio': 'Sia Kate Isobelle Furler is an Australian singer, songwriter and director known for her powerful voice and her choice to perform with her face hidden beneath large wigs. Born in Adelaide, South Australia, she began her music career in the early 1990s.\n\nAfter years of writing hits for other artists, including Rihanna, Beyoncé and Katy Perry, Sia launched her own successful solo career with the album 1000 Forms of Fear in 2014, which included the global hit Chandelier.\n\nSia is one of the most prolific songwriters in the music industry, having written hundreds of songs for major artists. She is known for her unique artistic vision, her advocacy for mental health and her distinctive visual style featuring a face-obscuring blonde wig.'
    },
    'Celine Dion': {
        'nationality': 'Canadian',
        'born': 'March 30, 1968',
        'net_worth': '$800 Million',
        'known_for': 'My Heart Will Go On, The Power of Love, Because You Loved Me',
        'bio': 'Celine Marie Claudette Dion is a Canadian singer widely regarded as one of the greatest vocalists of all time. Born in Charlemagne, Quebec, the youngest of fourteen children, she recorded her first song at age twelve.\n\nShe gained international recognition after winning the Eurovision Song Contest in 1988 representing Switzerland. Her English-language debut album Unison launched her career in the English-speaking world. Her 1997 Titanic soundtrack contribution My Heart Will Go On became one of the best-selling physical singles of all time.\n\nCeline has sold over 200 million records worldwide and has won five Grammy Awards. Her Las Vegas residency A New Day became the highest-grossing concert residency in history. She continues to inspire millions despite her personal health challenges.'
    },
    'Michael Bublé': {
        'nationality': 'Canadian',
        'born': 'September 9, 1975',
        'net_worth': '$80 Million',
        'known_for': 'Haven\'t Met You Yet, Feeling Good, It\'s a Beautiful Day',
        'bio': 'Michael Steven Bublé is a Canadian singer, songwriter and actor known for his smooth crooner style and his interpretations of classic jazz and pop standards. Born in Burnaby, British Columbia, he grew up listening to the music of artists like Frank Sinatra, Bobby Darin and Nat King Cole.\n\nHe was discovered by producer David Foster and released his self-titled debut album in 2003. His fourth studio album Crazy Love debuted at number one in both the US and Canada and won the Grammy Award for Best Traditional Pop Vocal Album.\n\nMichael is known for his charming stage presence, warm voice and his ability to blend traditional pop with contemporary sensibilities. He has sold over 60 million albums worldwide and is particularly beloved for his Christmas album, one of the best-selling holiday albums of all time.'
    },
    'Elton John': {
        'nationality': 'British',
        'born': 'March 25, 1947',
        'net_worth': '$550 Million',
        'known_for': 'Rocket Man, Tiny Dancer, Your Song, Crocodile Rock',
        'bio': 'Sir Elton Hercules John is a British singer, pianist and composer who is one of the best-selling music artists of all time, with estimated record sales of 300 million. Born Reginald Kenneth Dwight in Pinner, Middlesex, he showed prodigious musical talent from an early age.\n\nHe collaborated extensively with lyricist Bernie Taupin and together they created some of the most beloved songs in pop music history. His albums including Goodbye Yellow Brick Road and Honky Château are considered among the greatest albums ever made.\n\nElton has won five Grammy Awards, an Academy Award, a Golden Globe Award and a Tony Award. He was knighted by Queen Elizabeth II in 1998 for his services to music and charity. His Farewell Yellow Brick Road tour became one of the highest-grossing concert tours in history.'
    },
    'Shakira': {
        'nationality': 'Colombian',
        'born': 'February 2, 1977',
        'net_worth': '$300 Million',
        'known_for': 'Hips Don\'t Lie, Waka Waka, She Wolf, Whenever, Wherever',
        'bio': 'Shakira Isabel Mebarak Ripoll is a Colombian singer, songwriter and dancer who is one of the best-selling Latin music artists of all time. Born in Barranquilla, Colombia, to a Lebanese-Colombian family, she began writing songs at age eight.\n\nShe gained international fame with her crossover album Laundry Service in 2001, which included the hits Whenever, Wherever and Underneath Your Clothes. Her 2006 album She Wolf and the smash hit Hips Don\'t Lie with Wyclef Jean cemented her global superstar status.\n\nShakira is known for her distinctive raspy voice, multilingual recordings in both Spanish and English, and her signature belly dancing style. She has won three Grammy Awards and twelve Latin Grammy Awards and is a UNESCO Goodwill Ambassador.'
    },
    'Pitbull': {
        'nationality': 'American',
        'born': 'January 15, 1981',
        'net_worth': '$100 Million',
        'known_for': 'Give Me Everything, Timber, International Love, Feel This Moment',
        'bio': 'Armando Christian Pérez, known professionally as Pitbull, is an American rapper and singer of Cuban descent. Born in Miami, Florida, he grew up in a Cuban-American household and was deeply influenced by Miami bass and hip hop culture.\n\nHe signed with TVT Records and released his debut album M.I.A.M.I. in 2004. He gained mainstream success with his 2011 album Planet Pit, which included the global hits Give Me Everything and International Love.\n\nPitbull is known for his energetic live performances and his ability to blend hip hop with dance, pop and electronic music. He has collaborated with artists including Jennifer Lopez, Kesha and Enrique Iglesias. He is also a successful entrepreneur and motivational speaker, often citing his Cuban heritage as a source of inspiration.'
    },
    'Dwayne Johnson': {
        'nationality': 'American',
        'born': 'May 2, 1972',
        'net_worth': '$800 Million',
        'known_for': 'The Rock, Fast & Furious franchise, Jumanji',
        'bio': 'Dwayne Douglas Johnson, also known by his ring name The Rock, is an American actor, businessman and former professional wrestler. Born in Hayward, California, he comes from a wrestling family — his father and grandfather were both professional wrestlers.\n\nAfter a brief career in Canadian football, he joined the WWF in 1996 and became one of the most popular and electrifying performers in wrestling history. He transitioned to acting in 2001 and quickly became one of Hollywood\'s most bankable stars.\n\nDwayne has starred in some of the highest-grossing films of all time, including the Fast & Furious franchise, Jumanji and Black Adam. He is consistently ranked as one of the highest-paid actors in the world and was named Time magazine\'s 100 most influential people multiple times.'
    },
    'Kevin Hart': {
        'nationality': 'American',
        'born': 'July 6, 1979',
        'net_worth': '$200 Million',
        'known_for': 'Ride Along, Central Intelligence, stand-up comedy',
        'bio': 'Kevin Darnell Hart is an American stand-up comedian and actor who is one of the highest-grossing comedians in the world. Born in Philadelphia, Pennsylvania, he began his career performing stand-up comedy at local clubs before moving to New York.\n\nHe gained national recognition through his stand-up specials and his roles in films such as Ride Along, Get Hard and Central Intelligence. His comedy tours have sold out stadiums around the world and his Netflix specials have been viewed by tens of millions.\n\nKevin has expanded his empire through his entertainment company Laugh Out Loud Network and his fitness brand. Despite personal and professional setbacks, he has consistently reinvented himself and maintained his position as one of entertainment\'s biggest stars.'
    },
    'Will Smith': {
        'nationality': 'American',
        'born': 'September 25, 1968',
        'net_worth': '$350 Million',
        'known_for': 'The Fresh Prince of Bel-Air, Men in Black, Ali, King Richard',
        'bio': 'Willard Carroll Smith II is an American actor, rapper and film producer who is widely regarded as one of the most powerful and consistent box office draws in Hollywood. Born in Philadelphia, Pennsylvania, he began his career as a rapper under the name The Fresh Prince.\n\nHe gained international fame as the star of the sitcom The Fresh Prince of Bel-Air. He transitioned into films with Six Degrees of Separation and Bad Boys, establishing himself as a major movie star. His performances in Ali and The Pursuit of Happyness earned him Academy Award nominations.\n\nWill has been nominated for five Golden Globe Awards and two Academy Awards, winning the Best Actor Oscar for his portrayal of Richard Williams in King Richard in 2022. He is one of only eight actors to have won the Golden Globe, Screen Actors Guild Award and Academy Award for the same performance.'
    },
    'Leonardo DiCaprio': {
        'nationality': 'American',
        'born': 'November 11, 1974',
        'net_worth': '$300 Million',
        'known_for': 'Titanic, The Wolf of Wall Street, Inception, The Revenant',
        'bio': 'Leonardo Wilhelm DiCaprio is an American actor and film producer who is widely regarded as one of the greatest actors of his generation. Born in Los Angeles, California, he began his career with small television roles before making his film debut in Critters 3.\n\nHe received his first Academy Award nomination for What\'s Eating Gilbert Grape at age nineteen. His starring role in Titanic in 1997 made him one of the most recognizable faces in the world. He went on to collaborate extensively with director Martin Scorsese.\n\nLeonardo won the Academy Award for Best Actor for his role in The Revenant in 2016. He is also a passionate environmental activist and has donated tens of millions of dollars to conservation causes through his foundation. He serves as a United Nations Messenger of Peace.'
    },
    'Tom Cruise': {
        'nationality': 'American',
        'born': 'July 3, 1962',
        'net_worth': '$600 Million',
        'known_for': 'Mission: Impossible franchise, Top Gun, Jerry Maguire',
        'bio': 'Thomas Cruise Mapother IV, known professionally as Tom Cruise, is an American actor and film producer who is one of the highest-paid actors in the world. Born in Syracuse, New York, he had a difficult childhood marked by frequent moves and a struggling family.\n\nHe made his film debut in Endless Love in 1981 and quickly rose to fame with Risky Business and Top Gun. His performance in Born on the Fourth of July earned him his first Academy Award nomination.\n\nTom is known for performing his own stunts, particularly in the Mission: Impossible franchise which has become one of the highest-grossing action franchises in history. He has received three Academy Award nominations and three Golden Globe Awards. He continues to be one of the most bankable stars in Hollywood.'
    },
    'Brad Pitt': {
        'nationality': 'American',
        'born': 'December 18, 1963',
        'net_worth': '$400 Million',
        'known_for': 'Fight Club, Se7en, Troy, Once Upon a Time in Hollywood',
        'bio': 'William Bradley Pitt is an American actor and film producer who has been described as one of the most influential figures in the history of Hollywood. Born in Shawnee, Oklahoma, he studied journalism at the University of Missouri before dropping out to pursue acting.\n\nHe gained attention with supporting roles in Thelma and Louise and A River Runs Through It. He established himself as a leading man with Se7en, Twelve Monkeys and Fight Club. His production company Plan B has produced numerous critically acclaimed films including 12 Years a Slave and Moonlight.\n\nBrad has won two Academy Awards — Best Supporting Actor for Twelve Monkeys and Best Picture as a producer. He received his first Best Actor win for Once Upon a Time in Hollywood. He continues to be one of the most respected and sought-after performers in the industry.'
    },
    'Angelina Jolie': {
        'nationality': 'American',
        'born': 'June 4, 1975',
        'net_worth': '$120 Million',
        'known_for': 'Lara Croft: Tomb Raider, Maleficent, Girl Interrupted, Gia',
        'bio': 'Angelina Jolie Voight is an American actress, filmmaker and humanitarian who is considered one of the most powerful women in the entertainment industry. Born in Los Angeles, California, the daughter of actor Jon Voight, she began modeling at age fourteen.\n\nShe won the Academy Award for Best Supporting Actress for her role in Girl Interrupted in 2000. Her action roles in Lara Croft: Tomb Raider and Mr. and Mrs. Smith made her an international superstar and one of the highest-paid actresses in Hollywood.\n\nBeyond her acting career, Angelina is a dedicated humanitarian and former Special Envoy for the United Nations High Commissioner for Refugees. She has adopted three children and is a mother of six. She has received the Jean Hersholt Humanitarian Award from the Academy of Motion Picture Arts and Sciences.'
    },
    'Jennifer Aniston': {
        'nationality': 'American',
        'born': 'February 11, 1969',
        'net_worth': '$320 Million',
        'known_for': 'Friends, The Morning Show, Marley & Me, We\'re the Millers',
        'bio': 'Jennifer Joanna Aniston is an American actress, producer and businesswoman who is best known for her portrayal of Rachel Green on the television sitcom Friends, which ran from 1994 to 2004. Born in Sherman Oaks, Los Angeles, she is the daughter of Greek-American actor John Aniston.\n\nFriends became one of the most watched television series in history, and Jennifer\'s character Rachel Green became a cultural icon. The Rachel haircut became one of the most requested hairstyles of the 1990s. She won an Emmy Award, a Golden Globe and a Screen Actors Guild Award for her performance.\n\nSince Friends, Jennifer has built a successful film career with hits including Marley & Me, Just Go with It and We\'re the Millers. She co-founded the production company Echo Films and starred in and produced the critically acclaimed Apple TV+ series The Morning Show.'
    },
    'Johnny Depp': {
        'nationality': 'American',
        'born': 'June 9, 1963',
        'net_worth': '$150 Million',
        'known_for': 'Pirates of the Caribbean, Edward Scissorhands, Fear and Loathing in Las Vegas',
        'bio': 'John Christopher Depp II is an American actor, producer and musician who is widely regarded as one of the most versatile and eccentric performers in Hollywood. Born in Owensboro, Kentucky, he dropped out of high school at fifteen to pursue a music career before transitioning to acting.\n\nHe gained recognition with the television series 21 Jump Street and established himself as an unconventional leading man through his collaborations with director Tim Burton in films such as Edward Scissorhands and Ed Wood.\n\nHis portrayal of Captain Jack Sparrow in the Pirates of the Caribbean franchise earned him an Academy Award nomination and made him one of the highest-grossing actors in history. He has received three Academy Award nominations and been honored with a star on the Hollywood Walk of Fame.'
    },
    'Robert Downey Jr.': {
        'nationality': 'American',
        'born': 'April 4, 1965',
        'net_worth': '$300 Million',
        'known_for': 'Iron Man, Avengers franchise, Sherlock Holmes',
        'bio': 'Robert John Downey Jr. is an American actor and producer who is widely considered one of the greatest comeback stories in Hollywood history. Born in Manhattan, New York City, into a show business family, he made his acting debut at age five.\n\nAfter a promising early career with films like Less Than Zero and Chaplin, for which he received an Academy Award nomination, he struggled with substance abuse throughout the late 1990s and early 2000s.\n\nHis extraordinary comeback was sealed with his casting as Tony Stark in Iron Man in 2008, launching the Marvel Cinematic Universe. He became the highest-paid actor in Hollywood for multiple years, earning over 50 million dollars for Avengers: Endgame alone. He has reinvented himself as one of the most beloved and respected actors in the industry.'
    },
    'Chris Hemsworth': {
        'nationality': 'Australian',
        'born': 'August 11, 1983',
        'net_worth': '$130 Million',
        'known_for': 'Thor, Avengers franchise, Extraction',
        'bio': 'Christopher Hemsworth is an Australian actor who rose to international fame through his portrayal of the Marvel superhero Thor in the Marvel Cinematic Universe. Born in Melbourne, Victoria, he began his career on the Australian television soap opera Home and Away.\n\nHe auditioned unsuccessfully for the role of James Kirk in Star Trek before being cast as Thor in 2011. The Thor franchise and his appearances in the Avengers films made him one of the most recognizable actors in the world.\n\nBeyond Marvel, Chris has starred in a range of films including Rush, In the Heart of the Sea and Extraction. He is also known for his dedication to fitness and has launched a successful health and wellness app called Centr. He is considered one of the most charismatic leading men working in Hollywood today.'
    },
    'Chris Evans': {
        'nationality': 'American',
        'born': 'June 13, 1981',
        'net_worth': '$80 Million',
        'known_for': 'Captain America, Avengers franchise, Knives Out',
        'bio': 'Christopher Robert Evans is an American actor best known for his portrayal of Steve Rogers, also known as Captain America, in the Marvel Cinematic Universe. Born in Boston, Massachusetts, he began his career with small television roles before making his film debut.\n\nAfter starring as the Human Torch in the Fantastic Four films, he was cast as Captain America in 2011. His portrayal of the patriotic superhero over eleven years and twelve films made him an international icon. His farewell to the character in Avengers: Endgame was an emotional moment for audiences worldwide.\n\nSince departing the MCU, Chris has demonstrated his range as an actor with critically acclaimed performances in films such as Knives Out and its sequel Glass Onion. He is also known for his political activism and his advocacy for social justice causes.'
    },
    'Scarlett Johansson': {
        'nationality': 'American',
        'born': 'November 22, 1984',
        'net_worth': '$165 Million',
        'known_for': 'Black Widow, Lost in Translation, Marriage Story, Her',
        'bio': 'Scarlett Ingrid Johansson is an American actress and singer who is one of the world\'s highest-paid actresses. Born in New York City, she began her acting career as a child with the stage production of Sophistry.\n\nShe gained critical recognition with her performances in Lost in Translation and Girl with a Pearl Earring. Her portrayal of Natasha Romanoff, also known as Black Widow, in the Marvel Cinematic Universe across ten films made her one of the highest-grossing actresses of all time.\n\nScarlett has received two Academy Award nominations for her performances in Marriage Story and JoJo Rabbit. She is also known for her work as a producer and her advocacy for equal pay in Hollywood. She launched her own production company These Pictures and continues to be one of the most versatile actresses in the industry.'
    },
    'Zendaya': {
        'nationality': 'American',
        'born': 'September 1, 1996',
        'net_worth': '$20 Million',
        'known_for': 'Euphoria, Spider-Man franchise, The Greatest Showman, Dune',
        'bio': 'Zendaya Maree Stoermer Coleman is an American actress, singer and fashion icon who has become one of the most celebrated young talents in Hollywood. Born in Oakland, California, she began her career as a child model and backup dancer.\n\nShe gained fame on the Disney Channel series Shake It Up and K.C. Undercover before making her film debut in the musical The Greatest Showman. Her portrayal of MJ in the Spider-Man MCU films brought her global recognition.\n\nZendaya won the Primetime Emmy Award for Outstanding Lead Actress in a Drama Series for her role as Rue in Euphoria, becoming the youngest person to win the award at age twenty-four. She won again in 2022, making her the youngest two-time winner. She is widely considered one of the most talented and stylish figures in modern entertainment.'
    },
    'Tom Holland': {
        'nationality': 'British',
        'born': 'June 1, 1996',
        'net_worth': '$25 Million',
        'known_for': 'Spider-Man MCU trilogy, Avengers franchise, Cherry, Uncharted',
        'bio': 'Thomas Stanley Holland is a British actor who became a global phenomenon through his portrayal of Peter Parker, also known as Spider-Man, in the Marvel Cinematic Universe. Born in Kingston upon Thames, London, he trained as a dancer from age nine.\n\nHe made his professional debut in the title role of Billy Elliot the Musical in London\'s West End. His acrobatic abilities and youthful energy made him the perfect choice for Spider-Man, and he was cast in 2015 at the age of nineteen.\n\nTom\'s portrayal of Spider-Man across three solo films and multiple Avengers movies has made him one of the most beloved actors of his generation. Beyond Marvel, he has demonstrated dramatic range in films such as Cherry and The Impossible. He is known for his warmth, humility and his close friendship with his co-stars.'
    },
    'Ryan Reynolds': {
        'nationality': 'Canadian',
        'born': 'October 23, 1976',
        'net_worth': '$350 Million',
        'known_for': 'Deadpool franchise, Free Guy, The Proposal, Aviation Gin',
        'bio': 'Ryan Rodney Reynolds is a Canadian-American actor and businessman who has become one of the most bankable stars in Hollywood and one of the savviest entrepreneurs in the entertainment industry. Born in Vancouver, British Columbia, he began his career with the Canadian teen soap opera Hillside.\n\nAfter years of appearing in comedies and action films, his career was transformed by his portrayal of the irreverent antihero Deadpool in 2016. The film became the highest-grossing R-rated film at the time and spawned a franchise.\n\nBeyond acting, Ryan has built a business empire that includes Aviation American Gin, which he sold for over 600 million dollars, and Mint Mobile, which he sold to T-Mobile for 1.35 billion dollars. He is known for his sharp wit, self-deprecating humor and his playful social media presence.'
    },
    'Ryan Gosling': {
        'nationality': 'Canadian',
        'born': 'November 12, 1980',
        'net_worth': '$70 Million',
        'known_for': 'The Notebook, La La Land, Drive, Barbie',
        'bio': 'Ryan Thomas Gosling is a Canadian actor and musician who has established himself as one of the most critically acclaimed and versatile performers of his generation. Born in London, Ontario, he was selected to become a Mouseketeer on The All New Mickey Mouse Club at age twelve.\n\nHe received his first Academy Award nomination for Half Nelson in 2007. His romantic lead performance in The Notebook made him a household name and an enduring symbol of romantic cinema. His performance in La La Land earned him a Golden Globe Award and an Academy Award nomination.\n\nRyan is known for his ability to transform himself entirely for each role, whether playing a stuntman in The Fall Guy or Ken in Barbie, for which his comedic performance earned him an Academy Award nomination. He is widely regarded as one of the most dedicated and talented actors of his era.'
    },
    'Sandra Bullock': {
        'nationality': 'American',
        'born': 'July 26, 1964',
        'net_worth': '$250 Million',
        'known_for': 'Speed, Miss Congeniality, The Blind Side, Gravity',
        'bio': 'Sandra Annette Bullock is an American actress and producer who is one of the most successful stars in Hollywood history. Born in Arlington, Virginia, she grew up in Germany where her father was stationed with the US Army.\n\nShe broke into Hollywood with her role in the action thriller Speed in 1994 alongside Keanu Reeves. She followed it with a string of successful romantic comedies including While You Were Sleeping and Miss Congeniality.\n\nSandra won the Academy Award for Best Actress for her portrayal of Leigh Anne Tuohy in The Blind Side. She was subsequently nominated again for Gravity. She was named People magazine\'s Most Beautiful Woman and has been recognized as one of the most powerful women in Hollywood. Despite stepping back from acting in recent years, she remains one of the most beloved figures in the industry.'
    },
    'Julia Roberts': {
        'nationality': 'American',
        'born': 'October 28, 1967',
        'net_worth': '$250 Million',
        'known_for': 'Pretty Woman, Erin Brockovich, Ocean\'s Eleven, Notting Hill',
        'bio': 'Julia Fiona Roberts is an American actress and producer who is one of the biggest movie stars of her generation and one of the highest-paid actresses in Hollywood history. Born in Smyrna, Georgia, she moved to New York to pursue her acting career after completing high school.\n\nShe became a star with the romantic comedy Mystic Pizza before her breakthrough role in Pretty Woman in 1990, which earned her first Academy Award nomination and made her one of the most recognizable faces in the world.\n\nJulia won the Academy Award for Best Actress for her portrayal of real-life activist Erin Brockovich in 2001. She was the first actress to earn 20 million dollars for a single film. Known for her infectious smile and natural charisma, she has starred in dozens of beloved films across multiple genres.'
    },
    'Jason Statham': {
        'nationality': 'British',
        'born': 'July 26, 1967',
        'net_worth': '$90 Million',
        'known_for': 'The Transporter franchise, Crank, Fast & Furious franchise, The Meg',
        'bio': 'Jason Statham is a British actor who has established himself as one of Hollywood\'s premier action stars. Born in Shirebrook, Derbyshire, he was a competitive diver who represented England in the 1990 Commonwealth Games before turning to acting.\n\nHe was discovered by director Guy Ritchie and made his film debut in Lock, Stock and Two Smoking Barrels in 1998. He gained international fame as the lead in The Transporter franchise, showcasing his martial arts skills and action star charisma.\n\nJason has appeared in numerous major franchises including The Fast and the Furious, The Expendables and The Meg. He is known for performing many of his own stunts and for his imposing physical presence. His films have grossed over 1.5 billion dollars at the worldwide box office.'
    },
    'Keanu Reeves': {
        'nationality': 'Canadian',
        'born': 'September 2, 1964',
        'net_worth': '$380 Million',
        'known_for': 'The Matrix franchise, John Wick franchise, Speed, Point Break',
        'bio': 'Keanu Charles Reeves is a Canadian actor who is widely regarded as one of the most beloved performers in Hollywood history. Born in Beirut, Lebanon, to an English-Hawaiian father and English mother, he grew up in various countries before settling in Toronto.\n\nHe gained recognition with the comedy Bill and Ted\'s Excellent Adventure before his dramatic breakthrough in Point Break and Speed. His portrayal of Neo in The Matrix franchise established him as an action superstar and the film\'s philosophical themes made him a cultural icon.\n\nThe John Wick franchise reinvented his career, with the films becoming celebrated for their innovative action choreography. Known for his humility, generosity and kind personality, Keanu has earned a reputation as one of the nicest people in Hollywood. He has shared his film earnings with crew members and regularly performs acts of random kindness that have been widely reported.'
    },
    'Morgan Freeman': {
        'nationality': 'American',
        'born': 'June 1, 1937',
        'net_worth': '$250 Million',
        'known_for': 'The Shawshank Redemption, Million Dollar Baby, Se7en, Bruce Almighty',
        'bio': 'Morgan Freeman is an American actor, director and narrator who is considered one of the greatest actors of all time and whose distinctive deep voice has become one of the most recognizable in the world. Born in Memphis, Tennessee, he served in the United States Air Force before pursuing his acting career.\n\nHe gained critical recognition with his role in Street Smart in 1987, earning his first Academy Award nomination. He became a household name with his performances in Driving Miss Daisy, The Shawshank Redemption and Se7en.\n\nMorgan won the Academy Award for Best Supporting Actor for Million Dollar Baby. He has received five Academy Award nominations in total and has been honored with the American Film Institute Lifetime Achievement Award. At age 86, he continues to be one of the most in-demand actors in Hollywood.'
    },
    'Gal Gadot': {
        'nationality': 'Israeli',
        'born': 'April 30, 1985',
        'net_worth': '$30 Million',
        'known_for': 'Wonder Woman franchise, Fast & Furious franchise, Red Notice',
        'bio': 'Gal Gadot Varsano is an Israeli actress, model and producer who is best known for her portrayal of Diana Prince, also known as Wonder Woman, in the DC Extended Universe. Born in Petah Tikva, Israel, she won the Miss Israel 2004 pageant at age eighteen.\n\nShe served in the Israel Defense Forces as a combat trainer for two years before pursuing her modelling and acting career. She gained international recognition through her role as Gisele in the Fast & Furious franchise.\n\nHer portrayal of Wonder Woman in Batman v Superman: Dawn of Justice and the standalone Wonder Woman film made her a global superstar. The 2017 Wonder Woman film was both a critical and commercial success, grossing over 820 million dollars worldwide. Gal has become an important symbol of female empowerment in action cinema.'
    },
    'Anne Hathaway': {
        'nationality': 'American',
        'born': 'November 12, 1982',
        'net_worth': '$60 Million',
        'known_for': 'The Princess Diaries, The Devil Wears Prada, Les Misérables, The Dark Knight Rises',
        'bio': 'Anne Jacqueline Hathaway is an American actress who is widely regarded as one of the most talented performers of her generation. Born in Brooklyn, New York City, she was the first teenager to be admitted to the Barrow Group Theatre Company in New York.\n\nShe gained fame with the family film The Princess Diaries in 2001. She demonstrated her dramatic range with critically acclaimed performances in Brokeback Mountain, Rachel Getting Married and The Devil Wears Prada.\n\nAnne won the Academy Award for Best Supporting Actress for her portrayal of Fantine in Les Misérables, for which she also won a Golden Globe and a Screen Actors Guild Award. She has received two Academy Award nominations in total and continues to be one of Hollywood\'s most respected actresses, known for her commitment to her roles and her charitable work.'
    },
    'Margot Robbie': {
        'nationality': 'Australian',
        'born': 'July 2, 1990',
        'net_worth': '$26 Million',
        'known_for': 'The Wolf of Wall Street, Suicide Squad, I, Tonya, Barbie',
        'bio': 'Margot Elise Robbie is an Australian actress and film producer who has established herself as one of the most sought-after talents in Hollywood. Born in Dalby, Queensland, she began her career on the Australian television series Neighbours before moving to the United States.\n\nShe gained international attention with her performance alongside Leonardo DiCaprio in The Wolf of Wall Street. She then portrayed Harley Quinn in Suicide Squad and the critically acclaimed Suicide Squad sequel and Birds of Prey.\n\nMargot received Academy Award nominations for Best Actress for I, Tonya and Best Supporting Actress for Bombshell. Her portrayal of Barbie in the 2023 Greta Gerwig film alongside Ryan Gosling became a worldwide cultural phenomenon, with the film grossing over 1.4 billion dollars. She is also a successful producer through her company LuckyChap Entertainment.'
    },
    'Will Ferrell': {
        'nationality': 'American',
        'born': 'July 16, 1967',
        'net_worth': '$160 Million',
        'known_for': 'Elf, Anchorman, Step Brothers, Blades of Glory',
        'bio': 'John William Ferrell is an American actor, comedian, writer and producer who is considered one of the greatest comedic talents of his generation. Born in Irvine, California, he studied sports information at the University of Southern California before pursuing comedy.\n\nHe joined the cast of Saturday Night Live in 1995 and his impressions of George W. Bush became iconic. He departed SNL in 2002 to focus on his film career and quickly established himself as a leading comedy star with Elf, which has become one of the most beloved Christmas films of all time.\n\nWill co-founded the comedy website and production company Funny or Die, which has become one of the most successful comedy platforms online. His films have collectively grossed over 3 billion dollars worldwide. He is known for his fearless physical comedy, his improvisation skills and his willingness to embarrass himself for the sake of a laugh.'
    },
    'Vin Diesel': {
        'nationality': 'American',
        'born': 'July 18, 1967',
        'net_worth': '$225 Million',
        'known_for': 'Fast & Furious franchise, Guardians of the Galaxy, xXx, Riddick',
        'bio': 'Mark Sinclair, known professionally as Vin Diesel, is an American actor, producer and director who is one of the most commercially successful actors in Hollywood history. Born in Alameda County, California, he began his career writing, directing and starring in short films.\n\nHe gained widespread attention with his breakout role in Steven Spielberg\'s Saving Private Ryan and subsequently starred in Pitch Black and The Fast and the Furious. His portrayal of Dominic Toretto in the Fast & Furious franchise has become his defining role.\n\nVin serves as both actor and producer of the Fast & Furious franchise, which has grossed over 7 billion dollars worldwide making it one of the highest-grossing film franchises in history. He is also the voice of Groot in the Guardians of the Galaxy films. Known for his family-focused persona and his genuine warmth, he is beloved by fans around the world.'
    },
    'Hugh Jackman': {
        'nationality': 'Australian',
        'born': 'October 12, 1968',
        'net_worth': '$180 Million',
        'known_for': 'Logan, X-Men franchise, The Greatest Showman, Les Misérables',
        'bio': 'Hugh Michael Jackman is an Australian actor and producer who is best known for his portrayal of the mutant superhero Wolverine in the X-Men film franchise. Born in Sydney, New South Wales, he trained at the Western Australian Academy of Performing Arts before beginning his career in Australian theatre.\n\nHe was cast as Wolverine in 2000 and portrayed the character for seventeen years across nine films, a record for a superhero role in film history. His farewell performance in the standalone film Logan in 2017 was critically acclaimed and earned him a Screen Actors Guild Award nomination.\n\nHugh is also a renowned stage performer, having won Tony Awards for his roles in The Boy from Oz and The Music Man. His performance in The Greatest Showman demonstrated his versatility as a musical performer. He holds a Guinness World Record for the longest career as a live-action Marvel superhero character.'
    },
    'Emma Watson': {
        'nationality': 'British',
        'born': 'April 15, 1990',
        'net_worth': '$85 Million',
        'known_for': 'Harry Potter franchise, Beauty and the Beast, The Perks of Being a Wallflower',
        'bio': 'Emma Charlotte Duerre Watson is a British actress, model and activist who is best known for her portrayal of Hermione Granger in the Harry Potter film series. Born in Paris, France, to British parents, she began acting lessons at age six.\n\nShe was cast as Hermione Granger at the age of nine, starring in all eight Harry Potter films over eleven years. As the franchise became one of the highest-grossing film series of all time, Emma became one of the most recognizable faces in the world.\n\nAfter Harry Potter, Emma starred in The Perks of Being a Wallflower, This Is the End and the Disney live-action Beauty and the Beast. She is also a prominent activist, particularly for gender equality, having been appointed UN Women Goodwill Ambassador in 2014. She launched the HeForShe campaign, encouraging men to advocate for gender equality.'
    },
    'Nicole Kidman': {
        'nationality': 'Australian-American',
        'born': 'June 20, 1967',
        'net_worth': '$250 Million',
        'known_for': 'Moulin Rouge, The Hours, Eyes Wide Shut, Big Little Lies',
        'bio': 'Nicole Mary Kidman is an Australian-American actress and producer who is one of the most acclaimed and successful performers in Hollywood history. Born in Honolulu, Hawaii, to Australian parents, she grew up in Sydney, Australia.\n\nShe gained international recognition with her performance in the thriller Dead Calm in 1989. Her marriage to Tom Cruise and her starring roles in blockbusters including Far and Away and Eyes Wide Shut brought her worldwide fame.\n\nNicole won the Academy Award for Best Actress for her portrayal of Virginia Woolf in The Hours. She has received five Academy Award nominations in total. Her television work includes the critically acclaimed Big Little Lies and Nine Perfect Strangers. She was appointed a Goodwill Ambassador for UN Women and an Officer of the Order of Australia for her contributions to the arts.'
    },
    'Cristiano Ronaldo': {
        'nationality': 'Portuguese',
        'born': 'February 5, 1985',
        'net_worth': '$500 Million',
        'known_for': 'Five Ballon d\'Or titles, Manchester United, Real Madrid, Al Nassr',
        'bio': 'Cristiano Ronaldo dos Santos Aveiro is a Portuguese professional footballer widely regarded as one of the greatest players of all time. Born in Funchal, Madeira, he joined the Sporting CP academy at age twelve after showing exceptional talent.\n\nManchester United signed him in 2003 at age eighteen. He went on to win three consecutive Premier League titles and the UEFA Champions League before joining Real Madrid for a then world record fee in 2009.\n\nAt Real Madrid, Ronaldo became the all-time leading scorer for the club and won four Champions League titles. He has won five Ballon d\'Or awards and holds the record for the most international goals in football history. He currently plays for Al Nassr in Saudi Arabia and continues to inspire millions with his extraordinary dedication and athleticism.'
    },
    'Lionel Messi': {
        'nationality': 'Argentine',
        'born': 'June 24, 1987',
        'net_worth': '$600 Million',
        'known_for': 'Eight Ballon d\'Or titles, FC Barcelona, Inter Miami, 2022 World Cup winner',
        'bio': 'Lionel Andrés Messi is an Argentine professional footballer widely considered the greatest player of all time. Born in Rosario, Argentina, he was diagnosed with a growth hormone deficiency at age ten. FC Barcelona agreed to pay for his treatment in exchange for joining their famous La Masia academy.\n\nMessi spent over twenty years at Barcelona, becoming their all-time leading scorer and winning ten La Liga titles, four UEFA Champions League titles and eight Ballon d\'Or awards — the most in history.\n\nIn 2021 he moved to Paris Saint-Germain and later Inter Miami in MLS. His greatest achievement came in 2022 when he led Argentina to the FIFA World Cup title in Qatar, fulfilling his lifelong dream and cementing his legacy as the undisputed greatest footballer of all time.'
    },
    'LeBron James': {
        'nationality': 'American',
        'born': 'December 30, 1984',
        'net_worth': '$1 Billion',
        'known_for': 'Four NBA Championships, Lakers, Heat, Cavaliers, all-time NBA scoring leader',
        'bio': 'LeBron Raymone James Sr. is an American professional basketball player for the Los Angeles Lakers in the NBA. Born in Akron, Ohio, he was a highly touted prospect from a young age and was selected first overall in the 2003 NBA Draft.\n\nKnown as King James, he has won four NBA championships with three different teams, four MVP awards and four Finals MVP awards. He surpassed Kareem Abdul-Jabbar\'s all-time NBA scoring record in 2023.\n\nBeyond basketball, LeBron is a successful businessman and philanthropist. He co-founded the production company SpringHill Entertainment and owns a stake in Fenway Sports Group. His I Promise School in Akron provides education and support to at-risk youth. He is widely considered one of the greatest athletes in history.'
    },
    'Stephen Curry': {
        'nationality': 'American',
        'born': 'March 14, 1988',
        'net_worth': '$160 Million',
        'known_for': 'Four NBA Championships, Golden State Warriors, three-point shooting records',
        'bio': 'Wardell Stephen Curry II is an American professional basketball player for the Golden State Warriors who is widely regarded as the greatest shooter in NBA history. Born in Charlotte, North Carolina, the son of former NBA player Dell Curry, he grew up around professional basketball.\n\nDespite being lightly recruited out of high school, he attended Davidson College where he became one of the most electrifying players in college basketball history. After being selected seventh overall in the 2009 NBA Draft by the Golden State Warriors, he transformed the franchise and revolutionized the game.\n\nSteph has won four NBA championships, two MVP awards and six All-Star selections. He has broken the NBA record for three-pointers made in a season multiple times and holds the all-time record for three-pointers in NBA history. His shooting ability has fundamentally changed the way the game of basketball is played at every level.'
    },
    'Serena Williams': {
        'nationality': 'American',
        'born': 'September 26, 1981',
        'net_worth': '$250 Million',
        'known_for': '23 Grand Slam singles titles, greatest tennis player of all time',
        'bio': 'Serena Jameka Williams is a retired American professional tennis player who is widely regarded as the greatest tennis player of all time. Born in Saginaw, Michigan, she began playing tennis at age three under the tutelage of her father Richard Williams.\n\nShe turned professional at age fourteen and went on to win 23 Grand Slam singles titles, the most by any player in the Open Era. She held the number one world ranking for 319 weeks across her career.\n\nBeyond her playing career, Serena has built a successful business empire including venture capital fund Serena Ventures. She is also a fashion designer and has been an outspoken advocate for equal pay and racial equality in sports. She was named by Time magazine as one of the 100 Greatest Athletes of All Time and received the Presidential Medal of Freedom.'
    },
    'Venus Williams': {
        'nationality': 'American',
        'born': 'June 17, 1980',
        'net_worth': '$95 Million',
        'known_for': 'Seven Grand Slam singles titles, Wimbledon champion, equal pay advocate',
        'bio': 'Venus Ebony Starr Williams is an American professional tennis player and entrepreneur who is a former world number one and one of the most influential figures in the history of women\'s tennis. Born in Lynwood, California, she began playing tennis at age four alongside her sister Serena.\n\nShe turned professional at age fourteen and quickly established herself as one of the most dominant forces in women\'s tennis. She has won seven Grand Slam singles titles, including five Wimbledon championships, and four Olympic gold medals.\n\nVenus has been a passionate advocate for equal prize money for women in tennis, playing a significant role in convincing Wimbledon to offer equal prize money in 2007. She also founded the interior design firm V Starr Interiors and her athletic wear brand EleVen. She continues to compete professionally and inspire a new generation of tennis players.'
    },
    'Lewis Hamilton': {
        'nationality': 'British',
        'born': 'January 7, 1985',
        'net_worth': '$285 Million',
        'known_for': 'Seven Formula 1 World Championships, Mercedes AMG Petronas',
        'bio': 'Sir Lewis Carl Davidson Hamilton is a British racing driver who is widely considered the greatest Formula One driver of all time. Born in Stevenage, Hertfordshire, he began karting at age eight and quickly demonstrated exceptional talent.\n\nHe made his Formula One debut with McLaren in 2007 and won his first World Championship in 2008 at age twenty-three, becoming the youngest world champion at the time. He went on to join Mercedes where he dominated the sport, winning six further championships to bring his total to seven, equaling Michael Schumacher\'s record.\n\nLewis holds the records for most wins, most pole positions and most podium finishes in Formula One history. He was knighted in 2021 for services to motorsport. Beyond racing, he is known for his fashion sense, his music interests and his passionate advocacy for diversity and inclusion in motorsport and beyond.'
    },
    'Max Verstappen': {
        'nationality': 'Dutch-Belgian',
        'born': 'September 30, 1997',
        'net_worth': '$60 Million',
        'known_for': 'Four Formula 1 World Championships, Red Bull Racing, youngest F1 race winner',
        'bio': 'Max Emilian Verstappen is a Dutch-Belgian racing driver who currently competes in Formula One for Red Bull Racing. Born in Hasselt, Belgium, to a racing family — his father Jos Verstappen was a former Formula One driver and his mother Sophie Kumpen was a successful kart racer.\n\nHe made his Formula One debut with Toro Rosso at age seventeen, becoming the youngest driver to start an F1 race. After his move to Red Bull Racing, he became the youngest race winner in Formula One history at the 2016 Spanish Grand Prix.\n\nMax won his first World Championship in 2021 in a dramatic final race, defeating Lewis Hamilton. He went on to dominate the sport in subsequent seasons, winning three more consecutive championships and breaking numerous records. His aggressive driving style and exceptional car control have made him one of the most exciting drivers in the history of the sport.'
    },
    'Kylian Mbappé': {
        'nationality': 'French',
        'born': 'December 20, 1998',
        'net_worth': '$150 Million',
        'known_for': 'Real Madrid, PSG, France national team, 2018 FIFA World Cup winner',
        'bio': 'Kylian Mbappé Lottin is a French professional footballer who plays as a forward for Real Madrid and the France national team. Born in Bondy, a suburb north of Paris, to a Cameroonian father and an Algerian mother, he showed exceptional talent from a very young age.\n\nHe made his professional debut for AS Monaco at age sixteen and quickly established himself as one of the most exciting young players in world football. He helped Monaco win the Ligue 1 title before joining Paris Saint-Germain.\n\nMbappé won the FIFA World Cup with France in 2018 at age nineteen, becoming only the second teenager after Pelé to score in a World Cup final. He has won multiple Ligue 1 titles and was the top scorer in the competition for multiple consecutive seasons. In 2024 he fulfilled his dream of joining Real Madrid, the club he had supported since childhood.'
    },
    'Neymar Jr.': {
        'nationality': 'Brazilian',
        'born': 'February 5, 1992',
        'net_worth': '$200 Million',
        'known_for': 'Barcelona, PSG, Al-Hilal, Brazil national team, skill and flair',
        'bio': 'Neymar da Silva Santos Júnior, known simply as Neymar Jr., is a Brazilian professional footballer widely regarded as one of the most skillful and entertaining players in the world. Born in Mogi das Cruzes, São Paulo, he showed extraordinary talent from childhood.\n\nHe rose to prominence at Santos FC before his move to FC Barcelona where he formed a devastating attacking trio with Lionel Messi and Luis Suárez, winning the UEFA Champions League and multiple other trophies.\n\nHis transfer to Paris Saint-Germain for 222 million euros in 2017 remains the most expensive transfer in football history. Known for his exceptional dribbling, creativity and eye for goal, Neymar has been one of the most exciting players of his generation. He has represented Brazil at multiple FIFA World Cups and is his country\'s all-time leading scorer.'
    },
    'David Beckham': {
        'nationality': 'British',
        'born': 'May 2, 1975',
        'net_worth': '$450 Million',
        'known_for': 'Manchester United, Real Madrid, LA Galaxy, England national team, iconic free kicks',
        'bio': 'David Robert Joseph Beckham OBE is a retired English professional footballer who is one of the most recognizable and globally popular athletes in sports history. Born in Leytonstone, London, he joined the Manchester United academy at age eleven.\n\nHe became a central figure in Manchester United\'s dominance of English football in the 1990s and early 2000s, winning six Premier League titles and the UEFA Champions League. His iconic free kick against Greece in 2001 qualified England for the 2002 World Cup.\n\nAfter spells at Real Madrid, LA Galaxy, AC Milan and Paris Saint-Germain, he has become a global icon of sport and fashion. He co-owns Inter Miami CF in MLS. David and his wife Victoria Beckham are considered one of the most recognizable celebrity couples in the world. He has been awarded the OBE for his services to football.'
    },
    'Mike Tyson': {
        'nationality': 'American',
        'born': 'June 30, 1966',
        'net_worth': '$10 Million',
        'known_for': 'Youngest heavyweight champion, Iron Mike, undisputed heavyweight champion',
        'bio': 'Michael Gerard Tyson, known as Iron Mike, is a retired American professional boxer who is widely regarded as one of the most ferocious and powerful heavyweight champions in boxing history. Born in Brooklyn, New York City, he had a troubled childhood in one of New York\'s toughest neighborhoods.\n\nHe was discovered by legendary trainer Cus D\'Amato and quickly developed into an exceptional talent. At age twenty he became the youngest heavyweight champion in history, winning the WBC title in 1986. He went on to unify the heavyweight championship and was considered the most feared boxer in the world.\n\nDespite personal and professional setbacks, Mike Tyson remains one of the most iconic figures in sports history. He has reinvented himself as a media personality and continues to inspire debate about his place among the all-time greats in boxing. His return to the ring in his fifties demonstrated his enduring appeal and competitive spirit.'
    },
    'Floyd Mayweather Jr.': {
        'nationality': 'American',
        'born': 'February 24, 1977',
        'net_worth': '$450 Million',
        'known_for': 'Undefeated record 50-0, TBE (The Best Ever), five-division world champion',
        'bio': 'Floyd Joy Mayweather Jr. is a retired American professional boxer who compiled an undefeated professional record of 50 wins and 0 losses. Born in Grand Rapids, Michigan, into a boxing family, his father Floyd Mayweather Sr. and uncles Roger and Jeff Mayweather were all professional boxers.\n\nHe won a bronze medal at the 1996 Olympic Games in Atlanta before turning professional. He went on to win world championships in five different weight divisions and is considered by many experts to be the greatest defensive boxer of all time.\n\nFloyd\'s fights against Oscar De La Hoya, Manny Pacquiao and Conor McGregor were some of the highest-grossing combat sports events in history. His fight against Pacquiao in 2015 generated over 600 million dollars in revenue. He is known for his extraordinary financial success and his luxurious lifestyle. He retired with a perfect record and is considered one of the greatest boxers in history.'
    },
    'Conor McGregor': {
        'nationality': 'Irish',
        'born': 'July 14, 1988',
        'net_worth': '$200 Million',
        'known_for': 'UFC Double Champion, Floyd Mayweather bout, Proper Twelve whiskey',
        'bio': 'Conor Anthony McGregor is an Irish professional mixed martial artist, boxer and businessman. Born in Crumlin, Dublin, Ireland, he began training in boxing at age twelve before transitioning to MMA.\n\nHe became the first fighter in UFC history to hold championships in two weight divisions simultaneously, winning the featherweight title in 2015 and the lightweight title in 2016. His trash-talking persona and electrifying fighting style made him one of the sport\'s biggest draws.\n\nIn 2017, McGregor crossed over into boxing to face Floyd Mayweather Jr. in one of the highest-grossing combat sports events in history. Beyond fighting, he founded Proper No. Twelve Irish Whiskey, which he sold for a reported 600 million dollars, making him one of the wealthiest combat sports athletes in history.'
    },
    'Rafael Nadal': {
        'nationality': 'Spanish',
        'born': 'June 3, 1986',
        'net_worth': '$220 Million',
        'known_for': '22 Grand Slam titles, King of Clay, French Open record 14 titles',
        'bio': 'Rafael Nadal Parera is a Spanish professional tennis player who is widely regarded as one of the greatest tennis players of all time. Born in Manacor, Mallorca, he began playing tennis at age three under the guidance of his uncle Toni Nadal.\n\nHe turned professional at age fifteen and quickly established himself as an exceptional talent. His rivalry with Roger Federer is considered the greatest in tennis history and elevated the sport to new heights of popularity worldwide.\n\nRafael has won 22 Grand Slam singles titles, the most in men\'s tennis history. He has won the French Open a record 14 times, earning him the nickname King of Clay. Despite battling injuries throughout his career, he continued to compete at the highest level and retired as one of the most beloved and respected figures in the history of sport.'
    },
    'Novak Djokovic': {
        'nationality': 'Serbian',
        'born': 'May 22, 1987',
        'net_worth': '$220 Million',
        'known_for': '24 Grand Slam titles, most weeks at world number one',
        'bio': 'Novak Djokovic is a Serbian professional tennis player who holds the record for the most Grand Slam singles titles in the history of men\'s tennis with 24 championships. Born in Belgrade, Yugoslavia, he began playing tennis at age four and showed exceptional talent from a young age.\n\nHe turned professional in 2003 and steadily rose through the rankings. His dominance of the sport began in 2011 when he won three Grand Slam titles and reached a record 10 consecutive Grand Slam finals. His rivalry with Roger Federer and Rafael Nadal, known as the Big Three, is considered the golden era of men\'s tennis.\n\nNovak has spent more weeks at world number one than any other player in history. Known for his extraordinary flexibility, mental strength and competitive spirit, he continues to compete at the highest level well into his late thirties. He is a passionate advocate for players\' rights and has also been involved in humanitarian work in his native Serbia.'
    },
    'Roger Federer': {
        'nationality': 'Swiss',
        'born': 'August 8, 1981',
        'net_worth': '$550 Million',
        'known_for': '20 Grand Slam titles, most elegant player, GOAT debates',
        'bio': 'Roger Federer is a retired Swiss professional tennis player who is widely regarded as one of the greatest athletes of all time and arguably the most elegant player in tennis history. Born in Basel, Switzerland, to a Swiss father and South African mother, he showed exceptional coordination and athletic ability from childhood.\n\nHe turned professional in 1998 and won his first Grand Slam title at Wimbledon in 2003. He went on to dominate world tennis for more than a decade, winning 20 Grand Slam singles titles and spending a record 310 weeks at world number one.\n\nRoger\'s playing style, characterized by his fluid footwork, one-handed backhand and tactical genius, is considered the gold standard of tennis technique. His rivalries with Rafael Nadal and Novak Djokovic elevated the sport to new global heights. He retired from professional tennis in 2022 at a Laver Cup ceremony that moved fans and fellow players to tears worldwide.'
    },
    'Tiger Woods': {
        'nationality': 'American',
        'born': 'December 30, 1975',
        'net_worth': '$1.1 Billion',
        'known_for': '15 Major championships, transforming golf, comeback stories',
        'bio': 'Eldrick Tont Woods, known professionally as Tiger Woods, is an American professional golfer who is widely regarded as one of the greatest golfers of all time and one of the most recognizable athletes in the world. Born in Cypress, California, to a Black American father and a Thai mother, he showed prodigious golfing talent from infancy.\n\nHe appeared on The Mike Douglas Show at age two to demonstrate his putting skills and shot 48 for nine holes at age three. He became the youngest Masters champion at age twenty-one and went on to win 15 Major championships, second only to Jack Nicklaus\'s record of 18.\n\nTiger revolutionized golf, bringing unprecedented popularity and athleticism to the sport. His return to competitive golf following multiple surgeries and a devastating car accident in 2021 is considered one of sport\'s most remarkable comeback stories. He has earned over 120 million dollars in tournament winnings and over 1 billion dollars in endorsements.'
    },
    'Usain Bolt': {
        'nationality': 'Jamaican',
        'born': 'August 21, 1986',
        'net_worth': '$90 Million',
        'known_for': 'World\'s fastest man, 100m and 200m world records, eight Olympic gold medals',
        'bio': 'Usain St. Leo Bolt is a retired Jamaican sprinter who is widely considered the greatest sprinter of all time and holds the world records in both the 100 metres and 200 metres. Born in Sherwood Content, Trelawny, Jamaica, he showed exceptional athleticism as a child.\n\nHe burst onto the world stage at the 2008 Beijing Olympics where he won three gold medals and broke three world records, including running the 100m in 9.58 seconds — a record that still stands. He repeated his triple gold at the 2012 London Olympics and 2016 Rio Olympics, becoming the only sprinter to win the 100m and 200m at three consecutive Olympics.\n\nUsain is known for his extraordinary combination of size, power and speed, as his height of 6\'5" defied conventional wisdom about sprinting. His celebration style, featuring his signature Lightning Bolt pose, has become one of the most iconic in sports history. He retired from professional athletics in 2017 after winning 23 World Championship gold medals.'
    },
    "Shaquille O'Neal": {
        'nationality': 'American',
        'born': 'March 6, 1972',
        'net_worth': '$400 Million',
        'known_for': 'Four NBA Championships, Lakers dynasty, Shaq Diesel, dominant center',
        'bio': 'Shaquille Rashaun O\'Neal, known as Shaq, is a retired American professional basketball player who is widely regarded as the most dominant center in NBA history. Born in Newark, New Jersey, he grew to 7\'1" and developed into an exceptional athlete who combined size, power and surprising agility.\n\nHe was selected first overall in the 1992 NBA Draft by the Orlando Magic. After moving to the Los Angeles Lakers, he formed a devastating partnership with Kobe Bryant and won three consecutive NBA championships from 2000 to 2002. He won a fourth championship with the Miami Heat in 2006.\n\nShaq won four NBA championships, three Finals MVP awards and one league MVP award. He was selected to the All-Star Game fifteen times and was named to the All-NBA First Team eight times. Beyond basketball, he has pursued successful careers in music, acting and business, including a PhD in Education. He is a beloved media personality and sports analyst.'
    },
    'Oprah Winfrey': {
        'nationality': 'American',
        'born': 'January 29, 1954',
        'net_worth': '$2.5 Billion',
        'known_for': 'The Oprah Winfrey Show, OWN Network, media mogul, philanthropist',
        'bio': 'Oprah Gail Winfrey is an American talk show host, television producer, actress, author and philanthropist. Born in rural poverty in Kosciusko, Mississippi, she overcame a difficult childhood to become one of the most influential women in the world.\n\nShe began her media career in radio while in high school and co-anchored a local evening news program before moving to daytime talk. The Oprah Winfrey Show launched nationally in 1986 and became the highest-rated television program of its kind in history, running for 25 seasons.\n\nOprah became the first African American female billionaire through her media empire, which includes the OWN Network, Harpo Productions and O magazine. She is also known for her powerful book club, philanthropic work and her presidential Medal of Freedom. Her influence on American culture is immeasurable.'
    },
    'Ellen DeGeneres': {
        'nationality': 'American',
        'born': 'January 26, 1958',
        'net_worth': '$500 Million',
        'known_for': 'The Ellen DeGeneres Show, Finding Nemo, stand-up comedy, LGBTQ advocacy',
        'bio': 'Ellen Lee DeGeneres is an American comedian, television host, actress and author who hosted The Ellen DeGeneres Show for nineteen seasons. Born in Metairie, Louisiana, she began her career in stand-up comedy before breaking into television.\n\nHer sitcom Ellen made history in 1997 when both the character and DeGeneres herself came out as gay in the same episode, the first time a lead character on a primetime television series had come out. The episode, titled The Puppy Episode, was watched by 42 million viewers.\n\nThe Ellen DeGeneres Show, which ran from 2003 to 2022, won 63 Daytime Emmy Awards. She is also known for providing the voice of Dory in Pixar\'s Finding Nemo and Finding Dory. She has received the Presidential Medal of Freedom and the Mark Twain Prize for American Humor for her contributions to comedy and culture.'
    },
    'Kim Kardashian': {
        'nationality': 'American',
        'born': 'October 21, 1980',
        'net_worth': '$1.7 Billion',
        'known_for': 'Keeping Up with the Kardashians, SKIMS, KKW Beauty, criminal justice reform',
        'bio': 'Kimberly Noel Kardashian is an American media personality, socialite, businesswoman and model. Born in Los Angeles, California, she first gained public attention as a friend and stylist of Paris Hilton before becoming a television personality in her own right.\n\nKeeping Up with the Kardashians, which premiered in 2007, became one of the longest-running reality television series and turned the entire Kardashian family into global celebrities. Kim leveraged her fame into multiple successful business ventures.\n\nHer SKIMS shapewear company was valued at over 4 billion dollars, and her KKW Beauty line achieved massive commercial success. Kim has also pursued criminal justice reform, working to free wrongfully incarcerated individuals. She passed the baby bar exam in 2021 and is pursuing a law degree.'
    },
    'Kylie Jenner': {
        'nationality': 'American',
        'born': 'August 10, 1997',
        'net_worth': '$700 Million',
        'known_for': 'Kylie Cosmetics, Keeping Up with the Kardashians, youngest self-made billionaire',
        'bio': 'Kylie Kristen Jenner is an American media personality, socialite and businesswoman who became one of the youngest self-made billionaires in history. Born in Los Angeles, California, the youngest of the Kardashian-Jenner family, she began appearing on Keeping Up with the Kardashians as a child.\n\nShe launched Kylie Cosmetics in 2015 starting with Kylie Lip Kits and rapidly grew the company into a global cosmetics empire. She sold a 51 percent stake to Coty Inc. in 2020 in a deal that valued the company at 1.2 billion dollars.\n\nKylie has become one of the most followed people on Instagram with over 400 million followers. Her business ventures also include Kylie Swim, Kylie Baby and Kylie Skin. She has been recognized by Forbes as one of the most influential figures in business and entertainment.'
    },
    'Kendall Jenner': {
        'nationality': 'American',
        'born': 'November 3, 1995',
        'net_worth': '$60 Million',
        'known_for': 'Supermodel, Keeping Up with the Kardashians, 818 Tequila',
        'bio': 'Kendall Nicole Jenner is an American model and media personality who is one of the most successful models in the world. Born in Los Angeles, California, she began her modeling career at age fourteen, signing with Wilhelmina Models.\n\nShe has walked runways for the world\'s most prestigious fashion houses including Chanel, Givenchy, Dolce and Gabbana, Versace and Fendi. She has graced the covers of Vogue, Harper\'s Bazaar and countless other major fashion magazines.\n\nKendall has been named the highest-paid model in the world multiple times. Beyond modeling, she has launched 818 Tequila, which has become one of the fastest-growing spirits brands in the United States. She continues to appear on the family television franchise and is known for her striking features and her ability to maintain privacy despite her enormous public profile.'
    },
    'Gordon Ramsay': {
        'nationality': 'British',
        'born': 'November 8, 1966',
        'net_worth': '$220 Million',
        'known_for': 'Hell\'s Kitchen, MasterChef, Kitchen Nightmares, three-star Michelin chef',
        'bio': 'Gordon James Ramsay OBE is a British chef, restaurateur, television personality and writer. Born in Johnstone, Scotland, he initially pursued a career in professional football before an injury ended his playing days and he redirected his passion into cooking.\n\nHe trained under some of the world\'s greatest chefs including Marco Pierre White and Joël Robuchon in France. His London restaurant Gordon Ramsay at Royal Hospital Road became the first Scottish restaurant to be awarded three Michelin stars in 2001.\n\nGordon has become one of the most recognizable television personalities in the world through his shows Hell\'s Kitchen, MasterChef, Kitchen Nightmares and The F Word. His fiery kitchen persona combined with his genuine passion for cooking excellence has made him a global icon. His restaurants collectively hold multiple Michelin stars across the world.'
    },
    'Simon Cowell': {
        'nationality': 'British',
        'born': 'October 7, 1959',
        'net_worth': '$600 Million',
        'known_for': 'American Idol, The X Factor, Britain\'s Got Talent, blunt critiques',
        'bio': 'Simon Phillip Cowell is a British talent show judge, television producer and music executive who has become one of the most powerful and recognizable figures in the entertainment industry. Born in Brighton, East Sussex, he began his career in the music industry working in the mailroom at EMI.\n\nHe signed acts including Westlife and Robson and Jerome before transitioning into television. His role as a judge on Pop Idol in the UK and American Idol in the US established him as the most watched and controversial television personality in the world, known for his withering critiques of contestants.\n\nSimon created and produced The X Factor, Britain\'s Got Talent and America\'s Got Talent, discovering artists including One Direction, Susan Boyle and many others. His SYCO Entertainment label has discovered some of the biggest-selling music acts of the 21st century. His net worth, estimated at 600 million dollars, reflects his extraordinary commercial instincts.'
    },
    'MrBeast': {
        'nationality': 'American',
        'born': 'May 7, 1998',
        'net_worth': '$500 Million',
        'known_for': 'YouTube philanthropy, Squid Game recreation, MrBeast Burger, Feastables',
        'bio': 'Jimmy Donaldson, known online as MrBeast, is an American YouTuber, entrepreneur and philanthropist who has become the most subscribed individual creator on YouTube. Born in Greenville, North Carolina, he began posting videos to YouTube at age thirteen.\n\nHe is known for his elaborate stunts, challenges and acts of philanthropy, including giving away millions of dollars to strangers, funding surgeries for people with cataracts and planting twenty million trees through his TeamTrees initiative.\n\nMrBeast has built a media empire that extends beyond YouTube to include MrBeast Burger, a virtual restaurant chain, and Feastables, a chocolate brand that became one of the fastest-growing snack companies in America. He has been recognized as one of the most influential content creators in history and his approach to content creation has fundamentally changed the nature of online entertainment.'
    },
    'Jimmy Fallon': {
        'nationality': 'American',
        'born': 'September 19, 1974',
        'net_worth': '$60 Million',
        'known_for': 'The Tonight Show, Saturday Night Live, celebrity games, lip sync battles',
        'bio': 'James Thomas Fallon is an American comedian, television host, actor, singer and writer who has hosted The Tonight Show Starring Jimmy Fallon since 2014. Born in Brooklyn, New York City, he grew up in Saugerties in upstate New York.\n\nHe joined the cast of Saturday Night Live in 1998 and became one of the show\'s most popular cast members, known for his impressions and his tendency to break character by laughing. He hosted Late Night with Jimmy Fallon from 2009 before moving to The Tonight Show.\n\nFallon has reinvented The Tonight Show for the digital age, creating viral segments including Thank You Notes, Lip Sync Battle and various celebrity games that regularly generate hundreds of millions of views online. He has written several bestselling books and continues to be one of the most beloved figures in late night television.'
    },
    'Trevor Noah': {
        'nationality': 'South African',
        'born': 'February 20, 1984',
        'net_worth': '$100 Million',
        'known_for': 'The Daily Show, stand-up comedy, Born a Crime, South African perspective',
        'bio': 'Trevor Noah is a South African comedian, writer, producer and political commentator who served as the host of The Daily Show on Comedy Central from 2015 to 2022. Born in Johannesburg, South Africa, during the apartheid era, he is the son of a Black Xhosa mother and a White Swiss German father.\n\nHis birth was itself illegal under South African apartheid law, an experience he chronicled in his bestselling memoir Born a Crime, which spent years on the New York Times bestseller list. He began his career as a comedian in South Africa before moving to the United States.\n\nTrevor succeeded Jon Stewart as host of The Daily Show and became one of the most influential voices in American political satire. His international perspective and experience of growing up in South Africa gave him a unique lens through which to analyze American politics and culture. He is also a highly successful stand-up comedian who has performed to sold-out arenas worldwide.'
    },
    'Snoop Dogg': {
        'nationality': 'American',
        'born': 'October 20, 1971',
        'net_worth': '$160 Million',
        'known_for': 'Doggystyle, Drop It Like It\'s Hot, gin and juice, Cannabis brand',
        'bio': 'Calvin Cordozar Broadus Jr., known professionally as Snoop Dogg, is an American rapper, media personality, and businessman who has been one of the most iconic figures in hip hop since the early 1990s. Born in Long Beach, California, he grew up in a musical household and began rapping as a child.\n\nHe was discovered by Dr. Dre and appeared on the landmark album The Chronic in 1992 before releasing his own debut Doggystyle in 1993. The album sold over a million copies in its first week and is considered one of the greatest hip hop albums of all time.\n\nSnoop has evolved from rapper to media empire, hosting television shows, acting in films and building business ventures including a cannabis company, a football league and food products. Known for his laid-back persona and distinctive voice, he served as a commentator for the 2024 Paris Olympics, winning over a new generation of fans with his infectious enthusiasm.'
    },
    'Ice Cube': {
        'nationality': 'American',
        'born': 'June 15, 1969',
        'net_worth': '$160 Million',
        'known_for': 'N.W.A., AmeriKKKa\'s Most Wanted, Friday franchise, Boyz n the Hood',
        'bio': 'O\'Shea Jackson, known professionally as Ice Cube, is an American rapper, actor, filmmaker and businessman who is one of the pioneering figures of West Coast hip hop and gangsta rap. Born in Baldwin Hills, Los Angeles, California, he began rapping as a teenager.\n\nHe rose to fame as a member of the influential and controversial rap group N.W.A., co-writing some of the most provocative and culturally significant hip hop songs of the 1980s. His solo debut AmeriKKKa\'s Most Wanted, released in 1990, is considered one of the greatest hip hop albums ever made.\n\nIce Cube transitioned into acting with critically acclaimed performances in Boyz n the Hood and New Jack City. He wrote and starred in the Friday comedy franchise, which became a beloved film series. He has also established himself as a successful producer and entrepreneur, creating the BIG3 basketball league.'
    },
    '50 Cent': {
        'nationality': 'American',
        'born': 'July 6, 1975',
        'net_worth': '$40 Million',
        'known_for': 'Get Rich or Die Tryin\', In Da Club, Vitamin Water investment, Power TV series',
        'bio': 'Curtis James Jackson III, known professionally as 50 Cent, is an American rapper, actor, businessman and television producer who rose from the streets of South Jamaica, Queens to become one of the best-selling music artists of all time. Born in Queens, New York City, he had a difficult childhood and became involved in drug dealing as a teenager.\n\nAfter being shot nine times in 2000, he emerged with a renewed determination to succeed. His mixtape Guess Who\'s Back caught the attention of Eminem and Dr. Dre who signed him to their labels. His debut album Get Rich or Die Tryin\' sold one million copies in four days.\n\nBeyond music, 50 Cent demonstrated shrewd business instincts by investing early in Vitamin Water, earning an estimated 100 million dollars when the company was acquired by Coca-Cola. He created and produced the hit television series Power and its multiple spinoffs, establishing himself as a major force in television production.'
    },
    'Martha Stewart': {
        'nationality': 'American',
        'born': 'August 3, 1941',
        'net_worth': '$400 Million',
        'known_for': 'Martha Stewart Living, home and lifestyle brand, television host, cookbook author',
        'bio': 'Martha Helen Stewart is an American retail businesswoman, writer, television personality and former model who built a home and lifestyle empire worth hundreds of millions of dollars. Born in Jersey City, New Jersey, she worked as a model before transitioning into catering and publishing.\n\nShe founded Martha Stewart Living Omnimedia and her publications, television programs and merchandise turned her into one of America\'s most recognizable brand names and a symbol of domestic perfection. Her books on cooking, entertaining and home decoration have sold millions of copies.\n\nDespite serving five months in federal prison in 2004, Martha made a remarkable comeback and has continued to expand her brand. She became, at age eighty-one, the oldest person to appear on the cover of Sports Illustrated Swimsuit Issue, demonstrating her enduring cultural relevance and her remarkable ability to reinvent herself.'
    },
    'David Letterman': {
        'nationality': 'American',
        'born': 'April 12, 1947',
        'net_worth': '$400 Million',
        'known_for': 'Late Night with David Letterman, Late Show with David Letterman, top ten lists',
        'bio': 'David Michael Letterman is a retired American television host, comedian, writer and producer who is widely regarded as one of the most influential figures in the history of late-night television. Born in Indianapolis, Indiana, he studied telecommunications at Ball State University.\n\nHe began his career as a local weatherman before moving to Los Angeles to pursue comedy. He hosted Late Night with David Letterman on NBC from 1982 and Late Show with David Letterman on CBS from 1993 to 2015, a combined total of 33 years.\n\nLetterman\'s innovative approach to late-night comedy, including his Top Ten Lists, Stupid Pet Tricks and desk pieces, defined the format for a generation of television hosts. He received numerous Emmy Awards and a Peabody Award for his work. Since retirement, he has hosted the Netflix interview series My Next Guest Needs No Introduction and has become known for his long beard.'
    },
    'Gwyneth Paltrow': {
        'nationality': 'American',
        'born': 'September 27, 1972',
        'net_worth': '$200 Million',
        'known_for': 'Shakespeare in Love, Iron Man, Goop lifestyle brand, wellness entrepreneur',
        'bio': 'Gwyneth Kate Paltrow is an American actress and businesswoman who won the Academy Award for Best Actress for her portrayal of Viola in Shakespeare in Love in 1999. Born in Los Angeles, California, the daughter of director Bruce Paltrow and actress Blythe Danner, she was immersed in the entertainment industry from birth.\n\nAfter starring in numerous critically acclaimed films including Emma, Sliding Doors and The Royal Tenenbaums, she joined the Marvel Cinematic Universe as Pepper Potts in the Iron Man franchise.\n\nIn 2008 Gwyneth founded the lifestyle brand Goop, which has grown into a highly controversial yet commercially successful wellness empire worth hundreds of millions of dollars. Known for her willingness to embrace unconventional wellness practices and her authentic voice, she has become one of the most recognizable figures at the intersection of celebrity and lifestyle.'
    },
    'Steve Harvey': {
        'nationality': 'American',
        'born': 'January 17, 1957',
        'net_worth': '$200 Million',
        'known_for': 'Family Feud, The Steve Harvey Morning Show, stand-up comedy, Act Like a Lady',
        'bio': 'Broderick Stephen Harvey is an American comedian, television host, actor, author and entrepreneur who is one of the most successful entertainers in America. Born in Welch, West Virginia, he had a difficult childhood that included a period of homelessness before his comedy career took off.\n\nHe was a successful stand-up comedian and starred in The Steve Harvey Show from 1996 to 2002. His nationally syndicated Steve Harvey Morning Show has millions of listeners and his hosting of Family Feud revitalized the show, making it one of the highest-rated game shows on American television.\n\nSteve is also a bestselling author, his book Act Like a Lady, Think Like a Man spending 100 weeks on the New York Times bestseller list and being adapted into a successful film. He is known for his family-friendly humor, his commitment to mentoring young men and his philanthropic work through the Steve and Marjorie Harvey Foundation.'
    },
    'Jamie Foxx': {
        'nationality': 'American',
        'born': 'December 13, 1967',
        'net_worth': '$170 Million',
        'known_for': 'Ray, Django Unchained, Ali, The Amazing Spider-Man 2',
        'bio': 'Eric Marlon Bishop, known professionally as Jamie Foxx, is an American actor, comedian, singer and musician who is one of the most versatile entertainers in Hollywood. Born in Terrell, Texas, he began performing stand-up comedy while in college.\n\nHe joined the cast of the sketch comedy series In Living Color before starring in his own sitcom The Jamie Foxx Show. His dramatic portrayal of Ray Charles in the 2004 biopic Ray earned him the Academy Award for Best Actor, making him only the second person to receive acting nominations in multiple categories at the same ceremony.\n\nJamie has demonstrated his versatility across comedy, drama and music. His albums including Unpredictable have produced hit singles and demonstrated his genuine musical talent. He is also a gifted impressionist and pianist. After a serious medical emergency in 2023, his remarkable recovery and return to work inspired millions of fans worldwide.'
    },
    'Nick Cannon': {
        'nationality': 'American',
        'born': 'October 8, 1980',
        'net_worth': '$20 Million',
        'known_for': 'Wild \'N Out, America\'s Got Talent, The Masked Singer host, Mariah Carey marriage',
        'bio': 'Nicholas Scott Cannon is an American comedian, rapper, actor, television personality and music executive who has become one of the most ubiquitous personalities on American television. Born in San Diego, California, he began performing stand-up comedy as a teenager.\n\nHe got his start in the entertainment industry on All That before creating and starring in the hit improv comedy series Wild \'N Out, which has run for numerous seasons on MTV and VH1. He hosted America\'s Got Talent and later became the host of The Masked Singer.\n\nNick has also pursued a music career and has been involved in various entrepreneurial ventures. He is also known for his high-profile marriage to Mariah Carey, with whom he has twins. He continues to be one of the most prolific entertainers in American television, often hosting multiple shows simultaneously.'
    },
    'Paris Hilton': {
        'nationality': 'American',
        'born': 'February 17, 1981',
        'net_worth': '$300 Million',
        'known_for': 'The Simple Life, heiress, DJ, entrepreneur, That\'s Hot catchphrase',
        'bio': 'Paris Whitney Hilton is an American media personality, socialite, businesswoman, model, actress and DJ who is considered one of the original modern celebrities — famous largely for being famous. Born in New York City, the great-granddaughter of hotel magnate Conrad Hilton, she grew up in one of America\'s wealthiest families.\n\nShe became a fixture of celebrity culture in the early 2000s and her reality television series The Simple Life with Nicole Richie became a massive cultural phenomenon. Her catchphrase That\'s Hot entered the popular lexicon.\n\nBeyond her celebrity persona, Paris has built a remarkable business empire spanning fragrances, clothing lines, nightclub appearances and DJing, with annual revenues reportedly exceeding 100 million dollars. Her candid documentary This Is Paris revealed a more complex person beneath the carefully constructed public image. She has become an advocate against institutional child abuse and continues to evolve as a businesswoman.'
    },
    'Roman Reigns': {
        'nationality': 'American',
        'born': 'May 25, 1985',
        'net_worth': '$12 Million',
        'known_for': 'Universal Champion, The Tribal Chief, The Head of the Table, Bloodline storyline',
        'bio': 'Leati Joseph Anoa\'i, known professionally as Roman Reigns, is an American professional wrestler and former American football player. Born in Pensacola, Florida, he comes from the legendary Anoa\'i wrestling dynasty, with his father Sika Anoa\'i and cousins The Usos and The Rock also being professional wrestlers.\n\nHe played college football at Georgia Tech and briefly played in the NFL before transitioning to professional wrestling. He signed with WWE in 2010 and trained at their developmental territory before debuting on the main roster as part of The Shield in 2012.\n\nRoman became one of WWE\'s most dominant champions, holding the Universal Championship and later the WWE Championship simultaneously as the Undisputed WWE Universal Champion for over 1300 days. His character evolution into The Tribal Chief and Head of the Table is widely considered one of the greatest character transformations in wrestling history.'
    },
    'John Cena': {
        'nationality': 'American',
        'born': 'April 23, 1977',
        'net_worth': '$60 Million',
        'known_for': 'You Can\'t See Me, 16-time World Champion, Never Give Up, Make-A-Wish record',
        'bio': 'John Felix Anthony Cena is an American professional wrestler, actor and television presenter. Born in West Newbury, Massachusetts, he studied exercise physiology at Springfield College before pursuing a career in bodybuilding and wrestling.\n\nHe signed with WWE in 2001 and became one of the company\'s most recognizable faces, winning a record-tying 16 world championships. Known for his Never Give Up motto and his tremendous work with the Make-A-Wish Foundation — having granted over 650 wishes — he became one of wrestling\'s most beloved figures.\n\nCena successfully transitioned into acting, starring in films such as The Marine, Trainwreck, Blockers and The Suicide Squad. He also hosted the reality show Are You Smarter Than a 5th Grader. His portrayal of Peacemaker in the DC series of the same name earned him significant critical praise. He announced his retirement from wrestling in 2025.'
    },
    'Randy Orton': {
        'nationality': 'American',
        'born': 'April 1, 1980',
        'net_worth': '$11 Million',
        'known_for': 'The Viper, RKO, 14-time World Champion, Legend Killer',
        'bio': 'Randal Keith Orton, known professionally as Randy Orton, is an American professional wrestler and third-generation wrestler. Born in Knoxville, Tennessee, into a wrestling family — his father Bob Orton Jr. and grandfather Bob Orton Sr. were both professional wrestlers.\n\nHe joined WWE in 2001 and became the youngest world champion in WWE history when he won the World Heavyweight Championship at age twenty-four. He became one of the most reliable and respected performers in the company over a career spanning more than two decades.\n\nRandy is known for his distinctive ring style, his devastating RKO finishing move and his ability to convincingly portray both heroic and villainous characters. His fourteen world championship reigns place him among the most decorated wrestlers in WWE history. His return from a serious spinal injury in 2023 was one of the most emotional moments in recent WWE history.'
    },
    'Cody Rhodes': {
        'nationality': 'American',
        'born': 'June 30, 1985',
        'net_worth': '$10 Million',
        'known_for': 'WWE Undisputed Champion, The American Nightmare, finishing the story',
        'bio': 'Cody Garrett Runnels Rhodes is an American professional wrestler and second-generation wrestler. Born in Marietta, Georgia, the son of legendary wrestler Dusty Rhodes, he was immersed in professional wrestling from birth.\n\nHe began his WWE career in 2007 and had success as a tag team and mid-card performer before departing to establish himself as a top-level performer on the independent circuit and in AEW, where he was a founder and Executive Vice President.\n\nHis return to WWE in 2022 began one of the most emotionally resonant storylines in modern wrestling. His quest to win the WWE Championship and "finish the story" his father started captivated audiences worldwide. He won the Undisputed WWE Championship at WrestleMania 40 in 2024 in one of the most celebrated moments in recent wrestling history. He is known for his exceptional promo ability and his genuine passion for the business of professional wrestling.'
    },
    'Seth Rollins': {
        'nationality': 'American',
        'born': 'May 28, 1986',
        'net_worth': '$9 Million',
        'known_for': 'The Visionary, World Heavyweight Champion, The Shield, innovative ring work',
        'bio': 'Colby Daniel Lopez, known professionally as Seth Rollins, is an American professional wrestler who is widely regarded as one of the most gifted performers in modern professional wrestling. Born in Buffalo, Iowa, he trained extensively before signing with WWE.\n\nHe debuted on the main roster as part of The Shield alongside Roman Reigns and Dean Ambrose in 2012. The faction became one of the most popular in WWE history. He became the first person to cash in the Money in the Bank contract at WrestleMania when he won the WWE World Heavyweight Championship in 2015.\n\nSeth is known for his extraordinary athleticism, his innovative ring work incorporating moves from various wrestling styles, and his ability to perform at an elite level in any type of match. He has held multiple world championships and is considered by many to be the most complete in-ring performer of his generation. His showmanship and unique entrance music have made him one of WWE\'s most recognizable personalities.'
    },
    'Drew McIntyre': {
        'nationality': 'Scottish',
        'born': 'June 6, 1985',
        'net_worth': '$5 Million',
        'known_for': 'WWE Champion, The Scottish Warrior, Claymore Kick, pandemic champion',
        'bio': 'Andrew McLean Galloway IV, known professionally as Drew McIntyre, is a Scottish professional wrestler who became the first Scottish-born WWE Champion in the company\'s history. Born in Ayr, Scotland, he was drawn to wrestling from a young age and trained extensively before signing with WWE.\n\nHe was personally signed by Vince McMahon and designated as a future star of the company. After an initial run that did not fulfill expectations, he was released from WWE in 2014. He used this setback as motivation to reinvent himself on the independent circuit, developing the skills and character that would eventually make him a world champion.\n\nHis triumphant return to WWE led to him winning the WWE Championship at WrestleMania 36 in 2020, the first WrestleMania held without a live audience due to the pandemic. His journey from being fired to becoming champion is one of the most inspiring comeback stories in wrestling history.'
    },
    'CM Punk': {
        'nationality': 'American',
        'born': 'October 26, 1978',
        'net_worth': '$12 Million',
        'known_for': 'Pipe Bomb promo, WWE Champion, straight-edge lifestyle, MMA career',
        'bio': 'Phillip Jack Brooks, known professionally as CM Punk, is an American professional wrestler who is widely regarded as one of the most talented microphone performers and overall wrestlers of his generation. Born in Chicago, Illinois, he trained on the independent circuit for years before signing with WWE.\n\nHis famous Pipe Bomb promo in 2011, in which he appeared to break kayfabe and speak candidly about WWE\'s business practices, is considered one of the greatest promos in wrestling history and elevated him to main event status. He held the WWE Championship for 434 days, one of the longest reigns in modern history.\n\nAfter departing WWE in 2014, he competed in MMA before returning to professional wrestling with AEW in 2021. His return to WWE in 2023 was one of the most anticipated moments in recent wrestling history. Known for his straight-edge lifestyle, his authenticity and his complex relationship with the wrestling business, he remains one of the most compelling figures in the industry.'
    },
    'Jey Uso': {
        'nationality': 'American',
        'born': 'August 22, 1985',
        'net_worth': '$3 Million',
        'known_for': 'Yeet!, WWE Tag Team Champion, The Bloodline, Main Event Jey Uso',
        'bio': 'Joshua Samuel Fatu, known professionally as Jey Uso, is an American professional wrestler and member of the legendary Anoa\'i wrestling dynasty. Born in San Francisco, California, he is the son of Rikishi and the twin brother of Jimmy Uso.\n\nJey debuted in WWE alongside his brother as The Usos, and the pair became one of the most decorated tag teams in WWE history with multiple championship reigns. His character development within the Bloodline storyline elevated him to a new level of fan appreciation.\n\nHis emotional and compelling performance within the Bloodline family storyline, particularly his complex relationship with his cousin Roman Reigns and later his opposition to him, made him one of the most popular performers in WWE. His catchphrase Yeet became a worldwide phenomenon embraced by fans of all ages. He won his first world championship in 2024 and is considered one of the most beloved figures in modern wrestling.'
    },
    'Jimmy Uso': {
        'nationality': 'American',
        'born': 'August 22, 1985',
        'net_worth': '$3 Million',
        'known_for': 'WWE Tag Team Champion, The Bloodline, Usos\' Hall of Fame tag team career',
        'bio': 'Jonathan Solofa Fatu, known professionally as Jimmy Uso, is an American professional wrestler and member of the legendary Anoa\'i wrestling dynasty. Born in San Francisco, California, he is the son of Rikishi and the twin brother of Jey Uso.\n\nJimmy and his brother Jey debuted as The Usos in WWE and became one of the most successful and entertaining tag teams in company history, winning the tag team championships numerous times across both Raw and SmackDown.\n\nHis role in the Bloodline storyline allowed him to demonstrate new dimensions of his character, particularly his complex relationship with Roman Reigns. His marriage to Naomi and his genuine chemistry with his brother have made him one of the most beloved figures in WWE. The Usos are considered one of the greatest tag teams in professional wrestling history.'
    },
    'The Undertaker': {
        'nationality': 'American',
        'born': 'March 24, 1965',
        'net_worth': '$17 Million',
        'known_for': 'The Deadman, WrestleMania streak 21-1, 7-time World Champion, 30-year career',
        'bio': 'Mark William Calaway, known professionally as The Undertaker, is a retired American professional wrestler who is widely regarded as one of the greatest and most iconic performers in the history of professional wrestling. Born in Houston, Texas, he began his wrestling career in 1984.\n\nHe joined WWE in 1990 and quickly established his supernatural Deadman persona. Over a thirty-year career, he became the most iconic character in WWE history, winning seven world championships and creating one of the most legendary streaks in sports entertainment — going undefeated at WrestleMania for 21 consecutive years.\n\nThe Undertaker is known for his commanding presence, his ability to reinvent his character multiple times over three decades and his genuine dedication to maintaining his mystique. His farewell ceremony in the Boneyard at WrestleMania 36 and his subsequent retirement and Hall of Fame induction were celebrated by fans worldwide as the end of a truly irreplaceable era in professional wrestling.'
    },
    'Triple H': {
        'nationality': 'American',
        'born': 'July 27, 1969',
        'net_worth': '$50 Million',
        'known_for': 'The Game, 14-time World Champion, D-Generation X, WWE Chief Content Officer',
        'bio': 'Paul Michael Levesque, known professionally as Triple H, is an American professional wrestling executive, businessman and retired professional wrestler. Born in Nashua, New Hampshire, he trained in professional wrestling as a teenager and worked his way through the independent circuit before signing with WWF.\n\nHe became one of the most dominant champions in WWE history, winning the world title fourteen times and feuding with virtually every major star of his era. His stable D-Generation X was one of the most popular and controversial in WWE history. His ring name evolved from Hunter Hearst Helmsley to Triple H.\n\nAfter transitioning from in-ring competition, Triple H became the Executive Vice President of Talent, Live Events and Creative for WWE. Following the retirement of Vince McMahon, he was named Chief Content Officer and has been credited with revitalizing WWE\'s creative direction, bringing back beloved performers and creating compelling storylines that have restored fan confidence in the product.'
    },
    'Shawn Michaels': {
        'nationality': 'American',
        'born': 'July 22, 1965',
        'net_worth': '$17 Million',
        'known_for': 'Mr. WrestleMania, Heartbreak Kid, Sweet Chin Music, D-Generation X',
        'bio': 'Michael Shawn Hickenbottom, known professionally as Shawn Michaels, is a retired American professional wrestler who is universally regarded as one of the greatest professional wrestlers of all time. Born in Chandler, Arizona, he began wrestling in his teenage years and quickly developed a reputation as an exceptional talent.\n\nHe won the Intercontinental Championship, the WWF Championship and the World Heavyweight Championship multiple times throughout his career. His WrestleMania matches are legendary in the industry — his matches against the Undertaker at WrestleMania 25 and 26 are frequently cited as among the greatest matches in wrestling history.\n\nShawn retired in 2010 after losing to The Undertaker but returned for one final match in 2018. Known for his ring psychology, his ability to tell stories in the ring, his charismatic character work and his Christian faith which transformed his personal life, he is considered the benchmark by which all performers in his industry are measured.'
    },
    'Brock Lesnar': {
        'nationality': 'American',
        'born': 'July 12, 1977',
        'net_worth': '$25 Million',
        'known_for': 'The Beast Incarnate, UFC Heavyweight Champion, conquering The Undertaker\'s streak',
        'bio': 'Brock Edward Lesnar is an American professional wrestler, former professional mixed martial artist and former American football player who is considered one of the most physically imposing and athletically gifted performers in combat sports history. Born in Webster, South Dakota, he was an exceptional amateur wrestler at the University of Minnesota.\n\nHe won the NCAA Division I wrestling championship in 2000 before signing with WWE. He became one of the most dominant WWE Champions of his era before departing to pursue an NFL career and later entering MMA. He won the UFC Heavyweight Championship in 2008 despite having limited professional MMA experience.\n\nBrock returned to WWE and became a part-time performer whose appearances were treated as genuine events. His victory over The Undertaker at WrestleMania XXX, ending the legendary 21-match streak, is considered one of the most shocking moments in wrestling history. His combination of genuine athletic credentials and entertainment charisma make him unique in professional wrestling.'
    },
    'AJ Styles': {
        'nationality': 'American',
        'born': 'June 2, 1977',
        'net_worth': '$6 Million',
        'known_for': 'The Phenomenal One, WWE Champion, TNA World Champion, global wrestling career',
        'bio': 'Allen Neal Jones, known professionally as AJ Styles, is an American professional wrestler who is widely regarded as one of the greatest professional wrestlers of all time. Born in Jacksonville, North Carolina, he began his wrestling career in 1998 on the independent circuit.\n\nHe spent years establishing himself as a world-class talent in various promotions before becoming the cornerstone of TNA Impact Wrestling where he won multiple world championships. His global career also included acclaimed runs in New Japan Pro-Wrestling where he won the IWGP Heavyweight Championship.\n\nHe signed with WWE in 2016 at age thirty-eight, an age when many wrestlers are winding down their careers, and went on to have arguably the greatest run of his career, winning multiple world championships. Known for his innovative offense, his exceptional ring psychology and his ability to perform at an elite level well into his forties, he is considered The Phenomenal One and a true legend of professional wrestling.'
    },
    'Rey Mysterio': {
        'nationality': 'American',
        'born': 'December 11, 1974',
        'net_worth': '$10 Million',
        'known_for': 'The Master of the 619, luchador mask, World Heavyweight Champion',
        'bio': 'Oscar Gutierrez, known professionally as Rey Mysterio, is an American-Mexican professional wrestler who is widely regarded as one of the greatest luchadors in wrestling history and one of the most beloved performers of his generation. Born in Chula Vista, California, to a Mexican family, he began training under his uncle Rey Mysterio Sr. as a teenager.\n\nHe began his career in Mexico and established himself as a sensational talent before signing with WCW where his masked, high-flying style captivated American audiences. After WCW\'s closure, he joined WWE where he became the first luchador to win the World Heavyweight Championship.\n\nRey is known for his spectacular aerial offense, his iconic mask, and his ability to have extraordinary matches with opponents of all sizes despite being smaller than most of his competitors. His crossover popularity transcended wrestling and his merchandise is among the best-selling in WWE history. He continues to perform at an extraordinary level well into his late forties.'
    },
    'Dominik Mysterio': {
        'nationality': 'American',
        'born': 'April 5, 2001',
        'net_worth': '$2 Million',
        'known_for': 'Dirty Dom, NXT North American Champion, The Judgment Day, turning heel on Rey',
        'bio': 'Dominik Mysterio is an American professional wrestler and the son of legendary luchador Rey Mysterio. Born in San Diego, California, he grew up around professional wrestling and was introduced to WWE audiences as a child when he appeared in storylines involving his father.\n\nHe signed with WWE and trained extensively before making his in-ring debut. His character evolution from a young babyface working alongside his father to a villainous heel who betrayed Rey Mysterio is considered one of the most effective character turns in recent WWE history.\n\nAs a member of The Judgment Day alongside Rhea Ripley, Finn Bálor and Damian Priest, Dominik has thrived as a heel character known for his cowardly mannerisms and his controversial actions. His natural charisma and his famous last name give him a unique platform to establish his own legacy in professional wrestling separate from, though always connected to, his father\'s legendary career.'
    },
    'LA Knight': {
        'nationality': 'American',
        'born': 'October 2, 1983',
        'net_worth': '$2 Million',
        'known_for': 'Yeah!, The Megastar, United States Champion, fan favorite promo ability',
        'bio': 'Shaun Ricker, known professionally as LA Knight, is an American professional wrestler who has become one of the most organically over performers in modern WWE through his exceptional promo ability and magnetic personality. Born in Carrollton, Georgia, he trained extensively and worked for years on the independent circuit before eventually signing with WWE.\n\nAfter years of working in various capacities including a spell as a producer, he was given an opportunity to perform on television that he seized emphatically. His character, an arrogant but confident and supremely entertaining Megastar, combined with his catchphrase Yeah and his genuine connection with live audiences made him one of WWE\'s most popular acts.\n\nLA Knight became the United States Champion and continues to be one of the loudest crowd reactions in WWE. His journey to success in WWE after years of perseverance has made him an inspiring figure for aspiring professional wrestlers everywhere.'
    },
    'Gunther': {
        'nationality': 'Austrian',
        'born': 'April 1, 1988',
        'net_worth': '$2 Million',
        'known_for': 'Intercontinental Champion record reign, Ring General, brutal chops, World Heavyweight Champion',
        'bio': 'Ludwig Kaiser, known professionally as Gunther, is an Austrian professional wrestler who is widely regarded as one of the most credible and dominant wrestling characters in modern WWE. Born in Vienna, Austria, he trained in professional wrestling in Europe and became one of the top performers on the European independent circuit.\n\nHe signed with WWE and competed in NXT UK where he quickly established himself as the most dominant champion in the brand\'s history. He joined the main roster as Gunther and won the Intercontinental Championship, holding it for 666 days in one of the longest championship reigns in modern WWE history.\n\nGunther is known for his devastating chops, his old-school presentation and his ability to create a genuine aura of dominance and credibility rare in modern sports entertainment. His World Heavyweight Championship reign has further cemented his status as one of WWE\'s premier stars. He is widely considered the best pure wrestler on the WWE roster.'
    },
    'Damian Priest': {
        'nationality': 'American',
        'born': 'November 25, 1982',
        'net_worth': '$2 Million',
        'known_for': 'World Heavyweight Champion, The Judgment Day, The Archer of Infamy',
        'bio': 'Luis Martinez, known professionally as Damian Priest, is an American professional wrestler who has become one of WWE\'s most prominent performers as a member of the villainous faction The Judgment Day. Born in New York City to Puerto Rican parents, he trained in professional wrestling and worked the independent circuit for many years.\n\nHe signed with WWE and competed in NXT where he developed his gothic rock-inspired character. After moving to the main roster, he joined The Judgment Day alongside Rhea Ripley, Finn Bálor and later Dominik Mysterio and JD McDonagh.\n\nDamian won the World Heavyweight Championship by cashing in his Money in the Bank contract at WrestleMania XL and went on to have a successful reign as champion. Known for his imposing physical presence, his distinctive look and his genuine connection with fans, he has established himself as a main event performer in WWE.'
    },
    'Finn Bálor': {
        'nationality': 'Irish',
        'born': 'July 25, 1981',
        'net_worth': '$3 Million',
        'known_for': 'First Universal Champion, The Demon, The Judgment Day, NXT founder',
        'bio': 'Fergal Devitt, known professionally as Finn Bálor, is an Irish professional wrestler who made history as the first ever Universal Champion in WWE history. Born in Bray, County Wicklow, Ireland, he trained at the Irish Wrestling Association before beginning his professional career.\n\nHe spent years in Japan working for New Japan Pro-Wrestling where he became a beloved figure and won multiple championships including the IWGP Junior Heavyweight Championship. He signed with WWE and was instrumental in establishing NXT as a premier brand, winning the NXT Championship.\n\nFinn\'s alter ego The Demon, featuring elaborate body paint and a ferocious in-ring performance, is one of the most visually striking characters in professional wrestling. As a member of The Judgment Day, he found renewed success on the main roster. He is considered one of the most talented and versatile performers in the history of professional wrestling.'
    },
    'Bianca Belair': {
        'nationality': 'American',
        'born': 'April 9, 1989',
        'net_worth': '$3 Million',
        'known_for': 'The EST of WWE, Raw Women\'s Champion, WrestleMania main event, iconic braid',
        'bio': 'Bianca Blair Belair is an American professional wrestler and former track and field athlete who has become one of the most celebrated performers in WWE history. Born in Knoxville, Tennessee, she was an exceptional athlete who competed in track and field at the University of Tennessee.\n\nAfter a successful collegiate athletic career, she signed with WWE and quickly established herself as one of the most physically gifted performers in the company. Her combination of athletic ability, charisma and her signature silver braid which she uses as a weapon made her stand out immediately.\n\nBianca won the SmackDown Women\'s Championship at WrestleMania 37 in a highly praised match against Sasha Banks that became the first WrestleMania main event between two Black women. She has held multiple championships and her authentic, positive personality has made her one of WWE\'s most beloved ambassadors both in and out of the ring.'
    },
    'Rhea Ripley': {
        'nationality': 'Australian',
        'born': 'October 8, 1996',
        'net_worth': '$2 Million',
        'known_for': 'Mami, World Women\'s Champion, The Judgment Day, dominant reign',
        'bio': 'Demi Bennett, known professionally as Rhea Ripley, is an Australian professional wrestler who has become one of the most dominant and popular performers in WWE history. Born in Adelaide, South Australia, she began training in professional wrestling as a teenager.\n\nShe signed with WWE and competed in NXT where she became one of the brand\'s most compelling performers, developing her character from a rebellious tough girl into the commanding Mami persona. Her partnership with The Judgment Day and her relationship with Dominik Mysterio became one of WWE\'s most entertaining ongoing storylines.\n\nRhea held the Women\'s World Championship for over a year in one of the most dominant championship reigns in modern WWE history. Known for her intensity, her genuine physicality and her connection with fans, she has been recognized by multiple publications as one of the most valuable performers on WWE\'s roster. Her journey from relative unknown to global star has been one of wrestling\'s most compelling stories.'
    },
    'Becky Lynch': {
        'nationality': 'Irish',
        'born': 'January 30, 1987',
        'net_worth': '$6 Million',
        'known_for': 'The Man, SmackDown Women\'s Champion, Raw Women\'s Champion, WrestleMania main event',
        'bio': 'Rebecca Quin, known professionally as Becky Lynch, is an Irish professional wrestler who has become one of the most popular and respected performers in WWE history. Born in Limerick, Ireland, she trained in professional wrestling as a teenager and spent years on the independent circuit before signing with WWE.\n\nHer most significant moment came in 2018 when she turned against her friend Charlotte Flair and her character The Man was born. The organic and passionate fan support for her character pushed WWE to make her the first woman to main event WrestleMania, which she did by simultaneously holding and defending both the Raw and SmackDown Women\'s Championships.\n\nBecky has been a trailblazer for women in professional wrestling, her journey from struggling independent performer to WWE\'s most popular female star inspiring countless aspiring wrestlers worldwide. Her marriage to Seth Rollins and the birth of their daughter have added new dimensions to her public persona while she continues to perform at an elite level.'
    },
    'Charlotte Flair': {
        'nationality': 'American',
        'born': 'April 5, 1986',
        'net_worth': '$2 Million',
        'known_for': 'The Queen, 14-time Women\'s Champion, daughter of Ric Flair, Figure Eight',
        'bio': 'Ashley Elizabeth Fliehr, known professionally as Charlotte Flair, is an American professional wrestler and second-generation wrestler who has become one of the most decorated women\'s champions in WWE history. Born in Charlotte, North Carolina, the daughter of legendary wrestler Ric Flair, she grew up around professional wrestling but initially pursued a career in volleyball.\n\nShe signed with WWE after pursuing other professional sports and quickly developed into an exceptional performer with her combination of athleticism, natural charisma and famous last name. She was central to the Women\'s Evolution movement in WWE alongside Becky Lynch, Sasha Banks and Bayley.\n\nCharlotte has won the Women\'s Championship fourteen times across both Raw and SmackDown, making her the most decorated women\'s champion in company history. Known for her technical wrestling ability, her commanding presence and her ability to deliver memorable performances in high-profile matches, she has earned the title of The Queen and cemented her place among the all-time greats of women\'s wrestling.'
    },
    'Liv Morgan': {
        'nationality': 'American',
        'born': 'June 8, 1994',
        'net_worth': '$2 Million',
        'known_for': 'SmackDown Women\'s Champion, Obsession character, Women\'s World Champion',
        'bio': 'Gionna Jene Daddio, known professionally as Liv Morgan, is an American professional wrestler who has become one of WWE\'s most popular and authentically lovable performers. Born in Elmwood Park, New Jersey, she signed with WWE at a young age and trained in their developmental system.\n\nAfter years of hard work and multiple character reinventions, Liv broke through as a solo performer and captured her first SmackDown Women\'s Championship. Her genuine enthusiasm for professional wrestling and her authentic connection with fans made her one of the most popular women on the roster.\n\nShe held the Women\'s World Championship and developed a villainous obsession character with Dominik Mysterio that allowed her to demonstrate new dimensions of her personality. Known for her high-energy performances, her acrobatic offense and her genuine love for the craft of professional wrestling, she has become one of WWE\'s most valuable female performers.'
    },
    'Bayley': {
        'nationality': 'American',
        'born': 'June 15, 1989',
        'net_worth': '$2 Million',
        'known_for': 'The Role Model, Hugger character, SmackDown Women\'s Champion, Four Horsewomen',
        'bio': 'Pamela Rose Martinez, known professionally as Bayley, is an American professional wrestler who has become one of WWE\'s most beloved and versatile performers. Born in San Jose, California, she grew up as a passionate wrestling fan and began training to become a wrestler as a teenager.\n\nShe joined WWE\'s developmental territory NXT where her enthusiastic hugger character connecting with the audience on a deeply emotional level made her one of NXT\'s most beloved figures. Her NXT Women\'s Championship matches, particularly her two matches with Sasha Banks, are considered among the greatest women\'s matches in WWE history.\n\nAfter transitioning to the main roster, Bayley reinvented herself as The Role Model, an arrogant and selfish heel character that allowed her to demonstrate new comedic and dramatic abilities. She has won multiple women\'s championships and her journey from wide-eyed fan to main event performer is one of WWE\'s most inspiring stories.'
    },
    'Alexa Bliss': {
        'nationality': 'American',
        'born': 'August 9, 1991',
        'net_worth': '$3 Million',
        'known_for': 'Five Feet of Fury, Raw Women\'s Champion, supernatural character, former fitness competitor',
        'bio': 'Alexis Kaufman, known professionally as Alexa Bliss, is an American professional wrestler and former fitness competitor who has become one of WWE\'s most versatile and entertaining performers. Born in Columbus, Ohio, she was a competitive cheerleader, softball player and fitness competitor before signing with WWE.\n\nShe developed her Little Miss Bliss character and quickly established herself as an exceptional promo performer with an ability to generate heel heat that belied her diminutive size. She won the SmackDown and Raw Women\'s Championships and became one of the most decorated champions in the women\'s division.\n\nHer supernatural character evolution involving the Fiend character allowed her to demonstrate an entirely different and more complex side of her personality that resonated with audiences. Known for her exceptional character work, her expressive facial expressions and her genuine dedication to continuously evolving her character, she remains one of WWE\'s most recognizable female performers.'
    },
    'Iyo Sky': {
        'nationality': 'Japanese',
        'born': 'March 26, 1990',
        'net_worth': '$1 Million',
        'known_for': 'WWE Women\'s Champion, Damage CTRL, aerial offense, Japanese wrestling background',
        'bio': 'Yoshiko Iida, known professionally as Iyo Sky, is a Japanese professional wrestler who is widely regarded as one of the most technically gifted female wrestlers in the world. Born in Tochigi, Japan, she began her wrestling career in Japan where she competed for numerous promotions and established herself as an exceptional talent.\n\nShe signed with WWE and competed in NXT before moving to the main roster where she joined the Damage CTRL faction alongside Bayley and Dakota Kai. Her exceptional aerial offense and her technical wrestling ability make her stand out in a crowded women\'s division.\n\nIyo won the WWE Women\'s Championship by defeating Bianca Belair in a memorable moment at SummerSlam 2023. Her championship reign demonstrated her ability to perform at the highest level and her unique presentation as a character has made her one of WWE\'s most distinctive performers. She is considered a future Hall of Famer by many in the wrestling community.'
    },
    'Asuka': {
        'nationality': 'Japanese',
        'born': 'September 26, 1981',
        'net_worth': '$2 Million',
        'known_for': 'The Empress of Tomorrow, undefeated streak, Raw Women\'s Champion, colorful persona',
        'bio': 'Kanako Urai, known professionally as Asuka, is a Japanese professional wrestler who is widely regarded as one of the greatest women\'s wrestlers in the world. Born in Osaka, Japan, she had a career as a graphic designer and competed in amateur wrestling before pursuing professional wrestling.\n\nShe competed extensively in Japan before signing with WWE and competing in NXT where she established an undefeated streak lasting over 500 days, one of the longest in company history. Her combination of legitimate athletic credentials, colorful fashion and unpredictable personality made her one of NXT\'s most compelling figures.\n\nAsuka has won both the Raw and SmackDown Women\'s Championships and her resilience and longevity in a physically demanding profession are testaments to her exceptional athleticism. Known for her emotional expressiveness, her genuine love of fashion and her authentic personality, she remains one of WWE\'s most beloved performers among hardcore fans worldwide.'
    },
    'Nia Jax': {
        'nationality': 'American',
        'born': 'May 29, 1984',
        'net_worth': '$2 Million',
        'known_for': 'The Irresistible Force, Raw Women\'s Champion, member of Anoa\'i family, dominant style',
        'bio': 'Lina Fanene, known professionally as Nia Jax, is an American professional wrestler and member of the legendary Anoa\'i wrestling dynasty. Born in San Jose, California, she is a cousin of Roman Reigns and Dwayne Johnson through the famous Samoan wrestling family.\n\nBefore professional wrestling, she worked as a model and appeared in various media. She signed with WWE and developed her Irresistible Force character, a dominant powerhouse who uses her size and strength to overwhelm opponents.\n\nNia won the Raw Women\'s Championship and has been known for her physical style and her ability to tell compelling underdog versus dominant monster stories. Her return to WWE after a period away from the company allowed her to reinvent aspects of her character. As a member of one of wrestling\'s most storied families, she carries a proud legacy while working to establish her own identity in the business.'
    },
}

with app.app_context():
    updated = 0
    not_found = []
    for name, info in data.items():
        celeb = Celebrity.query.filter_by(name=name).first()
        if celeb:
            celeb.nationality = info.get('nationality')
            celeb.born = info.get('born')
            celeb.net_worth = info.get('net_worth')
            celeb.known_for = info.get('known_for')
            celeb.bio = info.get('bio')
            updated += 1
        else:
            not_found.append(name)
    db.session.commit()
    print(f'\nSuccessfully updated {updated} celebrities!')
    if not_found:
        print(f'\nNot found in database ({len(not_found)}):')
        for name in not_found:
            print(f'  - {name}')
    else:
        print('All 130 celebrities updated successfully!')
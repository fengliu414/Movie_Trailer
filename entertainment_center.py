import media
import fresh_tomatoes

lala_land = media.Movie('La La Land',
    'Exploration of the joy and pain of pursuing your dreams',
    'http://www.filmpro.sk/files/plagat/llland_teaser_sk.jpg',
    'https://www.youtube.com/watch?v=0pdqf4P9MB8')

scent_of_a_woman = media.Movie('Scent of a Woman',
    'A young man serves as an assistant to a crazy retired Army officer',
    'https://upload.wikimedia.org/wikipedia/en/9/91/Scent_of_a_Woman.jpg',
    'https://www.youtube.com/watch?v=F2zTd_YwTvo')

underworld = media.Movie('Underworld',
    'A battle to fend off enemy attacks',
    'http://t1.qpic.cn/mblogpic/4d1ff689a1267c9216b6/2000.jpg',
    'https://www.youtube.com/watch?v=rKHL5PyAPzs')


movies = [lala_land, scent_of_a_woman, underworld]

# Create html file and open the web page
fresh_tomatoes.open_movies_page(movies)

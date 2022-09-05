import datetime as dt
from models.main import Menu
from models.movie import Movie

menu = Menu()
menu.show_menu()

# movie = Movie(name= 'incception', time= '120 Min', publish_date= 2013, director= 'Christofer Nolan')
date_time = dt.datetime.now()
movie = Movie('incception', 120, date_time.strftime('%y'), 'Christofer Nolan')

print(movie.get_movie_info())

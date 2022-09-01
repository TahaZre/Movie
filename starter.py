import datetime
from models.main import Menu
from models.movie import Movie

menu = Menu()
menu.show_menu()

# movie = Movie(name= 'incception', time= '120 Min', publish_date= 2013', director= 'Christofer Nolan')
movie = Movie('incception', '120 Min', 2013, 'Christofer Nolan')

print(movie.Get_movie_info())

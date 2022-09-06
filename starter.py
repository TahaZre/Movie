import datetime as dt
from models.main import Menu
from models.movie import Movie
from models.movie import Crew

# region Menu

menu = Menu()

# endregion


director_info = Crew(12000, 'Christofer', 'Nolan', 1970, 'ENGLAND', 'Director')
movie = Movie('Movie Name', 120, director_info, dt.datetime(2022, 11, 11))

print(movie.get_movie_info())

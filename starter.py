import datetime as dt
from models.main import Menu
from models.movie import (Movie, Crew)

# region Menu

menu = Menu()

# endregion


director_info = Crew(12000, 'Christofer', 'Nolan', 1970, 'ENGLAND', 'z')
cast_one = Crew(500000, 'Leo', 'Dicop', 1974, 'USA', 'c')
cast_two = Crew(300000, 'Tom', 'Hardi', 1977, 'ENGLAND', 'c')

movie = Movie('Movie Name', 120, dt.datetime(2022, 11, 11), director_info)

movie.add_cast(cast_one)
movie.add_cast(cast_two)

print(movie.get_movie_info())

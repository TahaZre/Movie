import datetime
from .person import Person


class Crew(Person):
    def __init__(self, salary, first_name, last_name, born, nationality, role):
        super().__init__(first_name, last_name, born, nationality, role)
        self.salary = salary

    def get_crew(self):
        return {
            'Person': super().person_info(),
            'Salary': self.salary
        }


class Movie:
    casts = []

    def __init__(self, name: str, time: int, *crews: Crew, publish_date=None):
        self.name = name
        self.time = time
        self.crews = crews
        self.publish_date = publish_date if publish_date != None else datetime.datetime.now()

    def get_movie_info(self):
        return {
            'name': self.name,
            'time': self.time,
            'publish_date': self.publish_date.strftime("%d %m %Y"),
            'Crews': len(self.crews),
            # self.director.role: self.director.get_crew()
        }

    def add_cast(self, cast: Crew):
        self.casts.append(cast)

    def get_casts(self):
        all_casts = []
        for cast in self.casts:
            all_casts.append(cast.get_crew())
        return all_casts

    def get_crews(self):
        all_crews = []
        for crew in self.crews:
            all_crews.append(crew.get_crew())
        return all_crews

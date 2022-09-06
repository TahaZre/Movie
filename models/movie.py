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
    def __init__(self, name: str, time: int, director: Crew, publish_date=None):
        self.name = name
        self.time = time
        self.director = director
        self.publish_date = publish_date if publish_date != None else datetime.datetime.now()

    def get_movie_info(self):
        return {
            'name': self.name,
            'time': self.time,
            'director': self.director.get_crew(),
            'publish_date': self.publish_date.strftime("%d %m %Y")
        }

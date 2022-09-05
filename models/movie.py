class Movie:
    def __init__(self, name, time, publish_date, director):
        self.name = name
        self.time = time
        self.publish_date = publish_date
        self.director = director

    def get_movie_info(self):
        return {
            'name': self.name, 'time': self.time, 'publish_date': self.publish_date, 'director': self.director
        }

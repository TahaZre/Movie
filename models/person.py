class Person:
    def __init__(self, first_name, last_name, born, nationality, role):
        self.first_name = first_name
        self.last_name = last_name
        self.born = born
        self.nationality = nationality
        self.role = role

    def person_info(self):
        return {
            'Full Name': f'{self.first_name} {self.last_name}',
            'Born': self.born,
            'Nationality': self.nationality,
        }

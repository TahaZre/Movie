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

    @property
    def role(self):
        return self.__role

    @role.setter
    def role(self, role):
        if role.lower() == 'd':
            self.__role = 'Director'
        elif role.lower() == 'c':
            self.__role = 'Cast'
        elif role.lower() == 'w':
            self.__role = 'Writer'
        else:
            self.__role = 'Staff'

from abc import ABC, abstractmethod
from datetime import datetime


class Person(ABC):

    def __init__(self, last_name, date_of_birth, faculty):
        self._last_name = last_name
        self._date_of_birth = date_of_birth
        self._faculty = faculty
        self._age = self.calc_age()

    @abstractmethod
    def calc_age(self):
        pass

    @property
    def age(self):
        return self._age


class Entrant(Person):

    def calc_age(self):
        return (datetime.now()).year - self._date_of_birth

    def __str__(self):
        return f'Last Name: {self._last_name}, Date of Birth: {self._date_of_birth}, ' \
               f'Faculty: {self._faculty}, Age: {self._age}'


class Student(Person):

    def __init__(self, last_name, date_of_birth, faculty, year_of_study):
        super().__init__(last_name, date_of_birth, faculty)
        self._year_of_study = year_of_study

    def calc_age(self):
        return (datetime.now()).year - self._date_of_birth

    def __str__(self):
        return f'Last Name: {self._last_name}, Date of Birth: {self._date_of_birth}, ' \
               f'Faculty: {self._faculty}, Year of Study: {self._year_of_study}, Age: {self._age}'


class Teacher(Person):

    def __init__(self, last_name, date_of_birth, faculty, position, work_experience):
        super().__init__(last_name, date_of_birth, faculty)
        self._position = position
        self._work_experience = work_experience

    def calc_age(self):
        return (datetime.now()).year - self._date_of_birth

    def __str__(self):
        return f'Last Name: {self._last_name}, Date of Birth: {self._date_of_birth}, ' \
               f'Faculty: {self._faculty}, Position: {self._position}, ' \
               f'Experience: {self._work_experience}, Age: {self._age}'


if __name__ == '__main__':
    person_list = []
    first_entrant = Entrant('Ivanov', 1990, 'Psychology')
    person_list.append(first_entrant)
    first_student = Student('Petrov', 1970, 'Economics', 2)
    person_list.append(first_student)
    first_teacher = Teacher('Stepanov', 1960, 'Literature', 'Dean', 36)
    person_list.append(first_teacher)

    for person in person_list:
        print(person)

    print('Below you will find people from list which meet requirements of the age from 15 till 50:')

    from_age = 15
    til_age = 50

    for person in person_list:
        if from_age <= person.age <= 50:
            print(person)

from db_context_manager import MyDbContextManager


class User:
    def __init__(self, database):
        self._database = database

    def get_list_of_a_students(self):

        with MyDbContextManager(self._database) as db:
            list_of_students = db.execute('SELECT students.first_name, students.last_name '
                                          'FROM students INNER JOIN marks on students.student_id = marks.student_id '
                                          'WHERE marks.mark > 90')

            return list_of_students.fetchall()

    def get_list_of_all_students(self):

        with MyDbContextManager(self._database) as db:
            list_of_all_students = db.execute('SELECT students.first_name, students.last_name '
                                              'FROM students')

            return list_of_all_students.fetchall()

    def find_student_by_number(self, student_id):

        with MyDbContextManager(self._database) as db:
            student_by_number = db.execute('SELECT students.first_name, students.last_name '
                                           'FROM students '
                                           'WHERE student_personal_number = ?', [student_id])

            return student_by_number.fetchone()

    def get_full_info_by_number(self, student_id):
        with MyDbContextManager(self._database) as db:
            student_full_info_by_number = db.execute('SELECT students.first_name, '
                                                     'students.last_name, '
                                                     'students.student_personal_number, '
                                                     'faculty.faculty_name, '
                                                     'marks.subject, '
                                                     'marks.mark '
                                                     'FROM students '
                                                     'INNER JOIN faculty on students.faculty_id = faculty.faculty_id '
                                                     'INNER JOIN marks on students.student_id = marks.student_id '
                                                     'WHERE student_personal_number = ?', [student_id])

            return student_full_info_by_number.fetchone()


class Admin(User):

    def add_student(self, first_name, last_name, student_id, faculty):

        with MyDbContextManager(self._database) as db:
            # print(faculty)
            res = db.execute("SELECT faculty_id FROM faculty WHERE faculty_name LIKE ?", ('%' + faculty + '%', ))
            faculty_id = res.fetchone()
            # print(faculty_id)
            if faculty_id is None:
                # print('nothing is returned')
                return
            else:
                db.execute("INSERT INTO students ('first_name', 'last_name', 'student_personal_number', 'faculty_id') "
                           "VALUES (?, ?, ?, ?)", (first_name, last_name, student_id, faculty_id[0]))
                # print('We added him!!)))')

    def change_student_last_name(self):
        pass

    def change_student_faculty(self):
        pass


if __name__ == '__main__':
    DATABASE = 'students.db'
    # some_user = User(DATABASE)
    # print(some_user.get_list_of_a_students())
    # print(some_user.get_list_of_all_students())
    # print(some_user.find_student_by_number('324698753'))
    # print(some_user.get_full_info_by_number(324698753))

    some_admin = Admin(DATABASE)
    some_admin.add_student('first', 'attempt', 123456789, 'philoso')

import sqlite3


class MyDbContextManager:

    def __init__(self, database):
        self._database = database
        self._connection = sqlite3.connect(self._database)

    def __enter__(self):
        return self._connection.cursor()

    def __exit__(self, ex_type, ex_value, ex_traceback):
        self._connection.commit()
        self._connection.close()


if __name__ == '__main__':
    lookup = 'phil'
    with MyDbContextManager('students.db') as db:
        selection = db.execute('select faculty_id from faculty where faculty_name like ?', (str('%' + lookup + '%'), ))

        print(selection.fetchone())

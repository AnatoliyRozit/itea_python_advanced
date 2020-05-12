import json
from datetime import date


class UserRegistration:

    def __init__(self, username, password):
        self._username = username
        self._password = password
        self._user_role = 'user'

    def is_unique_username(self):

        with open('users.json') as json_file:
            data = json.load(json_file)

        for user in data:
            if user['username'] == self._username:

                return False

        return True

    def is_valid_password(self):

        if len(self._password) < 8:
            return False

        digits = 0
        letters = 0

        for element in self._password:
            if element.isdigit():
                digits += 1
            if element.isalpha():
                letters += 1

        if digits < 3:
            return False

        if letters < 3:
            return False

        return True

    def is_confirmed_password(self, confirmation):

        if self._password != confirmation:
            return False

        return True

    def create_user(self):

        new_user = {
            "username": self._username,
            "password": self._password,
            "user_role": self._user_role,
            "registration_date": str(date.today()),
            "posts": []
        }

        def write_json(data, filename='users.json'):
            with open(filename, 'w') as f:
                json.dump(data, f, indent=4)

        with open('users.json') as json_file:
            data = json.load(json_file)

            data.append(new_user)

        write_json(data)


class UserAuthentication(UserRegistration):

    def login_user(self):

        with open('users.json') as json_file:
            data = json.load(json_file)

        for user in data:
            if user['username'] == self._username:

                if user['password'] == self._password:

                    return True

        return False


class User:

    def __init__(self, username):
        self._username = username
        self._password = self._get_user_password()
        self._user_role = self._get_user_role()
        self._registration_date = self._get_user_registration_date()
        self._posts = self._get_user_posts()
        self._is_logged_in = True
        pass

    def _get_user_password(self):

        with open('users.json') as json_file:
            data = json.load(json_file)

        for user in data:
            if user['username'] == self._username:

                return user['password']

    def _get_user_role(self):

        with open('users.json') as json_file:
            data = json.load(json_file)

        for user in data:
            if user['username'] == self._username:

                return user['user_role']

    def _get_user_registration_date(self):

        with open('users.json') as json_file:
            data = json.load(json_file)

        for user in data:
            if user['username'] == self._username:

                return user['registration_date']

    def _get_user_posts(self):

        with open('users.json') as json_file:
            data = json.load(json_file)

        for user in data:
            if user['username'] == self._username:

                return user['posts']

    def add_new_post(self, post):

        new_post = {
                "date": str(date.today()),
                "post_body": post
            }

        def write_json(data, filename='users.json'):
            with open(filename, 'w') as f:
                json.dump(data, f, indent=4)

        with open('users.json') as json_file:
            data = json.load(json_file)

            for user in data:
                if user['username'] == self._username:
                    user['posts'].append(new_post)

        write_json(data)

    def logout_user(self):
        self._is_logged_in = False

    @staticmethod
    def get_all_users():
        with open('users.json') as json_file:
            data = json.load(json_file)

        for user in data:
            username = user['username']
            password = user['password']
            user_role = user['user_role']
            registration_date = user['registration_date']
            print(f'User: \'{username}\', Password: \'{password}\', '
                  f'Role: \'{user_role}\', Date of Registration: {registration_date}')
            for post in user['posts']:
                date = post['date']
                post_body = post['post_body']
                print(f'User: \'{username}\' on {date} posted: \'{post_body}\'')

    @property
    def user_role(self):
        return self._user_role

    @property
    def registration_date(self):
        return self._registration_date

    @property
    def posts(self):
        return self._posts

    @property
    def is_logged_in(self):
        return self._is_logged_in


if __name__ == '__main__':

    SUPPORTED_ACTIONS = [1, 2, 3]

    to_exit_now = False

    is_logged_in = False

    print('Welcome to Test Social Network!')

    while True:

        if to_exit_now:
            print('\nThank you for visiting us!'
                  '\nLooking forward to seeing you again!')
            break

        user_action = input('\nPlease choose one of the options below to proceed:'
                            '\nEnter \'1\' to Sign Up'
                            '\nEnter \'2\' to Sign In'
                            '\nEnter \'3\' to Exit'
                            '\nMy Choice is ')

        try:
            int(user_action)
        except ValueError:
            print('\nPlease select one of the digits your were suggested to.')
            continue

        if int(user_action) not in SUPPORTED_ACTIONS:
            print('\nPlease select one of the digits your were suggested to.')
            continue

        if int(user_action) == 3:
            print('\nThank you for visiting us!'
                  '\nLooking forward to seeing you again!')
            break

        if int(user_action) == 1:

            while True:

                user = input('Enter Desired Username: ')
                password = input('Enter Password: ')
                confirm_password = input('Confirm Password: ')

                registration_attempt = UserRegistration(user, password)

                if not registration_attempt.is_unique_username():
                    print(f'\nUsername \'{user}\' is already in use. Please choose different value and retry.')
                    continue

                if not registration_attempt.is_valid_password():
                    print('\nEntered password does not meet minimum requirements:'
                          '\nPassword should be at least 8 characters;'
                          '\nAt least 3 digits;'
                          '\nAt least 3 letters.')
                    continue

                if not registration_attempt.is_confirmed_password(confirm_password):
                    print('\nEntered values for Password and Confirmation do not match.'
                          '\nPlease try again.')
                    continue

                registration_attempt.create_user()
                print(f'\nUser \'{user}\' has been registered successfully!'
                      f'\nChoose to Sign In to Login to your Account!')

                break

        if int(user_action) == 2:

            print('\nPlease Enter your User credentials to Login!')

            while True:

                user = input('Enter Username: ')
                password = input('Enter Password: ')

                login_attempt = UserAuthentication(user, password)

                if not login_attempt.login_user():
                    print('\nUsername or Password is invalid.'
                          '\nPlease check your credentials and try again!')
                    continue
                else:
                    print(f'\nUser \'{user}\' is successfully logged in!')
                    current_user = User(user)
                    is_logged_in = True
                    break

        while True:

            NEXT_USER_ACTIONS = [4, 5, 6, 3]

            if not is_logged_in:
                break

            next_user_action = input('\nPlease select one of the options to proceed:'
                                     '\nEnter \'4\' to Add a New Post'
                                     '\nEnter \'5\' to Log out'
                                     '\nEnter \'3\' to Exit'
                                     '\nIf you are an Admin, you can:'
                                     '\n\tEnter \'6\' to print the list of all users with corresponding posts.'
                                     '\nMy Choice is ')

            try:
                int(next_user_action)
            except ValueError:
                print('\nPlease select one of the digits your were suggested to.')
                continue

            if int(next_user_action) not in NEXT_USER_ACTIONS:
                print('\nIncorrect value was entered.')
                continue

            if int(next_user_action) == 3:
                to_exit_now = True
                break

            if int(next_user_action) == 4:
                post_body = input('\nPlease enter body of the post:\n')
                current_user.add_new_post(post_body)

            if int(next_user_action) == 5:
                is_logged_in = False
                break

            if int(next_user_action) == 6:

                if current_user.user_role == 'admin':
                    current_user.get_all_users()
                else:
                    print('\nWarning: Sorry, but current functionality is available for Admins ONLY!')
                    continue

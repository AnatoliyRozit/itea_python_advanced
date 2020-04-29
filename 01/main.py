# Task 1

even_nums = [print(number) for number in range(1, 101) if number % 2 == 0]

# Task 2

countries_and_capitals = {'germany': 'Munich', 'poland': 'Warsaw', 'england': 'London'}

countries_list = ['germany', 'russia', 'bulgary', 'italy']

for key, value in countries_and_capitals.items():

    if key in countries_list:
        print(value)

# Task 3

for number in range(1, 101):

    if number % 15 == 0:
        print('FizzBuzz')

    elif number % 5 == 0:
        print('Buzz')

    elif number % 3 == 0:
        print('Fizz')

    else:
        print(number)

# Task 4


def calculate_deposit(amount, years, percentage):

    return amount / 100 * percentage * years + amount


x = calculate_deposit(1000, 1, 10)
print(x)

from datetime import datetime


def my_logger(func):

    def wrapper(*args):
        start_time = datetime.now()
        print(f'{func.__name__} was started at {start_time}')

        result = [func(*args) for _ in range(1000000)]

        end_time = datetime.now()

        elapsed_time = end_time - start_time

        print(f'{func.__name__} was completed at {end_time}')
        print(f'{func.__name__} function execution time: {elapsed_time}')

        return result[0]

    return wrapper


@my_logger
def my_sum(x, y):
    return x + y


result = my_sum(5, 6)
print(result)

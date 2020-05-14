from threading import Thread
import time


def my_decorator(**kwargs):

    def wrapper(func):
        print('Wrapper was initiated')
        t = Thread(target=func, daemon=kwargs['is_daemon'])
        t.setName(kwargs['name'])
        print('Here we prepared for Thread start')
        return t.start()

    return wrapper


@my_decorator(name='my_thread', is_daemon=False)
def my_func():
    print('My Function was Started')
    time.sleep(5)
    print('This is my Function that woke up!')


a = my_func

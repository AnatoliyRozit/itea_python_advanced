from collections import deque


class Stack:

    def __init__(self):
        self._stack = deque()

    def __str__(self):
        return str(self._stack)

    def get_stack(self):
        return self._stack

    def add_item(self, item):
        return self._stack.append(item)

    def remove_item(self):
        return self._stack.pop()


class Queue:

    def __init__(self):
        self._queue = deque()

    def __str__(self):
        return str(self._queue)

    def get_stack(self):
        return self._queue

    def add_item(self, item):
        return self._queue.append(item)

    def remove_item(self):
        return self._queue.popleft()


class ComplexNumber:

    def __init__(self, real, imaginary):
        self.number = self.num_to_complex(real, imaginary)

    @staticmethod
    def num_to_complex(real, imaginary):
        return complex(real, imaginary)

    def __str__(self):
        return str(self.number)

    def __add__(self, other):
        real = self.number.real + other.number.real
        imaginary = self.number.imag + other.number.imag

        return ComplexNumber(real, imaginary)

    def __sub__(self, other):
        real = self.number.real - other.number.real
        imaginary = self.number.imag - other.number.imag

        return ComplexNumber(real, imaginary)

    def __mul__(self, other):
        real = self.number.real * other.number.real
        imaginary = self.number.imag * other.number.imag

        return ComplexNumber(real, imaginary)

    def __truediv__(self, other):
        real = self.number.real / other.number.real
        imaginary = self.number.imag / other.number.imag

        return ComplexNumber(real, imaginary)


if __name__ == '__main__':

    print('This is how stack works:')
    my_stack = Stack()
    my_stack.add_item(1)
    my_stack.add_item(2)
    my_stack.add_item(3)
    my_stack.add_item(4)
    print(my_stack)
    my_stack.remove_item()
    print(my_stack)
    my_stack.remove_item()
    print(my_stack)

    print('\nThis  is how queue works:')
    my_queue = Queue()
    my_queue.add_item(1)
    my_queue.add_item(2)
    my_queue.add_item(3)
    my_queue.add_item(4)
    print(my_queue)
    my_queue.remove_item()
    print(my_queue)
    my_queue.remove_item()
    print(my_queue)

    print('\nThis is how Complex number works:')

    complex_number_one = ComplexNumber(4, 8)
    print(f'Comp Num 1: {complex_number_one}')
    complex_number_two = ComplexNumber(6, 10)
    print(f'Comp Num 2: {complex_number_two}')
    sum_of_numbers = complex_number_one + complex_number_two
    print(f'Sum of Numbers: {sum_of_numbers}')
    substitution_of_numbers = complex_number_one - complex_number_two
    print(f'Sub of Numbers: {substitution_of_numbers}')
    division_of_numbers = complex_number_one / complex_number_two
    print(f'Div of Numbers: {division_of_numbers}')
    multiplication_of_numbers = complex_number_one * complex_number_two
    print(f'Mul of Numbers: {multiplication_of_numbers}')

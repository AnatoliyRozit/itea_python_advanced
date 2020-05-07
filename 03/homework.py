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

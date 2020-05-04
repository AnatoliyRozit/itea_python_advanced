class Dot:

    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z

    def get_x(self):
        return self._x

    def set_x(self, value):
        self._x = value

    def get_y(self):
        return self._y

    def set_y(self, value):
        self._y = value

    def get_z(self):
        return self._z

    def set_z(self, value):
        self._z = value

    def __add__(self, other):
        x = self.get_x() + other.get_x()
        y = self.get_y() + other.get_y()
        z = self.get_z() + other.get_z()

        return x, y, z

    def __sub__(self, other):
        x = self.get_x() - other.get_x()
        y = self.get_y() - other.get_y()
        z = self.get_z() - other.get_z()

        return x, y, z

    def __mul__(self, other):
        x = self.get_x() * other.get_x()
        y = self.get_y() * other.get_y()
        z = self.get_z() * other.get_z()

        return x, y, z

    def __truediv__(self, other):
        x = self.get_x() / other.get_x()
        y = self.get_y() / other.get_y()
        z = self.get_z() / other.get_z()

        return x, y, z

    def __neg__(self):
        return Dot(-self._x, -self._y, -self._z)


if __name__ == '__main__':
    dot_a = Dot(1, 2, 3)
    dot_b = Dot(1, 2, 3)
    dot_c = dot_a * dot_b
    print(dot_c)

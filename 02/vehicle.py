class Vehicle:

    type = 'Vehicle'

    def __init__(self, manufacturer, model, color, max_speed,
                 fuel_volume, fuel_consumption, speed_limit, pulled_weight):
        self._manufacturer = manufacturer
        self._model = model
        self._color = color
        self._max_speed = max_speed
        self._fuel_volume = fuel_volume
        self._fuel_consumption = fuel_consumption
        self._speed_limit = speed_limit
        self._pulled_weight = pulled_weight
        self._max_travel = self.calc_max_travel()

    def get_max_travel(self):
        return self._max_travel

    def get_fuel_volume(self):
        return self._fuel_volume

    def get_pulled_weight(self):
        return self._pulled_weight

    def get_fuel_consumption(self):
        return self._fuel_consumption

    def calc_max_travel(self):

        return self._fuel_volume / self._fuel_consumption * 100


class Car(Vehicle):

    _type = 'Car'


class Truck(Vehicle):

    _type = 'Truck'

    def calc_max_travel(self):

        if self.get_pulled_weight() > 0:

            additional_weight_coef = self.get_pulled_weight() / 100

        else:
            additional_weight_coef = 0

        return self.get_fuel_volume() / (self.get_fuel_consumption() + additional_weight_coef) * 100


if __name__ == '__main__':
    y = Truck('Mercedes', 'S5', 'Red', 200, 300, 10, 100, 200)
    x = Car('Mercedes', 'S5', 'Red', 200, 300, 10, 100, 200)

    print(y._max_travel, x._max_travel)
class MyList:

    def __init__(self, *args):
        self.data = []
        for arg in args:
            self.data.append(arg)

    def __str__(self):
        return str(self.data)

    def append(self, *args):
        self.data += args

    def insert(self, index, value):
        self.data[index] = value

    def pop(self):
        self.data = self.data[:len(self.data)-1]




    # def remove(self):
    #     pass
    #
    # def clear(self):
    #     pass
    #
    # def __add__(self, other):
    #     pass

if __name__ == '__main__':
    new_list = MyList(1, 2, 3)
    print(new_list)
    new_list_complex = MyList((2, 1), 2, 3)
    print(new_list_complex)
    new_list.append('it should work')
    print(new_list)
    new_list_complex.insert(1, 'some text')
    print(new_list_complex)
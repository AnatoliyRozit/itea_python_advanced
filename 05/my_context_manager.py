class MyContextManager:

    def __init__(self, name, mode):
        self.obj = open(name, mode)

    def __enter__(self):
        return self.obj

    def __exit__(self, type, value, traceback):
        self.obj.close()


if __name__ == '__main__':

    with MyContextManager('some_file.txt', 'w') as f:
        f.write('Hi!')

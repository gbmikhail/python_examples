class A:
    def __init__(self):
        print('__init__')
        self._a = 0

    @property
    def a(self):
        print('getter')
        return self._a

    @a.setter
    def a(self, value):
        print('setter')
        self._a = value


a = A()
a.a = 20
print(a.a)

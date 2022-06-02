# Дескрипроты

class NoneNegative:
    # def __init__(self, name):
    #     # До python 3.6
    #     self.name = name

    def __set_name__(self, owner, name):
        # Начиная с python 3.6
        self.name = name

    def __get__(self, instance, owner):
        # Создаем ключ в словаре (для что бы необязательно было использовать объявление в __init__)
        if self.name not in instance.__dict__:
            instance.__dict__[self.name] = None
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('Отрицательные значения недопустимы')
        instance.__dict__[self.name] = value


class Order:
    price = NoneNegative()
    count = NoneNegative()

    def __init__(self):
        # __init__ можно закомментировать
        self.price = 0
        self.count = 0


def main():
    order1 = Order()
    order1.price = 100
    order2 = Order()
    order2.price = 1

    print(order1.price, order1.count)
    print(order2.price, order2.count)


if __name__ == '__main__':
    main()

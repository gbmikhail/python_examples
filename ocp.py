from enum import Enum
from typing import List


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Product:
    def __init__(self, name, color, size):
        self.size = size
        self.color = color
        self.name = name


class ProductFilter:
    def filter_by_color(self, products: List[Product], color: Color):
        for i in products:
            if i.color == color:
                yield i

    def filter_by_size(self, products: List[Product], size: Size):
        for i in products:
            if i.size == size:
                yield i

    def filter_by_clor_and_size(self, products: List[Product], color: Color, size: Size):
        for i in products:
            if i.color == color and i.size == size:
                yield i


# Specification
class Specification:
    def is_satisfied(self, item):
        pass

    def __and__(self, other):
        return AndSpecification(self, other)


class Filter:
    def filter(self, items, spec: Specification):
        pass


class ColorSpecification(Specification):
    def __init__(self, color: Color):
        self.color = color

    def is_satisfied(self, item: Product):
        return item.color == self.color


class SizeSpecification(Specification):
    def __init__(self, size: Size):
        self.size = size

    def is_satisfied(self, item: Product):
        return item.size == self.size


class AndSpecification(Specification):
    def __init__(self, *args):
        self.args = args

    def is_satisfied(self, item):
        return all(map(
            lambda spec: spec.is_satisfied(item), self.args
        ))


class BetterFilter(Filter):
    def filter(self, items: List[Product], spec: Specification):
        for item in items:
            if spec.is_satisfied(item):
                yield item


if __name__ == '__main__':
    products = [
        Product('Apple', Color.GREEN, Size.SMALL),
        Product('Tree', Color.GREEN, Size.MEDIUM),
        Product('House', Color.BLUE, Size.LARGE),
    ]

    pf = ProductFilter()
    for p in pf.filter_by_color(products, Color.GREEN):
        print(p.name, p.color)

    print('*' * 80)
    bf = BetterFilter()
    green = ColorSpecification(Color.GREEN)
    for p in bf.filter(products, green):
        print(p.name, p.color)

    print(' * large:')
    large = SizeSpecification(Size.LARGE)
    for p in bf.filter(products, large):
        print(p.name, p.color, p.size)

    print(' * large and blue:')
    # and_specification = AndSpecification(large, ColorSpecification(Color.BLUE))
    and_specification = large & ColorSpecification(Color.BLUE)
    for p in bf.filter(products, and_specification):
        print(p.name, p.color, p.size)

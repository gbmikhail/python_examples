# v1 - metaclass
class SingleTone(type):
    __instance = None

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__call__(*args, **kwargs)
        return cls.__instance


class SqlConnection(metaclass=SingleTone):
    pass


a = SqlConnection()
b = SqlConnection()

print(id(a), id(b), a is b)


# v2 - BaseClass
class SingletonBase(object):
    __instance = None

    def __new__(cls):
        if not isinstance(cls.__instance, cls):
            cls.__instance = object.__new__(cls)
        return cls.__instance


class MyClass(SingletonBase):
    pass


a = MyClass()
b = MyClass()

print(id(a), id(b), a is b)

class RegistryHolder(type):
    __registry = {}

    def __new__(mcs, name, bases, attr):
        new_mcs = type.__new__(mcs, name, bases, attr)
        mcs.__registry[new_mcs.__name__] = new_mcs
        return new_mcs

    @classmethod
    def get_registry(mcs):
        return dict(mcs.__registry)

    # def __call__(cls, *args, **kwargs):
    #     print(f'call {cls.__name__}')
    #     # super().__call__(*args, **kwargs)


class BaseRegisteredClass(metaclass=RegistryHolder):
    pass


class FirstClass(BaseRegisteredClass):
    pass


a = FirstClass()
b = FirstClass()

print(BaseRegisteredClass.get_registry())

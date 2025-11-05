class UppercaseAttributes(type):
    def __new__(cls, name, bases, dct):
        uppercase = {k.upper(): v for k, v in dct.items() if not k.startswith('__')}
        return super().__new__(cls, name, bases, uppercase)

class MyClass(metaclass=UppercaseAttributes):
    greet = "hello"
    number = 42

obj = MyClass()
print(hasattr(obj, "greet"))   # False
print(obj.GREET)               # hello

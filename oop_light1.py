class Person:

    def __init__(self, name, age, secret) -> None:
        self._age = age
        self._name = name
        self.__secret = secret
        self._counter = 0

    def _get_secret(self):
        return self.__secret
    
p1 = Person('Sebastian', 40, 'Hemligt!')
p1._age = 200
print(p1._age)
print(p1._name)
print(p1._Person__secret)
print(p1._get_secret())
# print(p1.__secret)
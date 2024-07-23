class Person:
    count = 0

    def __init__(self, name):
        self.name = name
        Person.count += 1


person1 = Person('iu')
person2 = Person('BTS')

class Person:
    count = 0

    def __init__(self, name):
        self.name = name
        Person.count += 1

    @classmethod
    def number_of_population(cls):
        # 이 아래 두개는 완전 동일하지 않음: Class의 상속 기능 떄문에
        print(f'인구수는 {cls.count}입니다.')
        print(f'인구수는 {Person.count}입니다.')


person1 = Person('iu')
person2 = Person('BTS')

Person.number_of_population()
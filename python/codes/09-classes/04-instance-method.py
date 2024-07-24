class Person:
    def __init__(self, name):
        self.name = name
        # 왼쪽 name은 인스턴스 변수 name
        # 오른쪽 name은 함수의 매개변수 이름
        print('인스턴스가 생성되었습니다')

    def greeting(self):
        print(f'안녕하세요. {self.name}입니다')    

    def hobby(self, hobby_1, hobby_2):
        print(f'저 {self.name}은 {hobby_1}과 {hobby_2}를 좋아합니다')

person_1 = Person('성준')

print()

person_1.greeting()
Person.greeting(person_1)

print()

person_1.hobby('게임', '술')
Person.hobby(person_1, '게임', '술')


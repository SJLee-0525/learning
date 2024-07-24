class Person:
    # 클래스 변수 count
    count = 0

    def __init__(self, name):
        # 인스턴스 변수 name
        self.name = name
        Person.count += 1

person1 = Person('iu')
person2 = Person('BTS')

print(Person.count)  # 2

##########################

class Circle:
    pi = 3.14

    def __init__(self, r):
        self.r = r

c1 = Circle(5)
c2 = Circle(10)

print(c1.r)
print(c2.r)

print(c1.pi) # 3.14

# c1 본인에게 pi라는 인스턴스 변수가 있는지 찾아봄.
# 없으면 윗 단계로 가서 찾음
# 클래스 변수에 pi = 3.14 존재

c1.pi = 100

print(c1.pi) # 100 
# c1 본인의 인스턴스 변수 pi를 생성

print(Circle.pi) # 3.14
# 실제로 클래스 변수에는 영향이 없음


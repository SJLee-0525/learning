# super 사용 전
class Person:
    def __init__(self, name, age, number, email):
        self.name = name
        self.age = age
        self.number = number
        self.email = email


class Student(Person):
    def __init__(self, name, age, number, email, student_id):
        self.name = name
        self.age = age
        self.number = number
        self.email = email
        self.student_id = student_id



# super 사용 예시 - 단일 상속
class Person:
    def __init__(self, name, age, number, email):
        self.name = name
        self.age = age
        self.number = number
        self.email = email

class Student(Person):
    def __init__(self, name, age, number, email, id, gpa):
        super().__init__(name, age, number, email)
        self.id = id
        self.gpa = gpa

student_a = Student('sungjoon', 25, 9213, '@@@', 172614, 3.5)

print(student_a.name)
print(student_a.age)
print(student_a.number)
print(student_a.email)
print(student_a.id)
print(student_a.gpa)

print('---')
# super 사용 예시 - 다중 상속
class ParentA:
    def __init__(self):
        self.value_a = 'ParentA'

    def show_value(self):
        print(f'Value from ParentA: {self.value_a}')


class ParentB:
    def __init__(self):
        self.value_b = 'ParentB'

    def show_value(self):
        print(f'Value from ParentB: {self.value_b}')


class Child(ParentA, ParentB):
    def __init__(self):
        super().__init__() # 얘는 찾으면 끝임. 굳이 ParentB까지 가지 않음
        self.value_c = 'Child'

child_1 = Child()
print(child_1.value_a) # ParentA
print(child_1.value_c) # Child
# print(child_1.value_b) # AttributeError: 'Child' object has no attribute 'value_b'
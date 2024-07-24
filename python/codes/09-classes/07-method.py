class MyClass:
    def instance_method(self):
        return 'instance method', self

    @classmethod
    def class_method(cls):
        return 'class method', cls

    @staticmethod
    def static_method():
        return 'static method'


instance = MyClass()
# 클래스가 할 수 있는 것
print(MyClass.instance_method(instance)) # 인스턴스 매서드는 쓰지 마셈
print(MyClass.class_method())
print(MyClass.static_method())

'''클래스는 클래스 매서드와 스태틱 매서드만 쓰자'''


# 인스턴스가 할 수 있는 것
print(instance.instance_method())
print(instance.class_method()) # 클래스 메서드 쓰지 ㄴㄴ
print(instance.static_method()) # 스태틱 메서드도 쓰지 ㄴㄴ

'''인스턴스는 인스턴스 매서드만 쓰자'''

class StringUtils:
    # 생성자 함수 생략이 가능함 (초기 값이 없다면)
    # 안 하면 파이썬이 알아서 만들어줌, 하지만 만드는 것을 추천
    def __init__(self):
        pass

    # 아래는 클래스가 호출하기 때문에, 굳이 인스턴스를 생성할 필요 없음
    @staticmethod
    def reverse_string(string):
        return string[::-1]

    @staticmethod
    def capitalrize_string(string):
        return string.capitalize()

text = 'hello, world'

# 스태틱 메서드는 굳이 인스턴스 생성 안 해도 됨

text_result_1 = StringUtils.reverse_string(text)
print(text_result_1)

print()

text_result_2 = StringUtils.capitalrize_string(text)
print(text_result_2)
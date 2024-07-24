# 클래스 정의
class Person: 
    # 속성
    blood_color = 'red'
    pass

    # 매서드
    def __init__(self, name):
        self.name = name

    def singing(self):
        return f'{self.name}이 노래합니다.'    

# 인스턴스 생성
singer_1 = Person('sungjoon')

# (인스턴스) 메서드 호출
print(singer_1.singing())

# 속성(변수) 접근 : 클래스 전역에서 변수 사용 가능
print(singer_1.blood_color)

# 인스턴스 속성(변수) : 이 변수는 singer_1만이 사용할 수 있음
print(singer_1.name)
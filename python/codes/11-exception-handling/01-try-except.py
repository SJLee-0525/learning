# try-except
# try:
#     result = 10 / 0
# except ZeroDivisionError:
#     print('0으로 못 나눠 바보야')

# try:
#     num = int(input()) / 2
#     print(num)
# except ValueError:
#     print('숫자가 아니야 바보야')

# 복수 예외처리
try:
    result = 100 / int(input())
except ZeroDivisionError:
    print('너 방금 0 넣었냐 ㅋ')
except ValueError:
    print('으휴 숫자도 아닌 거로 나누려고 하냐')
except:
    print('오류났어. 난 뭐가 문젠지 모르겠다/')
else:
    print(result)
finally:
    print('프로그램이 꺼진다 뿅')
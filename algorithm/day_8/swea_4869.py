T = int(input())

for tc in range(1, T + 1):
    N = int(int(input()) // 10)





#
# T = int(input())
#
# for tc in range(1, T + 1):
#     N = int(int(input()) // 10)
#
#     # DP로 풀어보기기
#     arr = [0] * (N + 1) # N번쨰 인덱스까지 있을 수 있도록 리스트 생성
#     arr[0] = 1 # 초기값 생성
#     arr[1] = 1
#
#     for i in range(2, N + 1): # 공식.. 다음번에는 내가 찾아보자
#         arr[i] = arr[i - 1] + (arr[i - 2] * 2)
#
#     print(f'#{tc} {arr[N]}')
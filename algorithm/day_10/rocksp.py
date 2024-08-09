def f(i, j):    # i~j번까지의 승자를 찾는 함수
    if i == j:    # 한 명만 남은 경우
        return i
    else:       # 두 명 이상인 경우 두 그룹의 승자를 찾차 최종 승자를 가림
        left = f(i, (i + j) // 2)       # 왼쪽 그룹의 승자
        right = f(((i + j) // 2) + 1, j)    # 오른쪽 그룹의 승자
        return win(left, right)     # 두 그룹의 승자를 찾는 함수 구현

def win(left, right):
    # 1 찌, 2 묵, 3 보
    if group[left] == group[right]: # 비기면 왼쪽애가
        return left
    elif (group[left] == 1 and group[right] == 3) or (group[left] == 2 and group[right] == 1) or (group[left] == 3 and group[right] == 2):
        return left
    else:
        return right

T = int(input())
for tc in range(1, T + 1):
    N = int(input()) # 인원수
    group = [0] + list(map(int, input().split()))
    result = f(1, N)
    print(f'#{tc} {result}')
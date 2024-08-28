'''
7
20 15 19 4 13 11 17

7
20 15 19 4 13 11 23
'''


# 최대힙
def enq(n):
    global last
    last += 1   # 마지막 노드 추가 (완전 이진 트리 유지) : len 연산을 피하기 위해
    h[last] = n # 마지막 노드에 데이터 삽입
    print(h, last)
    c = last    # 부모>자식 비교를 위해
    p = c//2    # 부모 번호 계산 (자식의 인덱스 번호를 이용해 부모 인덱스 구하기)
    while p >= 1 and h[p] < h[c]:   # 부모가 있는데, 더 작으면 (제자리를 찾거나, 루트일 때 까지)
        h[p], h[c] = h[c], h[p]     # 교환
        c = p
        p = c//2


def deq():
    global last
    tmp = h[1]      # 루트의 키값 보관 (마지막 노드 값을 복사)
    h[1] = h[last]
    last -= 1
    p = 1           # 새로 옮긴 루트
    c = p*2
    while c <= last:  # 자식이 있으면
        if c+1 <= last and h[c] < h[c+1]: # 오른쪽 자식이 있고 더 크면
            c += 1
        if h[p] < h[c]:     # 부모가 더 작으면
            h[p], h[c] = h[c], h[p] # swap
            p = c
            c = p*2
        else:
            break
    return tmp      # 뽑은 값 반환


N = int(input())          # 필요한 노드 수
arr = list(map(int, input().split()))

h = [0]*(N+1)   # 최대 힙: 완전 이진 트리 보장 -> 1차원 리스트로 구현 가능 (N 노드의 자식: N * 2, N * 2 + 1)
last = 0        # 힙의 마지막 노드 번호

for num in arr:
    enq(num)

print(h)

while last > 0:
    print(deq(), end=' ')

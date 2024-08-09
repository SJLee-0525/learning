# 방법 2 - 시간초과.
import sys
N = int(sys.stdin.readline().rstrip())
final_dic = {}
final_list = [0] * N # 색종이별 최종 값을 담을 리스트

for k in range(N):
    left_x, left_y, length, height = map(int, sys.stdin.readline().rstrip().split())
    right_x = left_x + length
    right_y = left_y + height
    final_dic.update({(i, j): k for i in range(left_x, right_x) for j in range(left_y, right_y)})

# print(final_dic)

for v in final_dic.values():
    final_list[v] += 1

for ans in final_list:
    print(ans)
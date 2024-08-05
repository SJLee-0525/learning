T = int(input())

for tc in range(1, T + 1):
    txt = input()
    txt_len = len(txt)
    start, end = 0, txt_len - 1

    ans = 1
    for i in range(txt_len // 2):
        if txt[i] != txt[txt_len - 1 - i]:
            ans = 0
            break

    print(f'#{tc} {ans}')

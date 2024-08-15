T = int(input())
for tc in range(1, T + 1):
    workspace = input()

    pipe = 0
    cut = 0
    for w in range(len(workspace)):
        if workspace[w] == '(': # 파이프 개수 늘림
            pipe += 1
        if workspace[w] == ')':
            if workspace[w - 1] == '(': # 레이저
                pipe -= 1
                cut += pipe # 레이저가 등장하면 존재하는 파이프 수만큼 커팅된 파이프가 생김
            else:
                cut += 1    # 레이저가 아니라면 파이프가 끝난 것. 
                pipe -= 1   # 끝날 때마다 커팅이 한 개 씩 늘어나고 파이프가 줄어듬

    print(f'#{tc} {cut}')
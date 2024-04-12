N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

max = N*M
cnt = 0
xy = [0]*max; num = [0]*max

# 북 동 남 서
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
dir = 0

# board idx ++ ~ xy 상황으로 넘겨주면 쉽게 풀릴 것 같음

for i in range(N):
    for j in range(M):
        if board[i][j] != 0:
            xy[cnt] = [i,j]
            num[cnt] = board[i][j]
            cnt += 1

for i in range(cnt+1):
    dir = 0
    if num[i-1] == 1:
        now = xy[cnt]
        for len() 
        x = dx[dir]; y = dy[dir]

    elif num[i-1] == 2:

    elif num[i-1] == 3:

    elif num[i-1] == 4:

    elif num[i-1] == 5:


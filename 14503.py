row,col = map(int, input().split())

# 북 동 남 서
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

nx,ny,dirct = map(int, input().split())

room = [list(map(int, input().split())) for _ in range(row)]

rect = 0

while(True):
    # 현재 칸 청소
    if(room[nx][ny] > 0):
        room[nx][ny] =0
        rect += 1

    # 주변 에서 청소가 안된 칸 수 세기
    num = 0

    for i in range(4):
        currX, currY = nx + dx[dirct], ny + dy[dirct]
        dirct = (dirct + 1) % 4

        if currX <0 or currX>=row or currY <0 or currY>=col:
            continue
        elif (room[currX][currY] == 1):
            num += 1
        else:
            continue

    # 빈칸이 없는 경우 -> 후진
    if(num < 0):
        dirct = (dirct + 2) % 4
        nx = nx+dx[dirct]; ny = ny+dy[dirct]
        # 뒤 칸이 벽이면 작동 break
        if room[nx][ny] < 0:
            break
        else:
            continue

    # 빈칸이 있는 경우
    else:
        for i in range(4):
            # 90도 회전 (반시계, 왼쪽)
            dirct = (dirct + 3) % 4
            currX, currY = nx + dx[dirct], ny + dy[dirct]
            # 앞칸 청소 되지 않은 칸 일때 -> 전진
            if currX <0 or currX>=row or currY <0 or currY>=col:
                continue
            elif room[currX][currY] > 0:
                nx = currX; ny = currY
                break
            # 아니면 다시 반복 continue
            else:
                continue

print(rect)




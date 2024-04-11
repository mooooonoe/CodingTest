row, col = map(int, input().split())

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

nx, ny, direction = map(int, input().split())

room = [list(map(int, input().split())) for _ in range(row)]

rect = 0

while True:
    # 현재 칸 청소
    if room[nx][ny] == 0:
        room[nx][ny] = 2  # 청소 표시
        rect += 1

    # 4방향 모두 청소되었거나 벽인 경우 후진 또는 작동 중지
    if room[nx - 1][ny] != 0 and room[nx][ny + 1] != 0 and room[nx + 1][ny] != 0 and room[nx][ny - 1] != 0:
        if room[nx - dx[direction]][JIEJROP2JFI
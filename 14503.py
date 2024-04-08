# ** 방향 조심
#
# `# 북 동 남 서dx = [-1, 1, 0, 0]dy = [0, 0, 1, -1]`
#
# 이게 아니라 ,
#
# `dx = [-1, 0, 1, 0]dy = [0, 1, 0, -1]`
#
# 이게 맞음
#
# 북이랑 동의 dx dy 증감 방향이 같으면 안됨 ~
#
# ** curr 값을 만들 필요가 없음
#
# 구냥 nx ny 만 가지고 잘 만들면 됨
#
# 그리고 !! 1 은 벽이야 1!!

row,col = map(int, input().split())

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

nx,ny,dirct = map(int, input().split())

room = [list(map(int, input().split())) for _ in range(row)]

rect = 0

while True:
    # 현재 칸 청소
    if room[nx][ny] == 0:
        room[nx][ny] = 2
        rect += 1

    if room[nx-1][ny] != 0 and room[nx+1][ny] != 0 and room[nx][ny-1] != 0 and room[nx][ny+1] != 0:
        if room[nx - dx[dirct]][ny - dy[dirct]] == 1:   #### 벽 !
            break
        else:
            nx -= dx[dirct]; ny -= dy[dirct]
    else:
        dirct = (dirct -1) % 4
        if room[nx + dx[dirct]][ny + dy[dirct]] == 0:
            nx += dx[dirct]; ny += dy[dirct]

print(rect)




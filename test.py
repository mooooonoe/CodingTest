# when, dir = input().split()
# print(when, dir)
# print(type(dir))
# print(type(int(when)))
#

####


# 위 오른쪽 아래 왼쪽
# 0     1  2    3
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
dirct = 1

nx, ny = 0, 0
print('현위치', nx, ny)

nx = nx + dx[dirct]
ny = ny + dy[dirct]

print(dx[dirct], dy[dirct])
print('오른쪽 이동후', nx, ny)

dirct = (dirct+1)%4
nx = nx + dx[dirct]
ny = ny + dy[dirct]

print(dx[dirct], dy[dirct])
print('아래 이동후', nx, ny)

dirct = (dirct+3)%4

nx = nx + dx[dirct]
ny = ny + dy[dirct]

print(dx[dirct], dy[dirct])
print('왼쪽 이동후', nx, ny)
num = max(1, 2, 3, 0, 5, 4)
print(num)

arrT = [3,5,1,1,2,4,2]
for i in range(len(arrT)-2, -1,-1):
    print(arrT[i], end ='')


day = 7
dp = [0 for i in range(day+1)]
print(dp)

newdp = [0] * day
print(newdp)

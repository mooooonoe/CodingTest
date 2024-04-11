N = int(input())
tester = list(map(int, input().split()))
a,b = map(int, input().split())

cnt = [0]*N
total = 0

for i in range(N):
    tester[i] -= a
    cnt[i] += 1
    while tester[i] > 0:
        tester[i] -= b
        cnt[i] += 1
        if tester[i] <= 0:
            total += cnt[i]
            break

print(total)
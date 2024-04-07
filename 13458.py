N = int(input())
tester = list(map(int, input().split()))
a,b = map(int, input().split())

total = 0
for i in range(N):
    cnt = 1
    tester[i] -= a
    while tester[i] > 0:
        tester[i] -= b
        cnt += 1
    total += cnt

print(total)
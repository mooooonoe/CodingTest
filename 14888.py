N = int(input())
num = list(map(int, input().split()))
tools = list(map(int, input().split()))
dtool = [0, 1, 2, 3] # +  -  *  /
org = [0]*(N-1); cnt=0

for i in range(4):
    while(tools[i]>0):
        org[cnt] = dtool[i]
        cnt += 1
        tools[i] -= 1
    if(tools[i]==0):
        continue

def permutation(arr, r):
    result = []
    arr.sort()
    def gen_permutation(elements, r, path=[]):
        if r == 0:
            result.append(path)
            return

        for i in range(len(elements)):
            if i > 0 and elements[i] == elements[i-1]:
                continue
            gen_permutation(elements[:i]+elements[i+1:], r - 1, path + [elements[i]])

    gen_permutation(arr, r)
    return result

Ori = list(permutation(org, N-1))

def Toolmath(a,b,x):
    if x == 0:
        return a+b
    elif x == 1:
        return a-b
    elif x == 2:
        return a*b
    elif x == 3:
        a = round(abs(a))
        b = round(abs(b))
        result = round(a/b)
        if a<0:
            result = -result
            return result
        else:
            return

one = 0; two = 0
arr = [0]*len(Ori)
for j in range(len(Ori)):
    for i in range(N-1):
        if i == 0:
            y = num[0]
        y = Toolmath(y, num[i+1], Ori[j][i])
        arr[j] = y

    one = min(arr)
    two = max(arr)


print(two)
print(one)











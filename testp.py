arr = [1,2,3]
r = 3

def per(arr, r):
    for i in per(arr[:i]+arr[i+1:], r-1):
        item = arr[i]


str= "BlockDMask Blog.";
print(f"str : {str}\n")

# find 예제1
print("1. str.find('찾을 문자')")
result1 = str.find('a')   # 문자가 있는 경우
result2 = str.find('Z')   # 문자가 없는 경우

print(f"str.find('a') : {result1}")
print(f"str.find('Z') : {result2}")

result3 = str.find('ask') # 문자열이 있는 경우
result4 = str.find('kkk') # 문자열이 없는 경우

print(f"str.find('ask') : {result3}")
print(f"str.find('kkk') : {result4}")
print()


# find 예제2
print("2. str.find('찾을 문자', 시작index)")
result5 = str.find('o')
result6 = str.find('o', 5)

print(f"str.find('o') : {result5}")

print(f"str[5] : {str[5]}")
print(f"str.find('o', 5) : {result6}")
print()


# find 예제3
print("3. str.find('찾을 문자', 시작 index, 끝 index)")
result7 = str.find('o')
result8 = str.find('o', 5, 11)  # "DMask B"

print(f"str.find('o') : {result7}")

print(f"str[5]~str[11] : {str[5]} ~ {str[11]}")
print(f"str.find('o', 5, 11) : {result8}")
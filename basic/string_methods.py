name = "파이썬"
hello = "hello"

#print("문자열의 길이 : " , len(name)) # 문자열의 길이 
#print("찾는 문자의 위치를 돌려주는 함수(find):", name.find("이")) # find는 문자열중 문자를 찾아 위치를 돌려줌
#print(hello.capitalize()) # 맨 첫 문장을 대문자로 표현
#print(hello.upper())
#print(hello.lower())
#print(hello.isdigit()) # 숫자면 true 다른거면 false
#print(hello.isalpha()) # 알파벳이면 true 다른거면 false
#print(hello.count("l")) #문자의 수를 셈.
#print(hello.replace("l", "w")) # 문자를 바꿔줌 ("기존문자", "바꿀문자")
#print(hello*3)



"""
String Slice 하는법
"""

# slicing [ start : end : step]

text = "python programming"

first = text[0:] # 처음부터 끝까지
print(first)

second = text[:6]
print(second)


step = text[0:len(text):1]
print(step)

# step 만큼 끊어서 저장
step = text[0:len(text):2]
print(step)

step = text[::3]
print(step)

reversed_text = text[::-1]
print(reversed_text)


"""
slice function
"""

site = "https://naver.com"

"""
-1 이 m
-2 가 o
...
-4 는 .
까지 전부다 지운다는 것
"""
str = slice(8, -4) # 단순히 어디서부터 어딜 자른다고 가지고 있는 것.
print(site[str])




"""
string.format() : 출력시 더 많은 제공을 해줌.
"""

animal = "동물들입니다"

print("the {:10} 입니다.".format(animal))
# 위처럼 설정시 지정된 문자열보다 길면 나머진 공백으로 채움.

print("the {:>10} 입니다.".format(animal)) #오른쪽 정렬
print("the {:^10} 입니다.".format(animal)) # 중앙정렬



number = 3.1415926535

print("the number is {:.2f}".format(number))


num = 1000

print("this is {:b}".format(num)) # 2진수
print("this is {:o}".format(num)) # 8진수
print("this is {:X}".format(num)) # 16진수
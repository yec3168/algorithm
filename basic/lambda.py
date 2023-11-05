# lambda 함수


# 하나의 라인으로 짜는 코딩
# 짧게 자를수 있음

"""
parameters:expression
"""


## 일반 표현식 
def double(x):
    return x * 2


print(double(5))


## 람다 표현식
double = lambda x: x*2
    # 파라미터 : 원하는결과

print(double(10))


# ex2
multiply = lambda x, y : x * y

print(multiply(10, 20))


#ex3
add = lambda a, b, c, d : a +b +c +d

print(add(1, 2, 3, 4))



"""
sorting ( lambda 사용 )
"""


student = [("학생1", "A", 21),
           ("학생2", "B", 21),
           ("학생3", "A", 20),
           ("학생8", "D", 29),
           ("학생4","C", 27)]



student.sort()

for i in student:
    print(i)

print()

grade = lambda grade:grade[1] ## index[1]로 sort
student.sort(key=grade)

for i in student:
    print(i)
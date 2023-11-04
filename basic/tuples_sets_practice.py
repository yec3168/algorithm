# tuple은 collection이라고도 함.
# 변경이 불가능
# 관련된 데이터들을 그룹화하는데 특화.

"""
tuple = (값, 값, 값...)같이 표현
c언어로 보자면 구조체??
"""

student = ("eungchan", 24, "male")

print(student.count(24))

# 특정값의 인덱스를 찾고 싶다면 사용하는 함수 index
# 아래를 출력하면 2가 나오는데 "male은" 인덱스가 2인곳에서 존재.
print(student.index("male")) 

# 각각의 index 값을 출력해줌.
for x in student:
    print(x)

if 24 in student:
    print("24 is here")


fruits = (("apple", 20, "10000"), ("banana", 10, "10000"))

print(fruits)

print(fruits[0].count("10000"))



"""
sets 연습
"""
# sets은 순서가 없는 그룹 ,중복이 안됨.
# index가 없음 위 tuple처럼 index로 찾는게 불가능

#실행시키면 순서가 없이 랜덤으로 출력이 됨.
vehicle = {"car", "bike", "horse"}

print("sets의 예시")
for v in vehicle:
    print(v)
print()


# 아래 예시를 보면 중복을 추가해도, 출력시 딱 한개만 나오는것을 볼 수 있다.
print("bike를 여러개 추가 했을때")
vehicle = {"car", "bike", "horse", "bike", "bike"}
for v in vehicle:
    print(v)


#set은 add 함수로 값을 추가할 수 있음

vehicle.add("bus")

for v in vehicle:
    print(v)

# sets은 remove 사용 ,clear도 사용가능.
vehicle.remove("bus")

for v in vehicle:
    print(v)


# update 사용법
extra_vehicle = {"texi", "train", "airplane", "car"}

vehicle.update(extra_vehicle)

for v in vehicle:
    print(v)


print()
print()
print()
# union 사용법

total_vehicle = vehicle.union(extra_vehicle)
for v in total_vehicle:
    print(v)

# different 사용
# 두개의 sets중 첫번째 기준으로 없는것만 출력
print()
print()
print()
print(vehicle.difference(extra_vehicle))

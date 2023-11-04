fruit = ["apple", "banana", "watermelon"]
# list의 표현

"""
print(fruit)
print(fruit[2])

fruit[2] = "strawberry"
print(fruit[2])

for f in fruit:
    print("fruit   " + f)
"""

"""
list. 명령어
"""


"""
fruit.append("watermelon")
print(fruit)

fruit.remove("strawberry")
print(fruit)

fruit.pop() # 마지막 요소를 제거
print(fruit)

#insert(넣을 위치, 값)
fruit.insert(1, "grape")
print(fruit)

fruit.sort()
print(fruit)

fruit.clear()
print(fruit)

"""


"""
2d list
"""

foods = ["cake", "icecream", "candy"]
drinks = ["soda", "water", "tea"]

list = [foods, drinks]

print(list)
print(list[1]) ## drinks가 나옴
print(list[0][0]) ## cake가 나옴
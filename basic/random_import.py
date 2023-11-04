import random

x = random.randint(1, 6)
y = int(random.random() *10)


print ( x, y)

sum = 0
for i in range(y):
    x = random.randint(1, 6)
    sum = sum + x


print(sum)

list = ["가위", "바위" ,"보"]

z= random.choice(list) # list 안에서 랜덤으로 선택하는 함수

print(z)


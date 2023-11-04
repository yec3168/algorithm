
name = None
          
"""
while not name:
    name = input("이름을 입력해주세요.")
    print(name)
"""


"""
for loop 
"""

for i in range(10):
    print(i)

for i in range(50, 55):
    # 첫번쨰인자는 시작
    # 두번쨰 인지는 end
    print(i)
  
for i in range(50, 70,2):
    #세번째 인자는 i를 몇씩 증가할건지
    print(i)

#아래 예시처럼 string 자체가 들어갈 수도 있음
for i in "python programming":
    print(i)


"""
programming example
"""

import time

#for s in range(10, 0, -1):
 #   print(s)
  #  time.sleep(1) #1이 1초임.


"""
이중 반복문
"""

row = int(input("row 수."))
column = int(input("column 수."))
c = input("문자하나.")

for i in range(row):
    for j in range(column):
        print(c, end="")
    print() # 줄바꿈
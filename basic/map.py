# map() 함수

# list, tuple, 등등  각각의 아이템을 반복해서 적용

"""
표현식

map( 함수, 자료형(리스트, 튜플 ))
"""

# 아래 구조는 튜플의 리스트 형식
cloths = [("바지", 20000),
          ("상의", 49000),
          ("신발", 50000),
          ("모자", 10000)]


to_multiple = lambda data: (data[0], data[1]*2) 
#data[0] = "바지", "상의"...
#data[1] = 20000, 49000...

result = map(to_multiple, cloths)

for i in result:
    print(i)



result = list(map(to_multiple, cloths))

print(result)
   
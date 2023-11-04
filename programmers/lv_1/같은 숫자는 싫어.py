#리스트가 주어질 때 리스트는 0~9까지 숫자로 이루어져 있다.
#연속적인 숫자는 하나만 남기고 제거한다.
"""
[1, 1, 3, 3, 0, 1, 1]
= [1, 3, 0 ,1]

[4, 4, 4, 3, 3]
= [4, 3]

"""

def solution(arr):
    position = 0
    list = [arr.pop(0)]
    for i in arr:
        if list[position] != i:
            position +=1
            list.append(i)
    
    return list



list = [1,1,3,3,0,1,1]
print(solution(list))


#다른 사람 풀이

def sol2(arr):
    list = []
    for i in arr:
        # list 맨뒤와 arr[i]와 비교
        if list[-1:] == [i]:
            continue
        list.append(i)
    return list

list = [1,1,3,3,0,1,1]
print(sol2(list))
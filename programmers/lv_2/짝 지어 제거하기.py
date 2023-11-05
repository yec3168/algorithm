"""
문자열에서 같은 알파벳이 2개 붙어 있는 문자열을 찾는다.

그 둘을 제거한 후, 앞뒤의 문자열을 이어 붙인다.

이 과정을 반복하여 문자열이 모두 제거가 된다면 짝지어 제거하기가 종료

"""


# s는 알파벳 소문자로 이루어진 문자열
def solution(s):

    list = []

    for i in s:
        list.append(i)
        if len(list) > 1 and list[-1] == list[-2]:
            list.pop()
            list.pop()
        
    if len(list) ==0:
        return 1

    return 0  

print(solution("baacaacb "))


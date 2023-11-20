from collections import defaultdict
from itertools import combinations

def init_dictionary(clothes):
    init_dict = {}

    for clothe in clothes:
        init_dict[clothe[1]] = 0
    return init_dict

# 마지막 답지 확인
def solution(clothes):
    dic = defaultdict(list)
    
    for clothe in clothes:
        dic[clothe[1]].append(clothe[0])

    # value를 list형태로 다시 만듦
    clothe_list = []
    for key,value in dic.items():
        clothe_list.append(value);
    print(clothe_list)
    
    result = 1

    for value in clothe_list:
        result *= (len(value)+1)

   
    return result -1

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))
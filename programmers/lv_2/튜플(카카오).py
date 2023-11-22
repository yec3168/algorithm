# 원소의 개수가 n개이고 중복이 되는 원소가 없는 튜플이 주어짐
"""
(2, 1, 3, 4)
{2}, {2,1}, {2,1,3},{2,1,3,4}
"""
import re
from collections import Counter

def solution(s):
    s = s.replace("{", "")
    s = s.replace("}", "")
    
    split_list = s.split(",")
    
    counter = Counter(split_list)

    counter = sorted(counter.items(), key=lambda x : x[-1], reverse= True)

    result_list =[]
    for key in counter:
        result_list.append(int(key[0]))
    return result_list



solution("{{2},{2,1},{2,1,3},{2,1,3,4}}")
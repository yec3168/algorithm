import numpy as np
import json
def solution(arr1, arr2):
    arr3=np.array(arr1)
    arr4=np.array(arr2)
    result=np.dot(arr3,arr4)
    return result.tolist()


print(solution([[1, 4], [3, 2], [4, 1]],	[[3, 3], [3, 3]]))
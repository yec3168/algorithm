# 8x8 체스판을 만들기

# 각 칸이 검은색 or 흰색으로 색칠되어 있으면,
# 변을 공유하는 두개의  (왼, 오)은 색이 달라야함.

# 8<= n, m <= 50

import copy
def search_chess(temp):
    global n, m
    result = 1000
    aa = []
    aa= copy.deepcopy(temp)
    for i in range(n):
        for j in range(m):
            if i + 8 <= n and j + 8 <= m: 
                count = 0
                aa =copy.deepcopy(temp)
                for x in range(i, i+8):
                    for y in range(j+1, j+8):
                        #print (x, y)
                        if aa[x][y-1] == aa[x][y]:
                            count +=1
                
                print(count)
                result = min(result, count)
                print("result : ", result)
    return result

n, m = map(int, input().split())

temp = []
for i in range(n):
    s = input()
    temp.append(list(s))

print(search_chess(temp))
   
#미완성
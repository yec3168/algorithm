# 각 카드는 양의 정수.
# 딜러는 n장의 카드 모두 숫자가 보이도록 바닥에 둠
# 딜러는 숫자 m을 크게 외침

# 플레이어가 n장의 카드 중 3장을 고름
# 숫자 m을 넘지 않으면서 m과 가깝게 만듬


# 첫 째줄 입력 n, m
# 둘 째줄 입력 카드에 쓰여 있는 수

# 결과는 m에 가장 가까운 카드 3장


def blackjack(n, m, list):
    #print(n, m, list)
    result = 0
    for i in range(0 , n-2):
        for j in range(i+1, n-1):
            for z in range(j+1, n):
                sum = list[i]+list[j]+list[z]
                #print(sum)
                if result < sum:
                    if sum <= m:
                        result = sum
                        #print(result)
    return result

# 재귀방식
result = 0
def dfs(i, cnt, sum, m, list):
    global result
    
    if cnt == 3 and result < sum and sum <=m:
        result = sum
    elif cnt < 3 and i < len(list):
        dfs(i+1, cnt+1, sum + list[i], m, list)
        dfs(i+1, cnt, sum, m, list)
    
    return result


n, m = map(int, input().split())

list = list(map(int, input().split()))

print(blackjack(n, m, list))

print(dfs(0, 0, 0, m, list))







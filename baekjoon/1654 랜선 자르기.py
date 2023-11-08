# n개의 랜선을 만들어야한다.
# k개 랜선들은 길이가 각각 제각각
# 랜선을 모두 n개의 같은 길이의 랜선으로 만들고 싶다.

"""
ex) 300cm 랜선을 140짜리 랜선을 만들려면 20cm는 버려야함.
"""
# 다시풀어보기 -> 푼 시간 한시간 반( 힌트 참고 )
# 반복문
def binary_search(start, end):
    global nums, k, n, max_cm

    while start <=end:
        mid = int((start+end) / 2)
        cnt = 0
        for i in nums:
            cnt += i // mid
        if cnt >= n:
            start = mid +1
        else:
            end = mid -1
    return end


k, n = map(int, input().split())

nums = []
for i in range(k):
    nums.append(int(input()))

# 이분탐색 
# 제일 앞이랑 제일 끝을 정함 
start, end = 1, max(nums)

print(binary_search(start, end))
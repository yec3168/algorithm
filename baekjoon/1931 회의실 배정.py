# 시작하는시간, 끝나는 시간
# 겹치지않게 회의 수를 최대로 하는 개수를 찾기


# 1번쨰 반복문(?)

# 1 <= N <= 100,000이라 재귀로 풀면 안될 듯
# 시작 시간과 끝나는 시간 이 2^31 -1 이기 때문에 범위도 큼 
 
# 다시풀기
def max_meeting():
    global N, meeting
    cnt = 0
    end = 0
    for i, j in meeting:
        if end <= i:
            cnt +=1
            #print("변하기 전 : " , current_num)
            end = j
            #print("변한 후 : " , current_num)

    return cnt

N = int(input())

meeting = []

for i in range(N):
    meeting.append(list(map(int, input().split())))

meeting.sort(key = lambda x : (x[1], x[0]))  #두 번째 열로 정렬

#print(meeting)
print(max_meeting())

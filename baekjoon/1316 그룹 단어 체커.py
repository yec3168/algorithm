def solution(word):
    for i in range(len(word)):
        pre = i;
        while(1):
            index = word[pre+1:].find(word[i])
            #print(word[pre+1:], index)
            if( index == -1):
                # 발견안함.
                #print(index, word[i], "발견안함")
                break

            if ( pre + index +1> pre+1):
                # 이전 위치 +1 보다 크다면
                #print(index, pre+1 ,"발견했는데 연속되지 않음.")
                return 0
            else:
                #print(pre, index, "갱신")
                pre +=index+1
                
    return 1
    


n = int(input())
result = 0
for i in range(n):
    result += solution(input())

print(result)
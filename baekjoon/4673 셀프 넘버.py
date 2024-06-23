def solution():
    n = 1
    while(n < 100):
        s = str(n)
        for i in range(len(s)):
            n += int(s[i])
        print(n)
#----------------------------------------------------------------
def solution2():
    #시간초과
    n=1
    while(n < 10000):
        f = False;
        for i in range(1, n):
            s = str(i)
            sum = i
            for j in range(len(s)):
                sum += int(s[j])
            if(sum == n):
                f = True
                break
        if(f == False):
            print(n)
        n +=1

#----------------------------------------------------------------

def self_num(n):
    s = list(str(n))
    result = n
    for i in range(len(s)):
        result += int(s[i])
    return result

def solution3():
    result = set()
    for i in range(10000):
        result.add(self_num(i))
    for i in range(10001):
        if i not in result:
            print(i)

solution3()
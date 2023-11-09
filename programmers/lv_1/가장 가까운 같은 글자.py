def solution(s):
    dict = {}
    result =[]
    for i in range(len(s)):
        # 딕셔너리에 문자가 존재하면
        if s[i] in dict:
            result.append(i-dict[s[i]])
        else:
            result.append(-1)
        dict[s[i]] = i
        

    for i, j in dict.items():
        print(i, j)
    return result

print(solution("foobar"))
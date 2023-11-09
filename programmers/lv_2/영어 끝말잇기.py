def solution2(n, words):
    result = []
    speak_word = [[] for _ in range(n)]
   
    count = 0
    find = False
    for word in words:
        #print("speak_word : " , speak_word)
        append_num = (count+n)%n #말하는사람 번호
        count_num = (count+n)//n #말한 횟수
        # 현재단어 첫번째 단어와 아까 넣은 단어 확인
        if count >= 1:
            #print("count 값 :", word[0], words[count-1][-1])
            if word[0] != words[count-1][-1]:
                print("다를 경우")
                result = [append_num+1, count_num]
                find = True
        #       break
        for speak in speak_word:
            #만약 단어가 말한 사람단어중에 존재한다면
            if word in speak:
                print("단어가 존재", append_num+1, count_num)
                result = [append_num+1, count_num]
                find = True
                break
        speak_word[append_num].append(word)
        count +=1

    if find == False:
        result = [0, 0]

    return result

def solution(n, words):
    used_words = []
    number, order = 0,0

    used_words.append(words[0])
    last_word = words[0][-1]
    for i in range(1,len(words)):
        if words[i] not in used_words and words[i][0] == last_word:
            used_words.append(words[i])
            last_word = words[i][-1]
        else:
            number = (i%n)+1
            order = (i//n)+1
            break
    
    return [number, order]

print(solution(2,  ["aba", "aba"] ))

print(solution(3,	["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
print(solution(2,	["hello", "one", "even", "never", "now", "world", "draw"]))
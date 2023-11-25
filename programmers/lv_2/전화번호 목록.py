def solution(phone_book):
    phone_book.sort()

    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
        
    return True


#시간초과
def solution2(phone_book):
    phone_book = sorted(phone_book, key = len)
    for i in range(len(phone_book)- 1):
        for j in range(i+1, len(phone_book)):
            if phone_book[j].startswith(phone_book[i]):
                print("포함", phone_book[i], phone_book[j])
                return False
            else:
                continue
    
    return True

    



print(solution(["119", "97674223", "1195524421"]))
print(solution(["12","123","1235","567","88"]))
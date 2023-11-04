try:
    num = int(input("숫자 입력."))
    a = int(input("나눌 숫자"))
    sum = num / a
    print(sum)
except ZeroDivisionError:
    #0으로 나눌때 생기는 exception 처리
    print("값이 제로")
except ValueError:
    print("숫자가 아닌 값이 들어옴")
except Exception:
    print("에러가 발생")
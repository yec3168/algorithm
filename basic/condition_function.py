age = int(input("나이를 입력 : "))

if age > 19:
    print("성인")
elif age < 0:
    print("잘못 입력하셨습니다")
else:
    print("성인이 아님")


"""
logical operators ( and, or, not)
"""

text = int(input("값을 입력하세요."))

if text >0 and text <30:
    print("F")
elif text <= 0 or text >100:
    print("값을 잘못 입력")
elif text >30:
    print("A~D")
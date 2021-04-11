"""
Created at Demi-Ad
윤년 판별
윤년 이란 4의 배수 면서 100의 배수가 아닌 년도 또는 400의 배수인 년도
"""

user_input: int = int(input("년도를 입력하세요 : "))

if user_input % 4 == 0 and (user_input % 100 != 0 or user_input % 400 == 0):
    print(True)
else:
    print(False)

"""
Created at 2021-04-11
Author Demi-Ad
수식 분기
사용자 입력이 0이상 이라면 CASE A 0미만 이라면 CASE B
"""

user_input = int(input())
answer: int = 0
if user_input >= 0:
    answer = user_input ** 2 + (2 * user_input) + 1  # CASE A
else:
    answer = user_input ** 3 - user_input  # CASE B

print(answer)

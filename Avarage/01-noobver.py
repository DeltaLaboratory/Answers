kor_score = int(input("국어 점수 :"))
eng_score = int(input("영어 점수 :"))
mat_score = int(input("수학 점수 :"))
total = kor_score + eng_score + mat_score
average = total / 3
print("종합 : " + str(total))
print("평균 : " + str(average))
if average >= 80:
    print("잘함")
elif average >= 70:
    print("보통")
else:
    print("미흡")

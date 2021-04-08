from typing import Dict


def main() -> None:
    Scores: Dict[str, int] = {"kor_score": int(input("국어 점수 : ")),
                              "eng_score": int(input("영어 점수 : ")),
                              "math_score": int(input("수학 점수 : "))}
    total: int = sum([Scores[i] for i in Scores.keys()])
    average: int = int(total / 3)
    print(f"총점 : {total}\n평균 : {average}")
    if average >= 80:
        print("잘함")
    elif average >= 70:
        print("보통")
    else:
        print("미흡")
    return


if __name__ == "__main__":
    main()

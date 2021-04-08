import random


def main() -> None:
    num: int = int(input("점수를 입력하세요:"))

    if random.randint(1, 10) == 1:
        print("전산오류")
        return

    if 90 <= num:
        print("A")
    elif 90 > num >= 80:
        print("B")
    elif 80 > num and 70 >= num:
        print("C")
    return


if __name__ == "__main__":
    main()

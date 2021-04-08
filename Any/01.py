def main() -> None:
    for i in range(1, int(input("정수를 하나 입력하세요:"))+ 1):
        print(" ".join([str(_) for _ in range(1, i+1)]))


if __name__ == "__main__":
    main()

def main() -> None:
    Chars = "abcdefghijklmnopqrstuvwxyz"
    Shift = int(input())
    String = input()
    if String in Chars:
        print(Chars[(Chars.find(String) + Shift) % len(Chars)])
        return
    else:
        raise ValueError


if __name__ == "__main__":
    main()

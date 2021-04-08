"""
변수 a,b에 정수 값을 입력받고,
두 값을 더한값과 두 값을 곱한값을 구한다.
두 값중 더 큰 값에서 작은 값을 뺀 결과값이
8보다 작으면 a,b를 Swap(교환)한다.
최종 결과를 출력하는 프로그램을 작성하라"
"""


def main() -> None:
    a: int = int(input())
    b: int = int(input())
    p: int = a + b
    m: int = a * b

    if p > m:
        if p - m < 8:
            print(f"a = {b}, b = {a}")
        else:
            print(f"a = {a}, b = {b}")
    if p < m:
        if m - p < 8:
            print(f"a = {b}, b = {a}")
        else:
            print(f"a = {a}, b = {b}")
    
    return


if __name__ == "__main__":
    main()

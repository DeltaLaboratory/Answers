a = int(input())
c = int(input())
p = a + c
m = a * c

if p > m:
    print("Result = ", (p - m))
    if p - m < 8:
        print("Swap!!")
        print("a =", c, ", b =", a)
    else:
        print("a =", a, ", b =", c)
if p < m:
    print("Result =", (m - p))
    if m - p < 8:
        print("Swap!!")
        print("a =", c, ", b =", a)
    else:
        print("a =", a, ", b =", c)

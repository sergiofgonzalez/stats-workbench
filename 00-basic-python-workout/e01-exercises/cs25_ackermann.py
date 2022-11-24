import sys


def ackermann(m: int, n: int) -> int:
    if m == 0:
        return n + 1
    elif n == 0:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n - 1))


print(f"ackermann(2, 2)={ackermann(2, 2)}")
print(f"ackermann(2, 1)={ackermann(2, 1)}")


try:
    print(f"ackermann(4, 3)={ackermann(4, 3)}")
except Exception as e:
    print(f"ERROR: {e}")
    print(f"sys.getrecursionlimit()={sys.getrecursionlimit()}")

# fails with a segmentation fault even if bumping up the recursion limit
sys.setrecursionlimit(100000)
print(f"ackermann(5, 0)={ackermann(5, 0)}")

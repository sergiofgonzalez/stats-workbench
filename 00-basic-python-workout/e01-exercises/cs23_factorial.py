def factorial(n: int) -> int:
    def calc_factorial(n):
        if n == 0:
            return 1
        else:
            return n * calc_factorial(n - 1)

    if not isinstance(n, int):
        print("n must be a non-negative integer")
        raise SystemExit()

    result = calc_factorial(n)
    return result


print(f"5!={factorial(5)}")

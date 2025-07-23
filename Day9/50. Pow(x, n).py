def myPow(self, x: float, n: int) -> float:
    if x == 0:
        return 0
    if n == 0:
        return 1

    if n < 0:

        x = 1 / x
        n *= -1

    a = self.myPow(x, n // 2)

    if n % 2 == 0:
        return a * a
    return a * a * x

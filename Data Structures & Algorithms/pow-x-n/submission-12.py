class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0

        condition_1: bool = -100.0 < x < 100.0
        condition_2: bool = -1_000 <= n <= 1_000
        condition_3: bool = type(n).__name__ == "int"

        if condition_1 and condition_2 and condition_3:
            if n == 0:
                return 1
            else:
                result: int = 1
                for index in range(abs(n)):
                    result *= x
                
                if n > 0:
                    return result
                else:
                    return 1 / result
            
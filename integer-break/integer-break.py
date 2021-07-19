class Solution:
    def integerBreak(self, n: int) -> int:
        # 7 = 3 + 4 = 12  ---------->  7 % 3 = 1
        # 8 = 3 + 3 + 2 = 18 ------->  8 % 3 = 2
        # 9 = 3 + 3 + 3 = 27 ------->  9 % 3 = 0
        # 10 = 3 + 3 + 4 = 36 ------> 10 % 3 = 1
        # 11 = 3 + 3 + 3 + 2 = 54 --> 11 % 3 = 2
        # 12 = 3 + 3 + 3 + 3 = 81 --> 12 % 3 = 0
        # 3 is most important. So we just multiply number of 3s in the factor
        # Then if there's a remainder of 1, we subtract a multiple of 3 and multiply by 4 instead
        # Remainder of 2, you multiply by 2 after
        # Remainder 0 is just straight up answer
        if n <= 3:
            return n-1
        elif n % 3 == 0:
            return 3 ** (n // 3)
        elif n % 3 == 1:
            return 3 ** (n // 3 - 1) * 4
        elif n % 3 == 2:
            return 3 ** (n // 3) * 2
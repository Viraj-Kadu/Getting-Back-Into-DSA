class Solution:
    def smallestNumber(self, n: int) -> int:
        b = n.bit_length()
        ans = 0
        for i in range(0,b):
            ans += 2**i
        return ans

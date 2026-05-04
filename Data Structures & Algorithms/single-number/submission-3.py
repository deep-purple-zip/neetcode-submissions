class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result: int = 0
        for number in nums:
            result ^= number
        return result
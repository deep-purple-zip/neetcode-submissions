class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        frequencies: dict[int, int] = {}
        for number in nums:
            if number in frequencies:
                frequencies[number] += 1
            else:
                frequencies[number] = 1
        return [key for key in frequencies if frequencies[key] == 1][0]
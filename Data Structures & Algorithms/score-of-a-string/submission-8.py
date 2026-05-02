class Solution:
    def scoreOfString(self, s: str) -> int:
        length: int = len(s)
        if 2 <= length <= 100 and s.islower():
            characters: list[str] = list(s)
            sum: int = 0
            for i in range(length - 1):
                sum += abs(ord(characters[i]) - ord(characters[i+1]))
            return sum
        return 0

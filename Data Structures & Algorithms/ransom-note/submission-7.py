class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        target: str = ransomNote
        candidate_characters: str = magazine
        frequencies: dict[str, int] = {}
        for character in candidate_characters:
            frequencies[character] = candidate_characters.count(character)
        for character in target:
            if not character in frequencies:
                return False
            else:
                frequencies[character] -= 1
                if frequencies[character] < 0:
                    return False
        return True

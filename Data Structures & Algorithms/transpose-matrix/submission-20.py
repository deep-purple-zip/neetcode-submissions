class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n: int = len(matrix)
        m: int = len(matrix[0])
        if 1 <= m <= 1_000 and 1 <= m <= 1_000 and 1 <= m * n <= 100_000:
            result: list[list[int]] = []
        
            for j in range(m):
                row: list[int] = []
                for i in range(n):
                    row.append(matrix[i][j])
                result.append(row)
            return result
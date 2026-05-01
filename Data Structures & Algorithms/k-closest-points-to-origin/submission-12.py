from math import sqrt

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = lambda point: sqrt(point[0] ** 2 + point[1] ** 2)
        distances: list[tuple[int, float]] = [
            (index, distance(point))
            for index, point in enumerate(points)
        ]
        distances.sort(key=lambda tuple_: tuple_[1])
        k_min_indices: list[int] = [distances[i][0] for i in range(k)]
        return [points[index] for index in k_min_indices]
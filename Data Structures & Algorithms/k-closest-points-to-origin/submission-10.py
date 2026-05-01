from math import sqrt

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances: list[tuple[int, float]] = []
        distance = lambda point: sqrt(point[0] ** 2 + point[1] ** 2)
        for index, point in enumerate(points):
            distances.append((index, distance(point)))
        distances.sort(key=lambda tuple_: tuple_[1])
        k_min_distances: list[tuple[int, float]] = distances[:k]
        k_min_indices: list[int] = [index for index, distance in k_min_distances]
        return [points[index] for index in k_min_indices]
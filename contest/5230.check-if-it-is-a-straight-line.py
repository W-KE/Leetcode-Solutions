class Solution:
    def function(self, x):
        return self.a * x + self.b

    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        xs = len(set(map(lambda x: x[0], coordinates)))
        ys = len(set(map(lambda x: x[1], coordinates)))
        if xs == 1 or ys == 1:
            return True
        if xs < len(coordinates) or ys < len(coordinates):
            return False
        self.a = (coordinates[1][1] - coordinates[0][1]) / (coordinates[1][0] - coordinates[0][0])
        self.b = coordinates[0][1] - self.a * coordinates[0][0]
        for coordinate in coordinates[2:]:
            if self.function(coordinate[0]) != coordinate[1]:
                return False
        return True

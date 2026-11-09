class Solution:
    # time = (target - position[i]) / speed[i]
    # time < min time increase fleet by 1
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet = 0
        cars = list(zip(position, speed))
        maxTime = 0
        for p, v in sorted(cars, reverse=True):
            t = (target - p) / v
            if t > maxTime:
                maxTime = t
                fleet += 1
        return fleet
        
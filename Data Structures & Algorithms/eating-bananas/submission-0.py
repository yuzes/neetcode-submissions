class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        minSpeed = 1
        maxSpeed = max(piles)
        while minSpeed < maxSpeed:
            mid = (maxSpeed + minSpeed) // 2
            total = 0
            for p in piles:
                total += math.ceil(p / mid)
            if total <= h:
                # slow down
                maxSpeed = mid
            else:
                # speedUp
                minSpeed = mid + 1
        return maxSpeed

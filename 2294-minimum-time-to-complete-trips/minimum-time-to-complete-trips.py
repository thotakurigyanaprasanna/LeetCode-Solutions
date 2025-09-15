class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        left, right = 1, min(time) * totalTrips
        ans = right
        
        while left <= right:
            mid = (left + right) // 2
            
            trips = sum(mid // t for t in time)
            
            if trips >= totalTrips:
                ans = mid
                right = mid - 1  # try smaller time
            else:
                left = mid + 1  # need more time
        
        return ans
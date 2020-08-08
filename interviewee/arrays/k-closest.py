class Solution(object):
    def findClosestElements(self, arr, k, x):
        if arr is None or len(arr) == 0:
            return []
        
        closest = self.binarySearch(arr,k,x)
        left = closest
        right = closest

        while right - left + 1 < k and left > 0 and right < len(arr) - 1:
            if abs(arr[left - 1] - x) <= abs(arr[right + 1] - x):
                left -= 1
            else:
                right += 1

        while right - left + 1 < k:
            if left > 0:
                left -= 1
            else:
                right += 1
        
        return arr[left:right+1]


    def binarySearch(self,arr,k,x):
        left = 0
        right = len(arr) - 1
        closest = -1
        minDiff = float("inf")

        while left <= right:
            mid = left + (right - left) // 2
            cand = arr[mid]
            if abs(cand - x) < minDiff:
                minDiff = abs(cand - x)
                closest = mid

            if cand == x:
                return mid
            
            elif cand < x:
                left = mid + 1
            
            else:
                right = mid - 1

        return closest

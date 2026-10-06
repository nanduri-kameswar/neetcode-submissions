class Solution:
    def findMin(self, nums: List[int]) -> int:
        minVal = float("inf")
        l, r = 0, len(nums)-1
        while l <= r:
            m = (l+r)//2
            if nums[m] >= nums[l]:
                # sorted half
                minVal = min(minVal, nums[l])
                l = m+1
            else:
                minVal = min(minVal, nums[m], nums[r])
                r = m-1
        return minVal
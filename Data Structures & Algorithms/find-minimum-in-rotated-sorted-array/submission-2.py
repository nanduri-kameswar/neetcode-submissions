class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        # Time: O(logn), Space: O(1)
        while l < r:
            m = (l+r)//2
            # min lies on (m, r]
            if nums[m] > nums[r]:
                l = m+1
            # min lies on [l, m]
            else:
                r = m
        return nums[l]
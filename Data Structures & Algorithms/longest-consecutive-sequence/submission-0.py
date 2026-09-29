class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Brute Force - Time: O(nlogn), Space: O(1)
        n = len(nums)
        if n == 0 or n == 1:
            return n
        nums.sort()
        max_count = 0
        count = 1
        for i in range(1, n):
            if nums[i-1] == nums[i]:
                continue
            if nums[i] - nums[i-1] == 1:
                count += 1
            else:
                max_count = max(max_count, count)
                count = 1
        return max(max_count, count)
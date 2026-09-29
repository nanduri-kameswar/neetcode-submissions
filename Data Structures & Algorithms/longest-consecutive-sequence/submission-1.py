class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # check the sequence start numbers
        n = len(nums)
        seen = set(nums)
        max_count = 0
        for i in nums:
            if i-1 not in seen: # if a number-1 is not in hash set or original array, it can't start a sequence
                count = 0
                while i+count in seen:
                    count += 1
                    max_count = max(count, max_count)
        return max_count


            
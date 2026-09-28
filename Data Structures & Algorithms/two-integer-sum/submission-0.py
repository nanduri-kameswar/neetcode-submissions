class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i, n in enumerate(nums):
            rem = target - n
            if rem in hash_map:
                return [hash_map[rem], i]
            else:
                hash_map[n] = i
        
class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Time: O(n), Space: O(n)
        """

        # Base case: In case of a single house, rob it
        if len(nums) == 1:
            return nums[0]

        # Rob a non-circular houses
        def rob_linear(arr: list[int]) -> int:
            prev, curr = 0, 0
            for x in arr:
                prev, curr = curr, max(curr, prev+x)
            return curr
        # Logic: Maximun of Rob(1st house till last but one) OR Rob(2nd house till last)
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))
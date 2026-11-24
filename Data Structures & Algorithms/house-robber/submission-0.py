class Solution:
    def rob(self, nums: List[int]) -> int:
        # Dynamic Programming
        # Time: O(n), Space: O(1)
        """
        logic is skip now and take max till now or steal now and take max till prev
        dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        """
        prev, curr = 0, 0
        for x in nums:
            prev, curr = curr, max(curr, prev+x)
        return curr
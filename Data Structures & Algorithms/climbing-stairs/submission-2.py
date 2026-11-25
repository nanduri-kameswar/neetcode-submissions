class Solution:
    def climbStairs(self, n: int) -> int:
        # Base case: n = 1 --> return 1
        # n = 2 --> 2
        # n = 3 --> (n=2) and (n=1) = 3
        # n = 4 --> (n=3) and (n=2) = 3+2 = 5
        """ Memoization - Top Down """
        # if n==1 or n==2:
        #     return n
        # return self.climbStairs(n-1) + self.climbStairs(n-2)
        """ Tabulation - Bottom Up """
        # Time: O(n), Space: O(1)
        if n <= 2:
            return n
        prev, curr = 1, 2
        for x in range(3, n+1):
            prev, curr = curr, prev+curr
        return curr


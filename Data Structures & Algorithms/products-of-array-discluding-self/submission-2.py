class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0]*n
        """
        Brute Force Solution - Time: O(n^2), Space: O(n)
        """
        # for i, n in enumerate(nums):
        #     product = 1
        #     for j in range(n):
        #         if i==j:
        #             continue
        #         product *= nums[j]
        #     res.append(product)
        # return res

        """
        Better Solution - Time: O(n), Space: O(n)
        """
        # prefProd = [1]*n # stores prefix product till i (arr[0]*...*arr[i-1])
        # suffProd = [1]*n # stores suffix product till i (arr[n]*...*arr[i+1])

        # for i in range(1, n):
        #     prefProd[i] = prefProd[i-1] * nums[i-1]
        
        # for j in range(n-2, -1, -1):
        #     suffProd[j] = suffProd[j+1] * nums[j+1]
        
        # for i in range(n):
        #     res[i] = prefProd[i]*suffProd[i]

        # return res
        """
        Optimal Solution (math logic) - Time: O(n), Space: O(1)
        """
        # zeroes, zeroth_idx = 0, 0
        # product = 1
        # for i, e in enumerate(nums):
        #     if e == 0:
        #         zeroes += 1
        #         zeroth_idx = i
        #         continue
        #     product *= nums[i]

        # if zeroes == 0:
        #     for i in range(n):
        #         res[i] = int(product/nums[i])
        # elif zeroes == 1:
        #     res[zeroth_idx] = product

        # return res 

        """
        Optimal Solution - Time: O(n), Space: O(1)
        """
        res = [1]*n
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(n-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res
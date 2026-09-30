class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        n = len(heights)
        left, right = 0, n-1
        # Two pointer approach
        while left < right:
            area = min(heights[left], heights[right])*(right - left)
            max_area = max(area, max_area)
            # move the smallest height pointer to next because
            # 
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        return max_area

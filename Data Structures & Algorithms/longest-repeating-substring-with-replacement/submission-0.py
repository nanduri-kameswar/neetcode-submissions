class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        n = len(s)
        res = 0
        count_map = {}
        # Time: O(26.n) = O(n), Space: O(26) = O(1)
        while l < n and r < n:
            count_map[s[r]] = count_map.get(s[r], 0) + 1 # O(26) operation
            window_length = r - l + 1
            max_repeated_char = max(count_map.values())
            if window_length - max_repeated_char <= k:
                res = max(res, window_length)
            else:
                count_map[s[l]] -= 1
                l += 1
            r += 1
        return res
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        n = len(s)
        res = 0
        count_map = {}
        # Time: O(26.n) = O(n), Space: O(26) = O(1)
        for r in range(n):
            count_map[s[r]] = count_map.get(s[r], 0) + 1 # O(26) operation
            max_repeated_char = max(count_map.values())
            while (r - l + 1) - max_repeated_char > k:
                count_map[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Time: O(n), Space: O(n)
        n = len(s)
        subStringSet = set()
        max_size = 0
        l = 0
        # logic: as it is non-repeating, add current char to set
        # if new otherwise if it is already found, remove the previous 
        # indices char until current char is removed 
        # and update max_size accordingly
        for r in range(n):
            while s[r] in subStringSet:
                subStringSet.remove(s[l])
                l += 1
            subStringSet.add(s[r])
            max_size = max(max_size, r-l+1)
        return max_size
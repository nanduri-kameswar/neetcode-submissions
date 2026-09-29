class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(char for char in s if char.isalnum()).lower()
        """
        Brute Force - Time: O(n), Space: O(1)
        """
        # if s == s[::-1]:
        #     return True
        # return False
        """
        Better Solution - Time: O(n), Space: O(1)
        """
        i, j = 0, len(s)-1
        while i<j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
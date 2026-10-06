class Solution:
    def isValid(self, s: str) -> bool:
        # Time: O(n), Space: O(n)
        stack = []
        for i in s:
            if i in ['(', '[', '{']:
                stack.append(i)
                continue
            if len(stack) == 0:
                return False
            x = stack.pop()
            if x+i not in ['()', '{}', '[]']:
                return False
        return True if len(stack) == 0 else False
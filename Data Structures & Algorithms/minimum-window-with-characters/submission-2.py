class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        
        l = 0
        res, resLen = [-1, -1], float("inf")
        have, need = 0, len(countT)
        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1
            # we care only the chars in s which are in t
            if c in countT and window[c] == countT[c]:
                have += 1
                # decrease window size and verify to get min length
                while have == need:
                    if r-l+1 < resLen:
                        res = [l, r]
                        resLen = r-l+1
                    window[s[l]] -= 1
                    if s[l] in countT and window[s[l]] < countT[s[l]]:
                        have -= 1
                    l += 1
        return s[res[0]: res[1]+1] if resLen != float('inf') else ""
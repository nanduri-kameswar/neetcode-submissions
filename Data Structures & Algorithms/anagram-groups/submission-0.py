class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list)
        for s in strs:
            count = [0]*26
            for c in s:
                i = ord(c) - ord("a")
                count[i] += 1
            hash_map[tuple(count)].append(s)
        return [item for item in hash_map.values()]
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = defaultdict(int) # to count the frequency of numbers
        count_array = [[] for i in range(len(nums)+1)] # to map the numbers as a list, considering key as the count
        for n in nums:
            hash_map[n] += 1
        for key, val in hash_map.items():
            count_array[val].append(key)
        res = []
        # from end to start, when there is a value for certain count, add it to result
        for i in range(len(count_array)-1, 0, -1):
            for n in count_array[i]:
                res.append(n)
                if len(res) == k:
                    return res
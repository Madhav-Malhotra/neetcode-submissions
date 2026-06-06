from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Phase 1: count frequencies w/ hashmap
        # O(n) time and O(n) space (worst case = all unique)
        count = defaultdict(int)
        for n in nums: 
            count[n] += 1

        # Phase 2: bucket sort given unique answer guarantee
        # O(n) time and O(n) space (worst case = all unique)
        buckets = [[] for _ in range(len(nums) + 1)]
        for num,count in count.items():
            buckets[count].append(num)

        # Phase 3: Return k largest counts
        out = []
        for i in range(len(buckets) - 1, -1, -1):
            for n in buckets[i]:
                out.append(n)
                if len(out) == k:
                    return out
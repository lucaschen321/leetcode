from collections import Counter, heapq, defaultdict
from typing import List


class Solution1:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = defaultdict(list)
        for key, cnt in Counter(nums).items():
            frequency[cnt].append(key)

        top_k = []
        for i in reversed(range(len(nums) + 1)):
            top_k.extend(frequency[i])  # frequency[i] creates and returns empty list if key not found
            if len(top_k) >= k:
                return top_k[:k]

        return top_k[:k]


class Solution2:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = Counter(nums)
        return heapq.nlargest(k, frequency.keys(), key=frequency.get)

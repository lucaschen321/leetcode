from collections import Counter, defaultdict
from typing import List


# Solution 1: Use sorted string as key.
class Solution1:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_dict = defaultdict(list)
        for s in strs:
            anagrams_dict[tuple(sorted(s))].append(s)
        return anagrams_dict.values()


# Solution 2: Use frequency as key.
class Solution2:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_dict = defaultdict(list)
        for s in strs:
            s_frequency = tuple(sorted(Counter(s).items()))
            anagrams_dict[s_frequency].append(s)
        return anagrams_dict.values()

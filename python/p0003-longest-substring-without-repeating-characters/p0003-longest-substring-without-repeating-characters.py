class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, max_length = 0, 0
        substring_set = set()
        for r in range(len(s)):
            if s[r] in substring_set:
                while s[left] != s[r] and s[left] in substring_set:
                    substring_set.remove(s[left])
                    left += 1
                left += 1
            else:
                substring_set.add(s[r])

            max_length = r - left + 1 if r - left + 1 > max_length else max_length

        return max_length

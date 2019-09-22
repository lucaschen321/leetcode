from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_frequency = Counter(t)
        window_frequency = Counter()
        left = 0
        num_unique_t_chars_in_window = 0  # Keep track of how many unique characters in t are present in current window in desired frequency.

        min_substring = s

        for right in range(len(s)):
            window_frequency[s[right]] += 1

            # After window is initially formed, always have window_frequency.get(s[right]) > t_frequency.get(s[right], 0):
            if window_frequency.get(s[right]) == t_frequency.get(s[right], 0):
                num_unique_t_chars_in_window += 1

            if num_unique_t_chars_in_window == len(t_frequency):
                while s[left] not in t_frequency or window_frequency[s[left]] > t_frequency[s[left]]:
                    window_frequency[s[left]] -= 1
                    left += 1

                min_substring = min_substring if len(min_substring) <= right - left + 1 else s[left:right + 1]

        return min_substring if num_unique_t_chars_in_window == len(t_frequency) else ""

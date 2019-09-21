from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0

        character_frequency = defaultdict(int)
        character_frequency[s[0]] += 1  # Include 1st character so character_frequency.values() isn't empty
        left, right, max_substring = 0, 1, 0

        while right < len(s):
            most_common_character_frequency = max(character_frequency.values())
            if (right - left) - most_common_character_frequency < k or \
               character_frequency[s[right]] == max(character_frequency.values()):
                # If (right - left) - most_common_character_frequency = k, only
                # increment right if it is a most common character (there may be
                # more than one)
                character_frequency[s[right]] += 1
                right += 1
            else:
                character_frequency[s[left]] -= 1
                left += 1

            max_substring = max(max_substring, right - left)

        return max_substring

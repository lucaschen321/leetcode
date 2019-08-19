from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def backtrack(digits, keypad, ans, letter_combination, i):
            if i == len(digits):  # End of digits has been reached
                ans.append(letter_combination)
                return
            else:
                for char in keypad[digits[i]]:
                    backtrack(digits, keypad, ans, letter_combination + char, i + 1)

        keypad = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        ans, letter_combination = [], ""

        if digits:
            backtrack(digits, keypad, ans, letter_combination, 0)

        return ans

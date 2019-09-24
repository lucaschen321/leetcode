class Solution1:
    def countSubstrings(self, s: str) -> int:
        is_palindrome = [[0 for i in range(len(s))] for j in range(len(s))]
        num_palindromes = 0

        for i in reversed(range(len(s))):  # Need to reverse to fill in DP array in correct order.
            for j in range(i, len(s)):
                if i == j or i + 1 == j:
                    is_palindrome[i][j] = 1 if s[i] == s[j] else 0
                elif i < j:
                    is_palindrome[i][j] = 1 if is_palindrome[i + 1][j - 1] and s[i] == s[j] else 0

                num_palindromes += is_palindrome[i][j]

        return num_palindromes


class Solution2:
    def countSubstrings(self, s: str) -> int:
        def num_palindromes_centered_at_ij(i, j):
            num_palindromes = 0

            while 0 <= i and j < len(s) and s[i] == s[j]:
                i, j = i - 1, j + 1
                num_palindromes += 1

            return num_palindromes

        num_palindromes = 0
        for i in range(len(s)):
            num_palindromes += num_palindromes_centered_at_ij(i, i)  # palindromes with s[i] as center
            num_palindromes += num_palindromes_centered_at_ij(i, i + 1)  # palindromes with s[i], s[i+1] as center

        return num_palindromes

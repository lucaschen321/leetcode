#include "leetcode.h"
#include <ctime>
#include <functional>
using namespace std;

class Solution {
public:
    string longestPalindrome(string s) {
        // Even positions represent strings; odd positions represent the empty string
        int max_palindrome_left = 0;
        int max_palindrome_length = 1;
        int palindrome_length;
        int palindromes[2 * s.size() - 1];
        int left, right, radius;
        int next;
        bool equal;
        for (int center = 0; center < 2 * s.size() - 1; center = next) {
            radius = 0;
            left = center - 1, right = center + 1;
            next = center + 1;
            equal = true;
            while (left >= 0 && right < 2 * s.size() - 1 && equal) {
                if (left % 2 == 0 && s.at(left / 2) != s.at(right / 2)) {
                    equal = false;
                } else {
                    palindromes[right] = palindromes[left];
                    radius++;
                    left--;
                    right++;
              }
            }
            if (left < 0 || right >= 2 * s.size() - 1)
            	radius++;

            palindromes[center] = radius;
            palindrome_length = radius;
            if (palindrome_length > max_palindrome_length) {

                max_palindrome_left = (left + 2) / 2;
                max_palindrome_length = palindrome_length;
            }

            // right is the first position where s[left] != s[right]
            while (next < right - 1 && next + palindromes[next] < right - 1) {
                next++;
            }
        }
        return s.substr(max_palindrome_left, max_palindrome_length);
    }
};

class Solution2 {
public:
    string longestPalindrome(string s){
        int left, right;
        string max_palindrome = "";
        for (int i = 0; i < 2 * s.size() - 1; i++) {
            if (i % 2 == 0) {
                left = i / 2;
                right = i / 2;
            }
            else {
                left = i / 2;
                right = i / 2 + 1;
            }
            while (left >= 0 && right < s.size() && s.at(left) == s.at(right)) {
                left--;
                right++;
            }
            if (right - left - 1 > max_palindrome.size()) {
                max_palindrome = s.substr(left + 1, right - left - 1);
            }
        }
        return max_palindrome;
    }

};

int main() {
    Solution s;
    Solution2 s2;
    string str = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa";
    // cin >> str;
    clock_t start = clock();

    cout << s.longestPalindrome(str) << endl;

    int ms = (clock() - start) / (double) (CLOCKS_PER_SEC / 1000);

    cout << "Manachers' Finished in " << ms << "ms" << std::endl;

    start = clock();

    cout << s2.longestPalindrome(str) << endl;

    ms = (clock() - start) / (double) (CLOCKS_PER_SEC / 1000);

    cout << "Alternative Finished in " << ms << "ms" << std::endl;
}

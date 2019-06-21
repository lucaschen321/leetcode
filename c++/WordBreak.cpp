/*
 * Solution to LeetCode Problem 139
 * Source: https://leetcode.com/problems/word-break/description/
 * Author: Lucas Chen
 */

/*
 * Description:
 * Given anon-emptystringsand a dictionarywordDictcontaining a list ofnon-
 * emptywords, determine ifscan be segmented into a space-separated sequence of one
 * or more dictionary words.Note:The same word in the dictionary may be reused
 * multiple times in the segmentation.You may assume the dictionary does not
 * contain duplicate words.Example 1:Input:s = "leetcode", wordDict = ["leet",
 * "code"]Output:trueExplanation:Return true because"leetcode"can be segmented
 * as"leet code".Example 2:Input:s = "applepenapple", wordDict = ["apple",
 * "pen"]Output:trueExplanation:Return true because"applepenapple"can be segmented
 * as"apple pen apple".
 *              Note that you are allowed to reuse a dictionary word.Example
 * 3:Input:s = "catsandog", wordDict = ["cats", "dog", "sand", "and",
 * "cat"]Output:false
 */

#include "leetcode.h"

class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        unordered_set<string> setDict(wordDict.begin(), wordDict.end());
        vector<bool> canBreak(s.length());

        for (int i = 0; i < s.length(); i++) {
            if (setDict.find(s.substr(0, i+1)) != setDict.end()) {
                canBreak[i] = true;
            }
            for (int j = 0; j < i; j++) {
                if (canBreak[j]  && setDict.find(s.substr(j+1,i-j)) != setDict.end()){
                    canBreak[i] = true;
                    break;
                }
            }
            cout << canBreak[i] <<endl;
        }
        return canBreak[s.length() - 1];
    }
};

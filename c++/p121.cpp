#include "leetcode.h"

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int currentMin = 0, profit = 0;
        for (int i = 1; i < prices.size(); i++) {
            if (prices[i] < prices[currentMin]){
                currentMin = i;
            }
            if (prices[i] - prices[currentMin] > profit){
                profit = prices[i] - prices[currentMin];
            }
        }
        return profit;
    }
};

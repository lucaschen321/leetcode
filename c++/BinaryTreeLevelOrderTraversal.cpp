#include "leetcode.h"

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        if (root == NULL) {
            return {};
        }

        vector <vector<string> > big;
        big.push_back( vector<string>() );
        queue<TreeNode*> q;
        q.push(root);

        vector<vector<int>> ans;
        ans.push_back(vector<int>());
        int nodesInCurrentLevel = 1;
        int nodesInNextLevel = 0;

        while (!q.empty()) {
            TreeNode* node = q.front();
            ans.back().push_back(node->val);
            q.pop();
            nodesInCurrentLevel--;

            if (node->left != NULL) {
                q.push(node->left);
                nodesInNextLevel++;
            }

            if (node->right != NULL) {
                q.push(node->right);
                nodesInNextLevel++;
            }

            if (nodesInCurrentLevel == 0 && nodesInNextLevel > 0) {
                ans.push_back(vector<int>());
                nodesInCurrentLevel = nodesInNextLevel;
                nodesInNextLevel = 0;
            }


        }
        return ans;
    }
};

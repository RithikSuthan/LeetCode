#include<vector>
#include<algorithm>
class Solution {
public:
    int longestValidParentheses(string s) {
        vector<int> stack;
        stack.push_back(-1);
        int max_ans=0;
        for(int i=0;i<s.size();i++)
        {
            if(s[i]=='(')
            {
                stack.push_back(i);
            }
            else
            {
                stack.pop_back();
                if(stack.empty())
                {
                    // cout<<"FD";
                    stack.push_back(i);
                }
                max_ans=max(max_ans,i-stack[stack.size()-1]);
            }
        }
        return max_ans;
    }
};
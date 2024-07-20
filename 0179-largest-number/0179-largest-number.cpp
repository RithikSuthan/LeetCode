#include<vector>
#include<algorithm>
#include<string>
class Solution {
public:
    bool static compare(string &a,string &b)
    {
        return a+b>b+a;
    }
    string largestNumber(vector<int>& nums) {
        vector<string> array;
        string ans;
        for(int i=0;i<nums.size();i++)
        {
            array.push_back(to_string(nums[i]));
        }
        sort(array.begin(),array.end(),compare);
        for(int i=0;i<array.size();i++)
        {
            ans=ans+array[i];
        }
        if (ans[0]=='0'){
            return "0";
        }
        return ans;

    }
};
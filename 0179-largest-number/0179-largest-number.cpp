class Solution {
public:
    static bool compare(string &a,string &b)
    {
        return a+b>b+a;
    }
    string largestNumber(vector<int>& nums) {
        vector<string> array;
        for(int i=0;i<nums.size();i++)
        {
            array.push_back(to_string(nums[i]));
        }
        sort(array.begin(),array.end(),compare);
            string answer="";
    for(auto it=array.begin();it!=array.end();it++)
    {
        answer+=*it;
    }
    if(answer[0]=='0')
    {
        return "0";
    }
    return answer;
    }


};
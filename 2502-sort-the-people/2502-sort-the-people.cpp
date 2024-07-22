class Solution {
public:
    vector<string> sortPeople(vector<string>& names, vector<int>& heights) {
        map<int,string> high;
        for(int i=0;i<heights.size();i++)
        {
            high[heights[i]]=names[i];
        }
        sort(heights.begin(),heights.end(),greater<int>());
        vector<string> ans;
        for(int i=0;i<heights.size();i++)
        {
            ans.push_back(high[heights[i]]);
        }
        return ans;
    }
};
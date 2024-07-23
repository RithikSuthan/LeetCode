class Solution {
public:
   static bool compare(pair<int,int>a,pair<int,int>b)
    {
        return a.second<b.second;
    }
    void freq(int search,vector<int> & nums,map<int,int> &dummy)
    {
        int freq=0;
        for(int i=0;i<nums.size();i++)
        {
            if(nums[i]==search)
            {
                freq+=1;
            }
        }        
        dummy[search]=freq;
    }

    vector<int> frequencySort(vector<int>& nums) {
        map<int,int> dummy;
        vector<int> ans;
        set<int> st;
        for(int i=0;i<nums.size();i++)
        {
            st.insert(nums[i]);
        }    
        for(auto &i:st)
        {
            freq(i,nums,dummy);
        }
        vector<pair<int,int>> array;
        for(auto &i:dummy)
        {
            array.push_back({i.first,i.second});
        }
        reverse(array.begin(),array.end());
        stable_sort(array.begin(),array.end(),compare);
          for(int i=0;i<array.size();i++)
        {
           cout<<array[i].first<<":"<<array[i].second<<endl;
        }
        for(auto &a:array)
        {

            for(int z=0;z<a.second;z++)
            {
                ans.push_back(a.first);
            }
            // cout<<a.first<<" "<<a.second<<endl;
        }
        return ans;
    }
};
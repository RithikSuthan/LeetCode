class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int count=0;
        for(auto it=nums.begin();it!=nums.end();)
        {
            if(*it==0)
            {
                nums.erase(it);
                count+=1;
            }
            else
            {
                it++;
            }
        }
        for (int i=0;i<count;i++)
        {
            nums.push_back(0);
        }
    }
};
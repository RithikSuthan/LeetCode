class Solution {
public:
    int titleToNumber(string columnTitle) {
        long long unsigned int ans=0;
        map<char,int> map1;
        for(int i=65;i<91;i++)
        {
            map1[static_cast<char>(i)]=i-64;
        }
        long long unsigned int count=1;
        for(int i=columnTitle.length()-1;i>0-1;i--)
        {
            for(auto &ele:map1)
            {
                if (ele.first==columnTitle[i])
                {
                    ans+=ele.second*count;
                    count*=26;
                }
            }

        }
    return ans;
    }
};
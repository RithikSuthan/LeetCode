class Solution {
public:
    vector<string> commonChars(vector<string>& words) {
       vector<string> frequency;
       for (auto &chr:words[0])
       {
            int count=0;
            for(int i=1;i<words.size();i++)
            {
                // cout<<words[i];
                for(auto &ch:words[i])
                {
                    if (ch==chr)
                    {
                        count+=1;
                        ch='-';
                        break;
                    }
                }
            }
            // cout<<count<<endl;
            if (count+1==words.size())
            {
                count=0;
                frequency.push_back(std::string(1,chr));
            }
       } 
       return frequency;
    }
};
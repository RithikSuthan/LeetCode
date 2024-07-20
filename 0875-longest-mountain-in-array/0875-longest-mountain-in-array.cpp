class Solution {
public:
    int longestMountain(vector<int>& arr) {
        int max_len=0;
        for(int i=0;i<arr.size();i++)
        {
            int curr=arr[i];
            int left=0;
            int right=0;
            for(int l=i;l>0;l--)
            {
                if(arr[l]>arr[l-1])
                {
                    left+=1;
                }
                else
                {
                    break;
                }
            }
            for(int r=i+1;r<arr.size();r++)
            {
                if(arr[r-1]>arr[r])
                {
                    right+=1;
                }
                else
                {
                    break;
                }
            }
            // cout<<arr[i]<<" "<<left<<" "<<right<<endl;
            if (left!=0 && right!=0)
            {
                max_len=max(max_len,left+right+1);
            }
        }
        return max_len;
    }
};
class Solution {
public:
    void print_arr(vector<vector<int>> &original,int rows,int cols)
    {
        for(int i=0;i<rows;i++)
        {
            for(int j=0;j<cols;j++)
            {
                cout<<original[i][j]<<" ";
            }
            cout<<endl;
        }    
    }
    vector<vector<int>> restoreMatrix(vector<int>& rowSum, vector<int>& colSum) {
        int rows=rowSum.size();
        int cols=colSum.size();

        vector<int> curr_row_sum;
        vector<int> curr_col_sum;
        
        for(int i=0;i<rows;i++)
        {
            curr_row_sum.push_back(0);
        }

        for(int i=0;i<cols;i++)
        {
            curr_col_sum.push_back(0);
        }


vector<vector<int>> original;
        for(int i=0;i<rows;i++)
        {
            vector<int> temp;
            original.push_back(temp);
            for(int j=0;j<cols;j++)
            {
                original[i].push_back(0);
            }
        }        
        // print_arr(original,rows,cols);
        for(int i=0;i<rows;i++)
        {
            for(int j=0;j<cols;j++)
            {
                cout<<original[i][j]<<endl;
                original[i][j]=min(rowSum[i]-curr_row_sum[i],colSum[j]-curr_col_sum[j]);
                curr_row_sum[i]+=original[i][j];
                curr_col_sum[j]+=original[i][j];
            }
        }
        return original;
    }
};
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int t =0;
        for(auto s : nums)
        {
            if(t==0 || t==1 || nums[t-2] != s)
            {
                nums[t] = s;
                t++;
            }
        }
    return t ;
    }
};

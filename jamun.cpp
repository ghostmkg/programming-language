#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maxArea(vector<int>& height) {
        int area=0;
        int n=height.size();
        int l=0,r=n-1;
        while(l<=r){
            int len=min(height[l],height[r]);
            int w=r-l;
            int a=len*w;
            area=max(a,area);
            if(height[l]<height[r])
                l++;
            else
                r--;
        }
        return area;
    }
};
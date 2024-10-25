//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution {
  public:
    // Function to find the number of islands.
    void solve(int i, int j,vector<vector<char>>&grid, int n, int m){
        grid[i][j] = '2';
        int dx[] = {-1,-1,-1,0,0,1,1,1};
        int dy[] = {-1,0,1,-1,1,-1,0,1};
        
        for(int k=0;k<8;k++){
            int nx = i+dx[k];
            int ny = j+dy[k];
            if(nx>=0 && ny>=0 && nx<n && ny<m && grid[nx][ny] == '1' ){
                solve(nx,ny,grid,n,m);
            }
        }
    }
    int numIslands(vector<vector<char>>& grid) {
        // Code here
        int n = grid.size();
        int m = grid[0].size();
        // vector<vector<int>>visited(n,vector<int>(m,0));
        int count = 0;
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(grid[i][j] == '1'){
                    count++;
                    solve(i,j,grid,n,m);
                }
            }
        }
        return count;
    }
};

//{ Driver Code Starts.
int main() {
    int tc;
    cin >> tc;
    while (tc--) {
        int n, m;
        cin >> n >> m;
        vector<vector<char>> grid(n, vector<char>(m, '#'));
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                cin >> grid[i][j];
            }
        }
        Solution obj;
        int ans = obj.numIslands(grid);
        cout << ans << '\n';
    }
    return 0;
}
// } Driver Code Ends
